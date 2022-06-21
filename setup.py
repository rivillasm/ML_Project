from setuptools import setup
from typing import List




# declering variables for setup functions
PROJECT_NAME = "housing_predictor"
VERSION = "0.0.1"            # any sequential number
AUTHOR = "Mario"
DESCRIPTION = "First FSDS batch ML project"
PACKAGES = ["housing"]        # specify the folder name
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: is going to read a the requirements.txt file and return
    a list of requirements (string values)

    return: a list which will contain name of libraries mentioned in the file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)