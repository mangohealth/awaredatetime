#!/usr/bin/env python

import os
import re
import shutil
import subprocess
from setuptools import setup, find_packages, Command
from setuptools.command.test import test as test_cmd

pkg_name = "awaredatetime"

install_requires = [
    "pytz",
]

tests_require = [
    "flake8",
    "unittest2",
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

version = get_version(pkg_name)


class test_dev_cmd(test_cmd):
    def run(self):
        # Install dependencies
        if self.distribution.install_requires:
            self.distribution.fetch_build_eggs(
                self.distribution.install_requires)
        if self.distribution.tests_require:
            self.distribution.fetch_build_eggs(self.distribution.tests_require)

        # Use the flake8 setup.py command (declared via entry_points in flake8's setup.py)
        self.run_command("flake8")

        # Run the unittests as normal
        return test_cmd.run(self)  # Can't use super() since test_cmd is an old-style class...


def publish_helper(setup_cmd, env):
    # Cleanup old builds
    shutil.rmtree("dist", ignore_errors=True)
    shutil.rmtree("build", ignore_errors=True)
    shutil.rmtree("%s.egg-info" % pkg_name, ignore_errors=True)

    # Build Python package
    setup_cmd.run_command("bdist_wheel")

    # Register & upload to PyPi
    subprocess.check_call("twine register -r %s dist/*" % env, shell=True)
    subprocess.check_call("twine upload -r %s dist/*" % env, shell=True)

    # Update git tags
    subprocess.check_call("git tag v%s && git push origin --tags && git push upstream --tags" % version, shell=True)


class publish_test(Command):
    description = "Publishes to test PyPi environment"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        publish_helper(self, "test")


class publish_pypi(Command):
    description = "Publishes to PyPi environment"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        publish_helper(self, "pypi")


setup(
    name=pkg_name,
    version=version,
    description="Drop-in replacement for timezone aware datetime objects",
    long_description=(
        open("README.rst").read().strip() + "\n\n" +
        open("CONTRIBUTING.rst").read().strip() + "\n\n" +
        open("CHANGELOG.rst").read().strip() + "\n\n"
    ),
    classifiers=[
        "Intended Audience :: Developers",
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
    cmdclass={
        "test_dev": test_dev_cmd,
        "publish_test": publish_test,
        "publish_pypi": publish_pypi,
    },
)
