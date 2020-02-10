# Copyright (c) 2020, Matt Layman
"""
nose-tap is a reporting plugin for nose that outputs
`Test Anything Protocol (TAP) <http://testanything.org/>`_ data.
TAP is a line based test protocol for recording test data in a standard way.

Follow development on `GitHub <https://github.com/python-tap/nose-tap>`_.
Developer documentation is on
`Read the Docs <https://tappy.readthedocs.io/>`_.
"""

from setuptools import Command, find_packages, setup

import nose_tap


class ReleaseCommand(Command):
    description = "generate distribution release artifacts"
    user_options = []

    def initialize_options(self):
        """Initialize options.

        This method overrides a required abstract method.
        """

    def finalize_options(self):
        """Finalize options.

        This method overrides a required abstract method.
        """

    def run(self):
        """Generate the distribution release artifacts.

        The custom command is used to ensure that compiling
        po to mo is not skipped.
        """
        self.run_command("compile_catalog")
        self.run_command("sdist")
        self.run_command("bdist_wheel")


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
        cmdclass={"release": ReleaseCommand},
    )
