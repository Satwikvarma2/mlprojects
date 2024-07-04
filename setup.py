from setuptools import find_packages,setup
from typing import List


hypenE="-e ."
def get_requirements(filepath:str)->List[str]:
    '''this function will return a set of requirements'''

    requirements=[]
    with open(filepath) as file:
        requirements=file.readlines()
        requirements=[req.replace("/n","")for req in requirements]

        if hypenE in requirements:
            requirements.remove(hypenE)

setup(
    name = 'mlproject',
    version = '0.01',
    author = 'Satwik',
    author_email = 'satwikvarmakunaparaju@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )