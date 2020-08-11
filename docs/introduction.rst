.. currentmodule:: github


Introduction
============

This is the documentation of github.py. An asynchronous python wrapper for interacting with GitHub API v4.


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
    license = repo.license

You can find more examples in the |examples|.


.. |examples| replace:: |examples_link|_
.. |examples_link| replace:: examples directory
.. _examples_link: https://github.com/ShineyDev/github.py/tree/master/examples
