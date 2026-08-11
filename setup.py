from typing import List
from setuptools import find_packages, setup

# Constant used to skip editable install flag inside requirements.txt
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads requirements.txt and returns a list of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Remove newline characters from each line
        requirements = [req.replace("\n", "") for req in requirements]

        # Remove '-e .' if present (used for local package building)
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Anusree',
    author_email='anusreeann1841@gmail.com',  # Replace with your actual email
    description='A Machine Learning end-to-end project',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)