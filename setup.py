#!/usr/bin/env python

from setuptools import setup, find_packages

import algorithms


setup(
    name='algorithms',
    version=algorithms.__version__,
    description='Algorithms implementations using Python',
    author='Lucas Magnum',
    author_email='lucasmagnumlopes@gmail.com',
    packages=find_packages(),
)
