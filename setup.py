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
    version='0.2.0',
    description='The official Python SDK for Blockfrost API v0.1.27',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blockfrost/blockfrost-python',
    # Author details
    author='https://github.com/mathiasfrohlich',
    author_email='',
    license='Apache-2.0',
    keywords='blockfrost blockchain cardano ipfs',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'tests.*']),
    python_requires='>=3.7, <4',
    install_requires=[
        "requests",
    ],
    extras_require={},
    tests_require=[
        "mock",
        'requests-mock',
    ],
    test_suite='setup.get_test_suite',

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: Apache-2.0',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
