#!/usr/bin/env python3
"""
A setuptools based setup module

Based on a template here:
https://github.com/pypa/sampleproject/blob/master/setup.py
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='blockfrost-python',
    version='0.0.1',
    description='The official Python SDK for Blockfrost API',
    long_description=long_description,
    url='https://github.com/blockfrost/blockfrost-python',
    # Author details
    author='Mathias Frøhlich',
    author_email='',
    license='Apache-2.0',
    keywords='blockfrost blockchain cardano ipfs',
    packages=find_packages(exclude=['contrib', 'docs', 'test', 'test.*']),
    python_requires='>=3.6, <4',
    install_requires=[
        "requests",
    ],
    extras_require={},
    tests_require=[
        "mock",
        'requests-mock',
    ],
    test_suite='setup.get_test_suite',
)
