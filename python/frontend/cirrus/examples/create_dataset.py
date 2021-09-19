from cirrus import utilities, automate, setup

utilities.set_logging_handler()

automate.create_data_files(
    setup.PUBLISHED_BUILD + "/executables/ubuntu",
    ("self", "cirrus_ubuntu_build_image"),
    "ubuntu"
)

print("DONE")
