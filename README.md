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

# How to Run:
python3 -m questionnaire_analysis file_path_to_csv





# questionnaire-package


# TODO:
# CARE, GCF( CALCULATE FUNCTION MISSING), MINI_ASQ ( 0s problem), PSS(check for reverse scoring columns), RAS(totally wrong), SIAS, URCS (missing), PTM(missing), IRI (missing)
# Care doesnt work need to fix
Make a fake long csv with every questionnaire on it - check for each questionnaire compatibility - PROG
RESEARCH LAB WORKAROUND - ND
# Write down instructions on how to make this run and how to make it run for each questionnaire and everything 
# It shud be as simple to use as possible
# Documentation for how to run it specifically 
# Making a CSV to toggle to ask the user if we want to create a new csv or not - ND


EERQ fix the fragmentation issues
PIP install package
ReNaming Function
JSON for stem names convention - Give a warning t say this is being relabeled from this to this
DRY RUN
ADD IN EDGE CASES
if its less, put out a waring and compute wiht assiming its 0
To make sure the item numners are correct


# So we want to treat it as a df rather then a csv
# We want to input the file path as a method rather then using it as an argument as we want to use it for functions