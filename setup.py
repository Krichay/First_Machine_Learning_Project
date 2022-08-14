from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup function
PROJECT_NAME="housing-price-predictor"
VERSION="0.0.3"
AUTHOR="Chaitanya"
DESCRIPTION="This is first Machine Learning Project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function returns list of requirements specified in
    requirements.txt file

    return This function returns list that contains name of libraries mentioned
    in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()
)