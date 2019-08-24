.. currentmodule:: github


Introduction
============

This is the documentation of github.py. An asynchronous python wrapper for the GitHub API, v4.


Installation
------------

**Python 3.5.2 or higher is required.**

To install a ``final`` version of the wrapper do one of the following:

.. code:: sh

    # Windows (PyPI)
    py -3 -m pip install --upgrade github.py

    # Linux / OS X (PyPI)
    python3 -m pip install --upgrade github.py

To install the development version of the wrapper do one of the following:

.. code:: sh

    # Windows (Git)
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    py -3 -m pip install --upgrade .

    # Windows (Git, shorthand)
    py -3 -m pip install --upgrade git+https://github.com/ShineyDev/github.py
    
    # Linux / OS X (Git)
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    python3 -m pip install --upgrade .

    # Linux / OS X (Git, shorthand)
    python3 -m pip install --upgrade git+https://github.com/ShineyDev/github.py

To install documentation dependencies do one of the following:

.. code:: sh

    # Windows (Git)
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    py -3 -m pip install --upgrade .[docs]

    # Windows (Git, shorthand)
    py -3 -m pip install --upgrade git+https://github.com/ShineyDev/github.py#egg=github.py[docs]

    # Linux / OS X (Git)
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    python3 -m pip install --upgrade .[docs]

    # Linux / OS X (Git, shorthand)
    python3 -m pip install --upgrade git+https://github.com/ShineyDev/github.py#egg=github.py[docs]


Examples
--------

Fetch a repository's license:

.. code:: py

    import github
    g = github.GitHub("token")
    # you'll need a personal access token to use this library - you can get
    # one from https://github.com/settings/tokens. for this example, your
    # token will need the `public_repo` scope.

    repo = await g.fetch_repository("ShineyDev", "github.py")
    license = repo.license

You can find more examples in the |examples_directory|.


.. |examples_directory| replace:: |examples_directory_link|_
.. |examples_directory_link| replace:: examples directory
.. _examples_directory_link: https://github.com/ShineyDev/github.py/tree/master/examples
