#%% md

# Logistic Regression
#---
# This notebook uses Cirrus to run logistic regression on the Criteo dataset.

#%% md

## Setup
#---

#%%

# To ease development, each time a cell is run, all modules will be reloaded.
#%load_ext autoreload
#%autoreload 2

#%%

import logging
import sys
import atexit
import boto3
#%%

# Cirrus produces logs, but they will not show unless we add a handler that prints.
from cirrus import utilities
utilities.set_logging_handler()

#%%

from cirrus import instance, parameter_server, automate, lr

#%% md

## Instance, server, and task
#---

#%% md

#First, we start an EC2 instance.

#%%
# ec2 = boto3.resource('ec2')
# availability_zones = ec2.meta.client.describe_availability_zones(Filters=[{'Name':'region-name', 'Values': ['us-west-1']}])
# av_zones =  ec2.meta.client.describe_availability_zones()
# exit()

inst = instance.Instance(
    name="lr_example_instance",
    disk_size=32,
    typ="m4.2xlarge",
    username='ubuntu',
    # username="ec2-user",
    ami_owner_name=("self", "cirrus_ubuntu_build_image"),
    port=22
)
inst.start()

#%% md

#Second, we create a parameter server to run on our instance.

#%%

server = parameter_server.ParameterServer(
    instance=inst,
    ps_port=22,
    error_port=23,
    num_workers=64
)

#%% md

#Third, we define our machine learning task.

#%%

task = lr.LogisticRegression(
    n_workers=1,
    n_ps=1,
    dataset="criteo-kaggle",
    learning_rate=0.0001,
    epsilon=0.0001,
    progress_callback=None,
    train_set=(0, 799),
    test_set=(800, 850),
    minibatch_size=200,
    model_bits=19,
    ps=server,
    opt_method="adagrad",
    timeout=60,
    lambda_size=192
)

#%% md

## Run
#---

#%% md

#Next, we run our machine learning task.

#%%
# task.ps._instance.
task.run()

#%% md

#Run this cell to see the present accuracy of the model.

#%%
# print("SERVER ERROR OUTPUT")
# print(server.error_output())
# for line in server.error_output().split("\n"):
#     if "Accuracy" in line:
#         print(line)

#%% md

## Cleanup
#---

#%% md

#When we're satisfied with the results, we kill our task.

#%%

# task.kill()

#%% md

#We also need to terminate our instance in order to avoid continuing charges.

#%%

# inst.cleanup()
