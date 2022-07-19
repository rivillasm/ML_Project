
from typing import List
from setuptools import setup, find_packages   # it will automatically find folders(PACKAGES) holding an _init__.py file

# declaring variables for setup functions
PROJECT_NAME = "housing_predictor"
VERSION = "0.0.1"            # any sequential number
AUTHOR = "Mario"
DESCRIPTION = "First FSDS batch ML project"
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements_list()->List[str]:
    """
    Description: is going to read a the requirements.txt file and return
    a list of requirements (string values)

    return: a list which will contain name of libraries mentioned in the file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)