"""
the setup.py file is essential part of packing and distributing python projects it is  used by setuptools to define the configuration of your project,such 
as its metadata, and its dependencies and more.

"""

from setuptools import setup, find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """

    requirement_list : List[str]=[]

    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e.

                if requirement and not requirement.startswith("-e"):
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt not found.")
    return requirement_list

setup(
    name='NetworkSecurity',
    version='1.0.0',
    description='My Python Package',
    author='Krishankant Saraswat',
    author_email='kk@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)