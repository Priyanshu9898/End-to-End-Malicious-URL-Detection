import sys
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:

    # This will return a list of requirements
    requirements = []

    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name = "Malicious URL Detection",
    author = "Priyanshu Malaviya",
    author_email = "priyanshumalaviya9210@gmail.com",
    version = "0.0.1",
    description = "Malicious URL Detection Project Using Machine Learning and Deep Learning",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)

