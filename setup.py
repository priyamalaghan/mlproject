from setuptools import find_packages,setup
#find_packages : This will automatically findout all the packages that are availble in the entire Ml application in the directory that we actually created
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
    
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    
#metadata information about the entire project
setup(
    name='mlproject',
    version='0.0.1',
    author='Priya',
    author_email='priyamalaghan31@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn'] #automatically it will do the installation of all libraries
    install_requires=get_requirements('requirements.txt')
    )