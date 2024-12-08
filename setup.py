from setuptools import setup, find_packages

setup(
    name='cim4',
    version='0.1',
    packages=find_packages(),
    py_modules=['cim4CLITool.main'],  # Update this line to include the path to main.py
    install_requires=[
        'click',
        # Add other dependencies here
    ],
    entry_points='''
        [console_scripts]
        cim4=cim4CLITool.main:main
    ''',
)


# pip install -e .

# The -e option stands for "editable" mode, which means the script will be installed in a way that reflects changes made to the source files without needing to reinstall.