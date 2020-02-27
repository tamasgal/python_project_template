#!usr/bin/env python
# -*- coding: utf-8 -*-
# Filename: setup.py
"""
Foo setup script.

"""

from setuptools import setup, find_packages

PACKAGE_NAME = 'foo'
URL = 'https://git.km3net.de/yname/foo'
DESCRIPTION = 'The foo project.'
__author__ = 'Your Name'
__email__ = 'yname@km3net.de'

with open('requirements.txt') as fobj:
    REQUIREMENTS = [l.strip() for l in fobj.readlines()]

setup(
    name=PACKAGE_NAME,
    url=URL,
    description=DESCRIPTION,
    author=__author__,
    author_email=__email__,
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=REQUIREMENTS,
    python_requires='>=2.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
    ],
)
