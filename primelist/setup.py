# setup.py
from setuptools import setup, find_packages

setup(
    name='prime_package',
    version='0.1',
    packages=find_packages(),
    description='A package for generating prime numbers',
    author='inishevv',
    author_email='einishev@bk.ru',
    url='https://github.com/inishevv/primelist',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)