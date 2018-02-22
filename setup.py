from setuptools import find_packages, setup
PACKAGE_NAME = "ethnicity_guesser"

if __name__ == "__main__":
    setup(
        name         = 'ethnicity-guesser',
        version      = '0.1',
        packages     = [PACKAGE_NAME],
        package_dir  = {
            PACKAGE_NAME: '.',
        },
        package_data = {
            PACKAGE_NAME: ['pickled_classifiers/*', "pickled_names/*"],
        },
    )
