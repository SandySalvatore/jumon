#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from setuptools import setup


ROOT = os.path.dirname(os.path.abspath(__file__))
README_PATH = os.path.join(ROOT, 'README')

try:
    with open(README_PATH, 'rb') as fp:
        long_desc = fp.read().encode('utf8')
except:
    long_desc = ''

requires = []

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.4',
    "Topic :: Software Development",
    ]


setup(
    name='jumon',
    version='1.1.11.altair',
    url='https://github.com/TakesxiSximada/jumon',
    license='Apache License 2.0',
    author='TakesxiSximada',
    author_email='takesxi.sximada@gmail.com',
    description='The small framework for sub commands.',
    long_description=long_desc,
    zip_safe=False,
    classifiers=classifiers,
    platforms='any',
    py_modules=['jumon'],
    include_package_data=True,
    install_requires=requires,
    )
