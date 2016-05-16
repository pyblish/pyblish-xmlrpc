from setuptools import setup, find_packages

import os
import imp

version_file = os.path.abspath("pyblish_rpc/version.py")
version_mod = imp.load_source("version", version_file)
version = version_mod.version

setup(
    name='pyblish-rpc',
    version=version,
    packages=find_packages(),
    license="LGPL",
    long_description=open('README.md').read(),
)
