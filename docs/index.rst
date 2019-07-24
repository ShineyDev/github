.. github.py documentation master file

github.py
=========

An asynchronous Python wrapper for the GitHub API, v4.

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

Objects
-------

.. toctree::

    github
    http

    objects/index

Abstract Base Classes
---------------------

.. toctree::

    objects/abc/index

Utilities
---------

.. toctree::

    utils

Other
-----

.. toctree::

    errors

Still can't find what you're looking for?

* :ref:`genindex`
* :ref:`search`
