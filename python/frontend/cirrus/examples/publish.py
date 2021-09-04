
from python.frontend.cirrus.cirrus import utilities, automate, setup

# Cirrus produces logs, but they will not show unless we add a handler that prints.
utilities.set_logging_handler()

# When Cirrus users run the setup script, a serverless function (AWS Lambda function) is created.
# The Lambda package provides the code for it.

automate.make_lambda_package(setup.PUBLISHED_BUILD + "/lambda_package", setup.PUBLISHED_BUILD + "/executables")



