from setuptools import find_packages, setup

setup(
    name         = 'ethnicity-guesser',
    version      = '1.0',
    packages     = ['guesser'],
    package_dir  = {
        'guesser': '.',
    },
    package_data = {
        'guesser':   ['./*'],
    },
)
