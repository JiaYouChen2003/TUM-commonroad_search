import numpy as np
from SMP.motion_planner.node import PriorityNode

from SMP.motion_planner.plot_config import DefaultPlotConfig
from SMP.motion_planner.search_algorithms.best_first_search import AStarSearch


class StudentMotionPlanner(AStarSearch):
    """
    Motion planner implementation by students.
    Note that you may inherit from any given motion planner as you wish, or come up with your own planner.
    Here as an example, the planner is inherited from the AStarSearch planner.
    """
    
    def __init__(self, scenario, planningProblem, automata, plot_config=DefaultPlotConfig):
        super().__init__(scenario=scenario, planningProblem=planningProblem, automaton=automata, plot_config=plot_config)
    
    def heuristic_function(self, node_current: PriorityNode) -> float:
        """
        Function that evaluates the heuristic cost h(n) in inherited classes.
        The example provided here estimates the time required to reach the goal state from the current node.
        @param node_current: time to reach the goal
        @return:
        """
        if self.reached_goal(node_current.list_paths[-1]):
            return 0.0
        
        if self.position_desired is None:
            return self.time_desired.start - node_current.list_paths[-1][-1].time_step
        else:
            velocity = node_current.list_paths[-1][-1].velocity
            
            if np.isclose(velocity, 0):
                return np.inf
            
            else:
                return self.calc_mean_squared_error(current_node=node_current) / velocity
    
    def calc_mean_squared_error(self, current_node: PriorityNode) -> float:
        """
        Calculates the mean square error of the vehicle center to the desired goal position. The attribute
        self.position_desired is extracted from the planning problem (see method self.parse_planning_problem() )
        
        @param current_node:
        @return: mean square error
        """
        current_node_state = current_node.list_paths[-1][-1]    # get last state in current path
        pos = current_node_state.position                       # get (rear axis) position of last state
        # get positions of vehicle center (node state refers to reference point of Motion Primitives, i.e., rear axis)
        pos_veh_center = pos + np.array([self.rear_ax_dist * np.cos(current_node_state.orientation),
                                         self.rear_ax_dist * np.sin(current_node_state.orientation)])
        
        if self.position_desired[0].contains(pos_veh_center[0]):
            delta_x = 0.0
        else:
            delta_x = min([abs(self.position_desired[0].start - pos_veh_center[0]), abs(self.position_desired[0].end - pos_veh_center[0])])
        
        if self.position_desired[1].contains(pos_veh_center[1]):
            delta_y = 0
        else:
            delta_y = min([abs(self.position_desired[1].start - pos_veh_center[1]), abs(self.position_desired[1].end - pos_veh_center[1])])
        
        return 0.5 * (delta_x ** 2 + delta_y ** 2)
