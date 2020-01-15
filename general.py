import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

create_project_dir('cisco')

