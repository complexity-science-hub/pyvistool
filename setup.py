#!/usr/bin/env python

import re
import sys

from setuptools import setup, find_packages


def version():
    with open('pyvistool/_version.py') as f:
        return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read()).group(1)

def requirements():
  with open('requirements.txt') as f:
    return f.readlines()

setup(name='pyvistool',
      version=version(),
      packages=['pyvistool'],#find_packages(),
      install_requires=[requirements()],
      package_data={'': ['index.html']},
      include_package_data=True,
      author='',
      author_email='',
      description='',
      url='',
      #license='GNU AFFERO GENERAL PUBLIC LICENSE Version 3',
      )