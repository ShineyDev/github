.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3AAnalyze+event%3Apush">
            <img alt="Analyze Status" src="https://github.com/ShineyDev/github/workflows/Analyze/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ABuild+event%3Apush">
            <img alt="Build Status" src="https://github.com/ShineyDev/github/workflows/Build/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ACheck+event%3Apush">
            <img alt="Check Status" src="https://github.com/ShineyDev/github/workflows/Check/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ADeploy+event%3Apush">
            <img alt="Deploy Status" src="https://github.com/ShineyDev/github/workflows/Deploy/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ALint+event%3Apush">
            <img alt="Lint Status" src="https://github.com/ShineyDev/github/workflows/Lint/badge.svg?event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">ShineyDev/github</h1>
    <p align="center">An asynchronous Python library for interaction with GitHub's GraphQL API.</p>


Install
-------

.. code:: shell

    $ pip install --upgrade git+https://github.com/ShineyDev/github.git@main


Use
---

.. code:: python

    >>> import aiohttp
    >>> import github
    >>> session = aiohttp.ClientSession()
    >>> client = github.Client(token="...", session=session)
    >>> await client.request("{viewer{login}}")
    {'viewer': {'login': 'nat'}}


.. raw:: html

    <h6 align="center">Copyright 2019-present ShineyDev<br>This repository is not sponsored by or affiliated with GitHub Inc. or its affiliates. "GitHub" is a registered trademark of GitHub Inc.</h6>
