from setuptools import setup, find_packages

setup(
    name='sapphire',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'sapp = sapp.cli:cli',  # Change main to cli
        ],
    },
)
