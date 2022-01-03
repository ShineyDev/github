.. raw:: html

    <p align="center">
        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3AAnalyze">
            <img alt="Analyze Status" src="https://github.com/ShineyDev/github/workflows/Analyze/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ABuild">
            <img alt="Build Status" src="https://github.com/ShineyDev/github/workflows/Build/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ACheck">
            <img alt="Check Status" src="https://github.com/ShineyDev/github/workflows/Check/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ADeploy">
            <img alt="Deploy Status" src="https://github.com/ShineyDev/github/workflows/Deploy/badge.svg?event=push" />
        </a>

        <a href="https://github.com/ShineyDev/github/actions?query=workflow%3ALint">
            <img alt="Lint Status" src="https://github.com/ShineyDev/github/workflows/Lint/badge.svg?event=push" />
        </a>
    </p>

----------

.. raw:: html

    <h1 align="center">ShineyDev/github</h1>
    <p align="center">An asynchronous Python library for interaction with GitHub's GraphQL API.<br><a href="https://docs.shiney.dev/github">documentation</a> | <a href="https://github.com/ShineyDev/github/tree/dotcom/examples">examples</a></p>


Install
-------

.. code:: shell

    $ pip install --upgrade git+https://github.com/ShineyDev/github.git@dotcom


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


.. raw:: html

    <h6 align="center">Copyright 2019-present ShineyDev<br>This repository is not endorsed by or affiliated with GitHub Inc. or its affiliates. "GitHub" is a registered trademark of GitHub Inc.</h6>
