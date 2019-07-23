github.py
=========

.. image:: https://img.shields.io/github/contributors/ShineyDev/github.py.svg
   :target: https://github.com/ShineyDev/github.py/graphs/contributors
   :alt: GitHub contributors

.. image:: https://img.shields.io/pypi/status/github.py.svg
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI status information

.. image:: https://img.shields.io/pypi/v/github.py.svg
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI version information

.. image:: https://img.shields.io/pypi/pyversions/github.py.svg
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI supported Python versions

.. image:: https://img.shields.io/pypi/l/github.py.svg
   :target: https://pypi.python.org/pypi/github.py
   :alt: PyPI license information

An asynchronous Python wrapper for the GitHub API, v4.

Features
--------

#. Modern API using ``async`` and ``await`` syntax.

.. #. 100% coverage of the supported GitHub API. (soon)

Installation
------------

**Python 3 or higher is required.**

To install a ``final`` version of the wrapper do the following:

.. code:: sh

    # Windows
    py -3 -m pip install -U github.py

    # Linux / OS X
    python3 -m pip install -U github.py

To install the development version of the wrapper do the following:

.. code:: sh
    
    # Windows
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    py -3 -m pip install -U .

    # Linux / OS X
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    python3 -m pip install -U .

Examples
--------

Fetch a repository's license:

.. code:: py

    import asyncio
    loop = asyncio.get_event_loop()

    import github
    g = github.GitHub("token")
    # you'll need a personal access token to use this library - you can
    # get one from https://github.com/settings/tokens. for this example,
    # your token will need the `public_repo` scope.

    async def main():
        repo = await g.fetch_repository("ShineyDev", "github.py")
        return repo.license

    license = loop.run_until_complete(main())
    print(license.name)

.. You can find more examples in ``examples/``.
