from setuptools import setup, find_packages

setup(
    name='std',
    version='0.1',
    packages=find_packages(),
    py_modules=['python.std'],  # Update this line to include the path to std.py
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points='''
        [console_scripts]
        std=python.std:cli
    ''',
)


# pip install -e .

# The -e option stands for "editable" mode, which means the script will be installed in a way that reflects changes made to the source files without needing to reinstall.