from setuptools import find_packages, setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='autogradercpp',
    packages=find_packages(
        include=['autogradercpp']
    ),
    version='0.1.1',
    description='An autograder library for evaluating C++ programs.',
    author='Abhijat Bharadwaj (Keymii)',
    author_email='bharadwaj.abhijat@yahoo.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
