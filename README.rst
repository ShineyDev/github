.. github.py readme


github.py
=========

.. image:: https://img.shields.io/github/contributors/ShineyDev/github.py.svg
   :target: https://github.com/ShineyDev/github.py/graphs/contributors
   :alt: GitHub contributors

.. image:: https://readthedocs.org/projects/githubpy/badge/?version=latest
   :target: https://githubpy.readthedocs.io/en/latest/
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/status/github.py.svg
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI status information

.. image:: https://img.shields.io/pypi/v/github.py.svg?color=blue
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI version information

.. image:: https://img.shields.io/pypi/pyversions/github.py.svg
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI supported Python versions

.. image:: https://img.shields.io/pypi/l/github.py.svg
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI license information


An asynchronous Python wrapper for GitHub API, v4.


Features
--------

#. Easy to use, modern Pythonic API using ``async``/``await`` syntax.
#. 100% coverage of the supported GitHub API.
#. All user-facing objects and methods are documented `here <https://githubpy.readthedocs.io/en/latest/>`_.


Installation
------------

**Python 3.5.2 or higher is required.**

To install a ``final`` version of the wrapper do one of the following:

.. code:: sh

    # Windows
    py -3 -m pip install --upgrade github.py

    # Linux / OS X
    python3 -m pip install --upgrade github.py

To install the development version of the wrapper do one of the following:

.. code:: sh

    # Windows
    py -3 -m pip install --upgrade git+https://github.com/ShineyDev/github.py

    # Linux / OS X
    python3 -m pip install --upgrade git+https://github.com/ShineyDev/github.py


Examples
--------

Fetch a repository's license:

.. code:: py

    import github
    g = github.Client("token")
    # you'll need a personal access token to use this library - you can get
    # one from https://github.com/settings/tokens.

    repo = await g.fetch_repository("ShineyDev", "github.py")
    print(repo.license.name)

You can find more examples in the |examples_directory|.


.. |examples_directory| replace:: |examples_directory_link|_
.. |examples_directory_link| replace:: examples directory
.. _examples_directory_link: https://github.com/ShineyDev/github.py/tree/master/examples


Attribution
-----------

`Rapptz <https://github.com/Rapptz/>`_ for EnumMeta - Copyright (c) 2015-2019 Rapptz
