from setuptools import find_packages, setup

setup(
    name         = 'ethnicity-guesser',
    version      = '0.1',
    packages     = ['ethnicity_guesser'],
    package_dir  = {
        'ethnicity_guesser': '.',
    },
    package_data = {
        'ethnicity_guesser':   ['./*'],
    },
)
