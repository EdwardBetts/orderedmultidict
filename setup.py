#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# omdict - Ordered Multivalue Dictionary.
#
# Ansgar Grunseid
# grunseid.com
# grunseid@gmail.com
#
# License: Build Amazing Things (Unlicense)

import os
import re
import sys
from os.path import dirname, join as pjoin
from setuptools import setup, find_packages, Command
from setuptools.command.test import test as TestCommand


with open(pjoin(dirname(__file__), 'orderedmultidict', '__init__.py')) as fd:
    VERSION = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(fd.read()).group(1)


class Publish(Command):
    """Publish to PyPI with twine."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('python setup.py sdist')
        rc = os.system(
            'twine upload dist/orderedmultidict-%s.tar.gz' % VERSION)
        sys.exit(rc)


class RunTests(TestCommand):
    """
    Run the unit tests.

    By default, `python setup.py test` fails if tests/ isn't a Python
    module (that is, if the tests/ directory doesn't contain an
    __init__.py file). But the tests/ directory shouldn't contain an
    __init__.py file and tests/ shouldn't be a Python module. See

      http://doc.pytest.org/en/latest/goodpractices.html

    Running the unit tests manually here enables `python setup.py test`
    without tests/ being a Python module.
    """
    def run_tests(self):
        from unittest import TestLoader, TextTestRunner
        tests_dir = pjoin(dirname(__file__), 'tests')
        suite = TestLoader().discover(tests_dir)
        result = TextTestRunner().run(suite)
        sys.exit(0 if result.wasSuccessful() else -1)


long_description = ('''
A multivalue dictionary is a dictionary that can store multiple values for the
same key. An ordered multivalue dictionary is a multivalue dictionary that
retains the order of insertions and deletions.

omdict retains method parity with dict.

Information and documentation at https://github.com/gruns/orderedmultidict.''')

required = ['six>=1.8.0']
if sys.version_info < (2, 7):
    required.append('ordereddict')

tests_require = ['pycodestyle']
if sys.version_info[:2] < (2, 7):
    tests_require += ['unittest2']

setup(
    name='orderedmultidict',
    version=VERSION,
    author='Ansgar Grunseid',
    author_email='grunseid@gmail.com',
    url='https://github.com/gruns/orderedmultidict',
    license='Unlicense',
    description='Ordered Multivalue Dictionary - omdict.',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    platforms=['any'],
    classifiers=[
        'Topic :: Software Development :: Libraries',
        'Natural Language :: English',
        'License :: Freely Distributable',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    install_requires=required,
    cmdclass={
        'test': RunTests,
        'publish': Publish,
    },
    tests_require=tests_require,
)
