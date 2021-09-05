#%% md

# Hyperparameter optimization
# ---
# This notebook uses Cirrus to optimize the hyperparameters of a logistic regression model.

#%% md

## Setup
# ---

#%%

# To ease development, each time a cell is run, all modules will be reloaded.
# %load_ext autoreload
# %autoreload 2

#%%

import logging
import sys
import atexit

#%%
from python.frontend.cirrus.cirrus import instance, automate, lr, GridSearch, utilities

# Cirrus produces logs, but they will not show unless we add a handler that prints.
utilities.set_logging_handler()


#%%


#%% md

## Instances, base task configuration, hyperparameters
#---

#%% md

# First, we start some EC2 instances.

#%%

NUM_INSTANCES = 2

instances = []
for i in range(NUM_INSTANCES):
    inst = instance.Instance(
        name="hyperparameter_example_instance_%d" % i,
        disk_size=32,
        typ="m4.2xlarge",
        username="ubuntu",
        ami_owner_name=("self", "cirrus_ubuntu_build_image")
    )
    inst.start()
    instances.append(inst)

#%% md

# Second, we define the base configuration for our machine learning task.

#%%

base_task_config = {
    "n_workers": 1,
    "n_ps": 1,
    "dataset": "criteo-kaggle",
    "learning_rate": 0.0001,
    "epsilon": 0.0001,
    "progress_callback": None,
    "train_set": (0, 799),
    "test_set": (800, 850),
    "minibatch_size": 200,
    "model_bits": 19,
    "opt_method": "adagrad",
    "timeout": 60,
    "lambda_size": 192
}

#%% md

# Third, we identify our hyperparameters and their possible values.

#%%

hyperparameter_names = [
    "n_workers",
    "learning_rate"
]
hyperparameter_values = [
    [1, 1],
    [0.001, 0.01]
]

#%% md

# All of the above defines a hyperparameter optimization task, which consists of one machine learning task per assignment of values to the hyperparameters.

#%%

search = GridSearch(
    task=lr.LogisticRegression,
    param_base=base_task_config,
    hyper_vars=hyperparameter_names,
    hyper_params=hyperparameter_values,
    instances=instances
)

#%% md

## Run
# ---

#%% md

# Next, we run our hyperparameter optimization task.

#%%

search.run()

#%% md

# Run this cell to see the present accuracy of experiment `I`.

#%%

I = 0

# for line in search.cirrus_objs[I].ps.error_output().split("\n")[-20:]:
#     print(line)

#%% md

## Cleanup
# ---

#%% md

# When we're satisfied with the results, we kill our task.

#%%

# search.kill_all()

#%% md

# We also need to terminate our instances in order to avoid continuing charges.

#%%

# for inst in instances:
#     inst.cleanup()

#%% md

# If a cell errors, running this should clean up any resources that were created. After running this cell, the kernel will become unusable and need to be restarted.

#%%

# atexit._run_exitfuncs()
