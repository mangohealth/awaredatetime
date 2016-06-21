#!/usr/bin/env python

import os
import re
from setuptools import setup, find_packages


install_requires = [
    "pytz",
]

tests_require = [
]

setup_requires = [
    "flake8",
]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.

    Slightly modified from https://github.com/tomchristie/django-rest-framework/blob/master/setup.py
    """
    init_py_filename = os.path.join(package, "__init__.py")
    with open(init_py_filename) as f:
        return re.search("__version__\s*=\s*['\"]([^'\"]+)['\"]", f.read()).group(1)
    raise RuntimeError("Failed to parse version from: %s" % init_py_filename)

setup(
    name="awaredatetime",
    version=get_version("awaredatetime"),
    description="Drop-in replacement for timezone aware datetime objects",
    long_description=(
        open("README.rst").read().strip() + "\n\n" +
        open("CONTRIBUTING.rst").read().strip() + "\n\n" +
        open("CHANGELOG.rst").read().strip() + "\n\n"
    ),
    classifiers=[
        'Intended Audience :: Developers',
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="python datetime timezone aware awaredatetime utc",
    url="https://github.com/mangohealth/awaredatetime",
    author="Mango Health",
    author_email="opensource@mangohealth.com",
    license="Apache 2.0",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite="tests",
    setup_requires=setup_requires,
)
