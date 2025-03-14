FILE STRUCTURE: 
questionnaire_package/         # Top-level package folder
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

Sample main init file : 
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

Making a CSV to toggle to ask the user if we want to create a new csv or not
Should make one csv instead of multiple ones 
FILE PATHING
RESEARCH LAB WORKAROUND
setup.py
check for each questionnaire compatibility
init file for questionnaires and export for public api
main functionality check (Test)  (April 4th)
try for each questionnaire analysis functionality
PIP install package
.gitignore for whatever we need to hide
ReNaming Function
JSON for stem names convention - Give a warning t say this is being relabeled from this to this
DRY RUN
ADD IN EDGE CASES
if its less, put out a waring and compute wiht assiming its 0
To make sure the item numners are correct
Dont worry about care now. 
# PMERQ,SU,DOSPERT,UPPS,EERQ work rn, need to make sure other scripts work or not. 
EDGE CASES:
