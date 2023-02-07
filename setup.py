#we need this file to make our project installable or used as library. to distribute our project
from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT = "-e ."   # -e . to trigger the setup.py file it is in requirement.txt
def get_requirements()->List[str]:
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list


setup(
    name="insurance",
    version="0.0.1",
    author="sumit",
    author_email="bhadouriasumit27@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)