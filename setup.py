from setuptools import find_packages,setup

from typing import List

HYPEN_E_DOT='-e .'


def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path)  as file_obj:
        requirements=file_obj.readlines()

        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

jls_extract_var = "arshankhan3315@gmail.com"
setup(

    name='Dimand_price_project',

    version='0.0.1',

    author='Arshan',
    author_email=jls_extract_var,
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)