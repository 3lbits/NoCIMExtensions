from setuptools import setup, find_packages

setup(
    name='standard',
    version='0.1',
    packages=find_packages(),
    py_modules=['python.standard'],  # Update this line to include the path to standard.py
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points='''
        [console_scripts]
        standard=python.standard:main
    ''',
)


# pip install -e .

# The -e option stands for "editable" mode, which means the script will be installed in a way that reflects changes made to the source files without needing to reinstall.