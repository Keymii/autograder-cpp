from setuptools import find_packages, setup

setup(
    name='autogradercpp',
    packages=find_packages(
        include=['autogradercpp']
    ),
    version='0.1.0',
    description='An autograder library for evaluating C++ programs.',
    author='Abhijat Bharadwaj (Keymii)',
    author_email='bharadwaj.abhijat@yahoo.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[]
)
