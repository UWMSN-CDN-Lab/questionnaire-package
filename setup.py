# Sample setup.py
from setuptools import setup, find_packages

setup(
    name='questionnaire_analysis',
    version='0.1.0',
    description='A package for analyzing questionnaires from CSV files using modular scripts.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Your Name', #TODO
    author_email='your.email@example.com', # TODO
    packages=find_packages(), 
    install_requires=[
        'pandas>=1.0',  # List your dependencies here
    ],
    entry_points={
        'console_scripts': [
            'questionnaire_analysis=questionnaire_analysis.__main__:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)