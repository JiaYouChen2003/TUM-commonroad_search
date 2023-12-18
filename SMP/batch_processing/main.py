#!/usr/bin/env python
# coding: utf-8

# # Tutorial: Batch Processing
# 
# This tutorial explains how to use the batch processing script to solve CommonRoad planning problems in parallel. The configuration for batch processing is stored in `batch_processing_config.yaml`. Some of the parameters are explained as follows:
# * **input_path**: input directory of your intended CommonRoad scenarios.
# * **output_path**: output directory of CommonRoad solution files.
# * **overwrite**: whether the existing solution files should be overwritten.
# * **validate_solution**: check the validity of the solutions with the feasibility checker.
# * **num_worker_processes**: the number of parallel executions of motion planners.
# 
# Parameters specified under the `default` block will be applied to all scenarios. If you wish to specify a different paramter for specific scenarios, simply insert a new block with the content of the `default` block copied, and overwrite parameters therein. This new block should be named after the ID of the sceanrio that you wish to aplly the parameters to. Related parameters are explained as follows:
# * **vehicle_model**: model of the vehicle, valid values: **PM, KS, ST and MB**. Refer to [Vehicle Models](https://gitlab.lrz.de/tum-cps/commonroad-vehicle-models/-/blob/master/vehicleModels_commonRoad.pdf) for more information.
# * **vehicle_type**: type of the vehicle, valid values: **FORD_ESCORT, BMW_320i and VW_VANAGON**.
# * **cost_function**: id of cost function. Refer to [Cost Functions](https://gitlab.lrz.de/tum-cps/commonroad-cost-functions/-/blob/master/costFunctions_commonRoad.pdf) for more information.
# * **planner**: the planner that is used to solve for solutions, possible values are: bfs, dfs, dls, ucs, gbfs, astar, student, student_example
# * **planning_problem_idx**: index of the planning problem. for cooperative scenarios: 0, 1, 2, ..., otherwise: 0
# * **max_tree_depth**: maximum depth of the search tree
# * **timeout**: timeout time for motion planner [s].
# 
# Note: the paths can either be **relative** or **absolute**.
# To start the search with batch processing, you can either directly run `SMP/batch_processing/batch_processing_parallel.py` in IDEs (e.g. PyCharm) with `commonroad-search/` marked as sources root, or run the following script.

# ## Parallel Batch Processing
# In parallel batch processing, the search are carried out on multiple threads simultaneously. This reduces the overall time required to test your algorithm on all the given scenarios. One drawback is that it is not very easy to debug your code with parallel batch processing.

# In[ ]:


get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import os
import sys

# add the folder containing batch processing script into python path
sys.path.append(os.path.join(os.getcwd(), "../../"))

from SMP.batch_processing.batch_processing_parallel import run_parallel_processing


# In[ ]:


run_parallel_processing()


# ## Sequential Batch Processing
# 
# Alternatively, one can use the `SMP/batch_processing/batch_processing_sequential.py` script to carry out the search sequentially on a single thread. This is a more user-friendly approach if you wish you debug your code in IDES (e.g. creating breakpoints in PyCharm) but still have it run against multiple scenarios.

# In[ ]:


from SMP.batch_processing.batch_processing_sequential import run_sequential_processing
run_sequential_processing()

