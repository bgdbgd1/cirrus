
# Publish
#---
#This notebook publishes resources needed by Cirrus users. It is mainly intended for use by Cirrus developers.

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

#%%

# Cirrus produces logs, but they will not show unless we add a handler that prints.
from cirrus import utilities
utilities.set_logging_handler()

#%%

from cirrus import automate
from cirrus import setup
# import boto3
#
# iam = boto3.resource('iam')
#
# resources = iam.get_available_subresources()

## Lambda package
#---
#When Cirrus users run the setup script, a serverless function (AWS Lambda function) is created. The Lambda package provides the code for it.

#%%

automate.make_lambda_package(setup.PUBLISHED_BUILD + "/lambda_package", setup.PUBLISHED_BUILD + "/executables")

#%%


