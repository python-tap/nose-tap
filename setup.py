# Copyright (c) 2017, Matt Layman
"""
nose-tap is a reporting plugin for nose that outputs
`Test Anything Protocol (TAP) <http://testanything.org/>`_ data.
TAP is a line based test protocol for recording test data in a standard way.

Follow development on `GitHub <https://github.com/python-tap/nose-tap>`_.
Developer documentation is on
`Read the Docs <https://tappy.readthedocs.io/>`_.
"""

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py
from setuptools.command.sdist import sdist
import sys

import nose_tap


class BuildPy(build_py):
    """Custom ``build_py`` command to always build mo files for wheels."""

    def run(self):
        # Babel fails hard on Python 3. Let Python 2 make the mo files.
        if sys.version_info < (3, 0, 0):
            self.run_command("compile_catalog")
        # build_py is an old style class so super cannot be used.
        build_py.run(self)


class Sdist(sdist):
    """Custom ``sdist`` command to ensure that mo files are always created."""

    def run(self):
        self.run_command("compile_catalog")
        # sdist is an old style class so super cannot be used.
        sdist.run(self)


if __name__ == "__main__":
    with open("docs/releases.rst", "r") as f:
        releases = f.read()

    long_description = __doc__ + "\n\n" + releases

    setup(
        name="nose-tap",
        version=nose_tap.__version__,
        url="https://github.com/python-tap/nose-tap",
        license="BSD",
        author="Matt Layman",
        author_email="matthewlayman@gmail.com",
        description="Test Anything Protocol (TAP) reporting plugin for nose",
        long_description=long_description,
        packages=find_packages(),
        entry_points={"nose.plugins.0.10": ["tap = nose_tap.plugin:TAP"]},
        include_package_data=True,
        zip_safe=False,
        platforms="any",
        install_requires=["nose", "tap.py"],
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Topic :: Software Development :: Testing",
        ],
        keywords=["TAP", "unittest", "nose"],
        cmdclass={"build_py": BuildPy, "sdist": Sdist},
    )
