import atexit

# %%

# Cirrus produces logs. Here we enable printing them in the notebook
from cirrus import utilities, automate, setup

utilities.set_logging_handler()


# automate.make_ubuntu_build_image("cirrus_ubuntu_build_image")
#
automate.make_executables(
    setup.PUBLISHED_BUILD + "/executables/ubuntu",
    ("self", "cirrus_ubuntu_build_image"),
    "ubuntu"
)

# automate.make_amazon_build_image("cirrus_amazon_build_image")

# automate.make_executables(
#     setup.PUBLISHED_BUILD + "/executables/amazon",
#     ("self", "cirrus_amazon_build_image"),
#     "ec2-user"
# )

atexit._run_exitfuncs()
