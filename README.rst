github.py
=========

.. image:: https://readthedocs.org/projects/githubpy/badge/?version=latest
   :target: https://githubpy.readthedocs.io/en/latest/
   :alt: Documentation Status

.. image:: https://img.shields.io/github/contributors/ShineyDev/github.py.svg
   :target: https://github.com/ShineyDev/github.py/graphs/contributors
   :alt: GitHub contributors

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

An asynchronous Python wrapper for the GitHub API, v4.

Features
--------

#. Modern, reliable, asynchronous API.
#. `Descriptive documentation <https://githubpy.readthedocs.io/en/latest/>`_.

.. #. 100% coverage of the supported GitHub API. (soon)

Installation
------------

**Python 3.5.2 or higher is required.**

To install a ``final`` version of the wrapper do the following:

.. code:: sh

    # Windows
    py -3 -m pip install --upgrade github.py

    # Linux / OS X
    python3 -m pip install --upgrade github.py

To install the development version of the wrapper do the following:

.. code:: sh
    
    # Windows
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    py -3 -m pip install --upgrade .

    # Linux / OS X
    git clone https://github.com/ShineyDev/github.py
    cd github.py
    python3 -m pip install --upgrade .

Examples
--------

Fetch a repository's license:

.. code:: py

    import github
    g = github.GitHub("token")
    # you'll need a personal access token to use this library - you can
    # get one from https://github.com/settings/tokens. for this example,
    # your token will need the `public_repo` scope.

    repo = await g.fetch_repository("ShineyDev", "github.py")
    print(repo.license)

Fetch the authenticated user's first 10 public gists with a custom query via HTTPClient.request:

.. code:: py

    import github
    g = github.GitHub("token")
    # you'll need a personal access token to use this library - you can
    # get one from https://github.com/settings/tokens. for this example,
    # your token will need the `public_repo` scope.

    query = """
      query fetch_authenticated_user_gists ($privacy: GistPrivacy!) {
        viewer {
          gists (privacy: $privacy, first: 10) {
            nodes {
              url
            }
          }
        }
      }
    """

    variables = {
        "privacy": "PUBLIC",
    }

    json = {
        "query": query,
        "variables": variables,
    }

    data = await g.http.request(json=json)
    gists = github.Gist.from_data(data["viewer"]["gists"]["nodes"], g.http)

You can find more examples in the ``examples/`` directory.
