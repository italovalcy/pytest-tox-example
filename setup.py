#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

# Package meta-data.
NAME = "pytest-tox-example"
DESCRIPTION = "Simple Math"
URL = "https://github.com/italovalcy/pytest-tox-example"
AUTHOR = "italovalcy" 
REQUIRES_PYTHON = ">=3.6.0"

# Set package version
about = {}
about["__version__"] = "0.1.0"

class TestCoverage(Test):
    """Display test coverage."""

    description = 'run tests and display code coverage'

    def run(self):
        """Run tests quietly and display coverage report."""
        cmd = 'coverage3 run setup.py pytest %s' % self.get_args()
        cmd += '&& coverage3 report'
        try:
            check_call(cmd, shell=True)
        except CalledProcessError as exc:
            print(exc)
            print('Coverage tests failed. Fix the errors above and try again.')
            sys.exit(-1)


class Linter(SimpleCommand):
    """Code linters."""

    description = 'lint Python source code'

    def run(self):
        """Run Yala."""
        print('Yala is running. It may take several seconds...')
        try:
            cmd = 'yala *.py tests'
            check_call(cmd, shell=True)
            print('No linter error found.')
        except CalledProcessError:
            print('Linter check failed. Fix the error(s) above and try again.')
            sys.exit(-1)

# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    #packages=find_packages(exclude=("tests",)),
    #package_data={"src": ["VERSION"]},
    install_requires=["numpy"],
    extras_require={},
    include_package_data=True,
    cmdclass={
        'coverage': TestCoverage,
        'lint': Linter,
    },
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
