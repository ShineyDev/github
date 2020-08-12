"""
/github/iterator.py

    Copyright (c) 2019-2020 ShineyDev

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from github import http
from github import utils


class CollectionIterator():
    """
    An |aiter_link|_ implementation used for collections.

    Example
    -------

    .. code-block::

        # fetch issues in a repository, iterate over them.

        repo = await client.fetch_repository("ShineyDev", "github.py")
        async for (issue) in repo.fetch_issues():
            ...
    """

    __slots__ = ("_collector", "_filter_func", "_map_func", "filter_func",
                 "map_func", "_current_page", "_has_next_page", "_paginate",
                 "_args", "_kwargs")

    def __init__(self, collector, *args, filter_func=None, map_func=None, **kwargs):
        self._collector = collector
        
        _self = lambda s: s
        _true = lambda _: True

        self._filter_func = filter_func or _true
        self._map_func = map_func or _self
        self.filter_func = _true
        self.map_func = _self

        self._current_page = None
        self._has_next_page = True
        self._paginate = kwargs.pop("_paginate", False)

        self._args = args
        self._kwargs = kwargs

    def __aiter__(self):
        return self

    async def __anext__(self):
        if not self._current_page and not self._has_next_page:
            # the previous iteration popped the final item
            raise StopAsyncIteration

        if self._current_page:
            # we already have a page, pop from it
            return self._current_page.pop(0)

        # this is the first page or the previous one was popped
        # let's collect the next one
        nodes, self._kwargs["cursor"], self._has_next_page = \
            await self._collector(*self._args, **self._kwargs)

        new_nodes = list()
        for (node) in nodes:
            pred = await utils.maybe_coro(self._filter_func, node)
            pred = pred and await utils.maybe_coro(self.filter_func, node)
            if not pred:
                continue

            node = await utils.maybe_coro(self._map_func, node)
            node = await utils.maybe_coro(self.map_func, node)

            new_nodes.append(node)

        if not new_nodes and not self._has_next_page:
            # all nodes were filtered or the collection was empty
            raise StopAsyncIteration

        if self._paginate:
            return new_nodes

        self._current_page = new_nodes
        return self._current_page.pop(0)

    def __length_hint__(self):
        return self._kwargs.get("first", http._DEFAULT_PAGE_LENGTH)

    def map(self, func):
        """
        This is similar to the built-in :func:`map <py:map>` function.

        Example
        -------

        .. code-block::

            # fetch followers of a user, iterate over their logins.

            user = await client.fetch_user("ShineyDev")
            async for login in user.fetch_followers().map(lambda u: u.login):
                ...

        Parameters
        ----------
        func
            The mapping function.

        Returns
        -------
        CollectionIterator
            Itself, for fluent-style chaining.
        """

        self.map_func = func
        return self

    def filter(self, func):
        """
        This is similar to the built-in :func:`filter <py:filter>`
        function.

        Example
        -------

        .. code-block::

            # fetch comments on an issue, iterate over a specific user's comments.

            def filter_func(user):
                return user.database_id == 480938

            issue = repo.fetch_issue(1497)
            async for comment in issue.fetch_comments().filter(filter_func):
                ...

        Parameters
        ----------
        func
            The filter predicate.

        Returns
        -------
        CollectionIterator
            Itself, for fluent-style chaining.
        """

        self.filter_func = func
        return self

    async def flatten(self):
        """
        |coro|

        Flattens the iterator into a list of its items.

        Example
        -------

        .. code-block::

            # fetch members of an organization, flatten them into a list.

            org = await client.fetch_organization("python")
            members = await org.fetch_members().flatten()
            ...

        Returns
        -------
        List[Any]
            A list of its items.
        """

        return [e async for e in self]
