#!/usr/bin/env python3
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

long_description = (HERE / 'README.md').read_text(encoding='utf-8')

setup(
    name='blockfrost-python',
    version='0.3.0',
    description='The official Python SDK for Blockfrost API v0.1.30',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/blockfrost/blockfrost-python',
    # Author details
    author='blockfrost.io',
    author_email='contact@blockfrost.io',
    ghostwriter='https://github.com/mathiasfrohlich',
    license='Apache-2.0',
    keywords='blockfrost blockchain cardano ipfs',
    packages=find_packages(exclude=['tests', 'tests.*']),
    python_requires='>=3.7, <4',
    install_requires=[
        "requests",
    ],
    tests_require=[
        "pytest",
        "mock",
        'requests-mock',
    ],

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
