#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import shutil
import sys

from setuptools import find_packages, setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.

    :param package:
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.

    :param package:
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


version = get_version('boagui')

setup(
      name="boaui",
      version=version,
      description="",
      author="Joeny Bui",
      author_email="joeny.bui@gmail.com",
      platforms=["any"],
      license="MIT",
      packages=find_packages(),
)
