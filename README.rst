nose-tap
==========

|version| |license| |travis| |travisosx| |appveyor| |coverage|

.. |version| image:: https://img.shields.io/pypi/v/nose-tap.svg
    :target: https://pypi.python.org/pypi/nose-tap
    :alt: PyPI version
.. |license| image:: https://img.shields.io/pypi/l/nose-tap.svg
    :target: https://raw.githubusercontent.com/python-tap/nose-tap/master/LICENSE
    :alt: BSD license
.. |downloads| image:: https://img.shields.io/pypi/dm/nose-tap.svg
    :target: https://pypi.python.org/pypi/nose-tap
    :alt: Downloads
.. |travis| image:: https://img.shields.io/travis/python-tap/nose-tap/master.svg?label=linux+build
    :target: https://travis-ci.org/python-tap/nose-tap
    :alt: Linux status
.. |travisosx| image:: https://img.shields.io/travis/python-tap/nose-tap/master.svg?label=os+x+build
    :target: https://travis-ci.org/python-tap/nose-tap
    :alt: OS X status
.. |appveyor| image:: https://img.shields.io/appveyor/ci/mblayman/nose-tap/master.svg?label=windows+build
    :target: https://ci.appveyor.com/project/mblayman/nose-tap
    :alt: Windows status
.. |coverage| image:: https://img.shields.io/codecov/c/github/python-tap/nose-tap.svg
    :target: https://codecov.io/github/python-tap/nose-tap
    :alt: Coverage

Test Anything Protocol (TAP) reporting plugin for
`nose <http://nose.readthedocs.io/en/latest/>`_

The plugin outputs test results as TAP data in a variety of formats.
See the `tappy documentation <http://tappy.readthedocs.io/en/latest/producers.html#nose-tap-plugin>`_
for more information on usage.

Install
-------

.. code-block:: console

   $ pip install nose-tap

Usage
-----

This is an example usage from the plugin's test suite.

.. code-block:: console

   $ nosetests --with-tap --tap-stream
   # TAP results for TestPlugin
   ok 1 - test_adds_error (nose_tap.tests.test_plugin.TestPlugin)
   ok 2 - test_adds_failure (nose_tap.tests.test_plugin.TestPlugin)
   ok 3 - test_adds_skip (nose_tap.tests.test_plugin.TestPlugin)
   ok 4 - test_adds_success (nose_tap.tests.test_plugin.TestPlugin)
   ok 5 - A bad format string exits the runner.
   ok 6 - test_dummy_stream_does_nothing (nose_tap.tests.test_plugin.TestPlugin)
   ok 7 - test_finalize_generates_reports (nose_tap.tests.test_plugin.TestPlugin)
   ok 8 - When the test is actually a ContextSuite, get the name from context.
   ok 9 - test_non_streaming_passes_stream_through (nose_tap.tests.test_plugin.TestPlugin)
   ok 10 - test_parser_adds_options (nose_tap.tests.test_plugin.TestPlugin)
   ok 11 - test_streaming_option_captures_stream (nose_tap.tests.test_plugin.TestPlugin)
   ok 12 - test_streaming_options_returns_dummy_stream (nose_tap.tests.test_plugin.TestPlugin)
   1..12
