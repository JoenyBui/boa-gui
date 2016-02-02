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
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


version = get_version('keydeck')

setup(
      name="peui",
      version=version,
      description="Protection Enginering User Interface",
      author="Joeny Bui",
      author_email="jbui@protection-consultants.com",
      platforms=["any"],
      license="BSD",
      packages=find_packages(),
)
