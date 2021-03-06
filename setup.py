#!/usr/bin/env python
from setuptools import setup

import quik


long_description = open('README.rst').read()

setup(name="quik",
      version=quik.__version__,
      description="A fast and lightweight Python template engine",
      long_description=long_description,
      author="Thiago Avelino",
      author_email="thiago@avelino.xxx",
      url="https://github.com/avelino/quik",
      download_url="https://github.com/avelino/quik/tarball/master",
      bugtrack_url="https://github.com/avelino/quik/issues",
      license="MIT",
      py_modules=['quik'],
      zip_safe=False,
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing :: Markup :: HTML'],
      keywords="template, engine, web, fast, lightweight",
      include_package_data=True,)
