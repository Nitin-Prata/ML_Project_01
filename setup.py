from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> list[str]:
    '''
    This function reads the requirements file and returns a list of requirements
    '''
    
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Corrected this line
        requirements = [req.replace('\n', '') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='mlproject',
    version='0.0.1',  # Fixed version string
    author='Nitin Kumar',
    author_email='nitinpratap997@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
