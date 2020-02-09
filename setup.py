# -*- coding: utf-8 -*-
# -*- author: Three Zhang -*-


import os
import sys
from setuptools import setup, find_packages

py_version = sys.version_info[:2]

if py_version < (3, 4):
    raise RuntimeError('On Python 3, Quantmatrix requires Python 3.4 or later')

requires = []
tests_require = []
if py_version < (3, 3):
    tests_require.append('mock')

testing_extras = tests_require + [
    'pytest',
    'pytest-cov',
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.md')).read()
except IOError as e:
    README = """ """
    CHANGES = """ """

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: No Input/Output (Daemon)',
    'Intended Audience :: System Administrators',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: System :: Boot',
    'Topic :: System :: Monitoring',
    'Topic :: System :: Systems Administration',
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

version_txt = os.path.join(here, 'quantmatrix/version.txt')
quantmatrix_version = open(version_txt).read().strip()

dist = setup(
    name='quantmatrix',
    version=quantmatrix_version,
    license='GPL-v3.0 (https://github.com/quantmatrix/quantmatrix/LICENSE.txt)',
    url='http://quantmatrix.org/',
    description="Machine learning automatic quantitative trading system",
    long_description=README + '\n\n' + CHANGES,
    classifiers=CLASSIFIERS,
    author="Three Zhang",
    author_email="quantmatrix.org@gmail.com",
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        'testing': testing_extras,
    },
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=False,
    test_suite="quantmatrix.tests",
    entry_points={
        'console_scripts': [
            'qmquant = quantmatrix.qmquant:main',
            'qmpump = quantmatrix.qmpump:main',
            'qmweb = quantmatrix.qmweb:main'
        ],
    },
)
