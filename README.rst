.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/github/actions/workflows/analyze.yml?query=branch%3Adotcom+event%3Apush"><img alt="Analyze Status" src="https://github.com/ShineyDev/github/actions/workflows/analyze.yml/badge.svg?branch=dotcom&event=push" /></a>
        <a href="https://github.com/ShineyDev/github/actions/workflows/build.yml?query=branch%3Adotcom+event%3Apush"><img alt="Build Status" src="https://github.com/ShineyDev/github/actions/workflows/build.yml/badge.svg?branch=dotcom&event=push" /></a>
        <a href="https://github.com/ShineyDev/github/actions/workflows/check.yml?query=branch%3Adotcom+event%3Apush"><img alt="Check Status" src="https://github.com/ShineyDev/github/actions/workflows/check.yml/badge.svg?branch=dotcom&event=push" /></a>
        <a href="https://github.com/ShineyDev/github/actions/workflows/deploy.yml?query=branch%3Adotcom+event%3Apush"><img alt="Deploy Status" src="https://github.com/ShineyDev/github/actions/workflows/deploy.yml/badge.svg?branch=dotcom&event=push" /></a>
        <a href="https://github.com/ShineyDev/github/actions/workflows/lint.yml?query=branch%3Adotcom+event%3Apush"><img alt="Lint Status" src="https://github.com/ShineyDev/github/actions/workflows/lint.yml/badge.svg?branch=dotcom&event=push" /></a>
    </p>

----------

.. raw:: html

    <h1 align="center">ShineyDev/github</h1>
    <p align="center">An asynchronous Python library for interaction with GitHub's GraphQL API.<br><a href="https://github.com/ShineyDev/github">source</a> | <a href="https://docs.shiney.dev/github">documentation</a></p>


Install
-------

.. pull-quote::

    [!WARNING]

    This installation may be unstable. If you're looking for a stable release, go `here <https://github.com/ShineyDev/github/tags>`_.

.. code:: shell

    $ pip install --upgrade git+https://github.com/ShineyDev/github.git@dotcom


There is also a more in-depth `installation guide <https://docs.shiney.dev/github/latest/guide/installation>`_ in the documentation.


Use
---

.. code:: python

    >>> import aiohttp
    >>> import github
    >>>
    >>> session = aiohttp.ClientSession()
    >>> client = github.Client(token="...", session=session)
    >>>
    >>> await client.request("{viewer{login}}")
    {'viewer': {'login': 'nat'}}


There are also more in-depth `usage guides <https://docs.shiney.dev/github/latest/guide/use>`_ in the documentation.


.. raw:: html

    <h6 align="center">Copyright 2019-present ShineyDev<br>This repository is not endorsed by or affiliated with GitHub Inc. or its affiliates. "GitHub" is a registered trademark of GitHub Inc.</h6>
