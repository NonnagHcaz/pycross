#!/usr/bin/env python

from __future__ import absolute_import, print_function, division
try:
    from setuptools import setup, find_packages
except ImportError:
    raise RuntimeError('No suitable version of setuptools detected.')
import codecs
import os
import re

HERE = os.path.abspath(os.path.dirname(__file__))

###############################################################################


def read(*parts):
    with codecs.open(
        os.path.join(HERE, *parts), 'rb', 'utf-8'
    ) as file_pointer:
        return file_pointer.read()


META_FILE = read(* ['pycross', '__init__.py'])


def find_meta(meta):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE,
        re.M)

    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


def get_dependencies():
    rfile = os.path.join(HERE, 'requirements.txt')
    reqs = []
    if os.path.exists(rfile):
        with codecs.open(rfile, 'rb', 'utf-8') as file_pointer:
            reqs = file_pointer.read().splitlines()
    return reqs


setup(
    name=find_meta('title'),
    version=find_meta('version'),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    url=find_meta('uri'),
    license=find_meta('license'),
    author=find_meta('author'),
    author_email=find_meta('email'),
    description=find_meta('summary'),
    maintainer=find_meta('author'),
    maintainer_email=find_meta('email'),
    keywords=find_meta('title'),
    long_description=read('README.rst') + '\n\n' + read('HISTORY.rst'),
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=get_dependencies(),
    zip_safe=False,
    classifiers=find_meta('classifiers').split('\n'),
    include_package_data=True,
    test_suite='tests')
