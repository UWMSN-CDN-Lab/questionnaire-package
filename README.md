FILE STRUCTURE: 
questionnaire_analysis/         # Top-level package folder
├── setup.py                    # (optional)
├── README.md
└── questionnaire_analysis/     # Package source code
    ├── __init__.py
    ├── __main__.py             # Central entry point
    ├── common.py               # Common functions (e.g., CSV access, questionnaire detection)
    └── questionnaires/         # Contains individual questionnaire modules
        ├── __init__.py
        ├── cbcl.py           # Contains your existing main() for CBCL analysis
        ├── eerq.py           # Contains main() for E-ERQ analysis
        └── upps.py 

This file structure should be followed for the package 


TODOS:
Look up init and setup requirements
Look up Licensing for pip install or not as well
Main File design 

Sample main init file : 

"""
pyexample.

An example python library.
"""

__version__ = "0.1.0"
__author__ = ''
__credits__ = ''

Sample Setup.py :
from setuptools import setup

setup(
    name='pyexample',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='Stephen Hudson',
    author_email='shudson@anl.gov',    
    license='BSD 2-clause',
    packages=['pyexample'],
    install_requires=['mpi4py>=2.0',
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)    


# questionnaire-package


# TODO: 


setup,py
check for each questionnaire compatibility 
init file for questionnaires and export for public api 
main functionality check (Test)  (April 4th)
try for each questionnaire analysis functionality 
