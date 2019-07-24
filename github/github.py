"""
/github/github.py

    Copyright (c) 2019 ShineyDev
    
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

import aiohttp
import typing

from github import http
from github.objects import codeofconduct
from github.objects import license
from github.objects import metadata
from github.objects import ratelimit
from github.objects import repository
from github.objects import topic
from github.objects import user
from github.objects.abc import node


class GitHub():
    """
    Represents a GitHub 'connection' or token.

    This is the base class of the wrapper and is used to interact with
    the GitHub API.

    Parameters
    ----------
    token: :class:`str`
        The authentication token. Do not prefix this token with
        anything, the wrapper will do this for you.

        You can get a personal access token, needed for this wrapper,
        from https://github.com/settings/tokens.
    base_url: Optional[:class:`str`]
        The base url used by this wrapper. This can be changed to allow
        support for GitHub Enterprise.
    user_agent: Optional[:class:`str`]
        The user-agent sent by this wrapper. This can be changed to
        allow GitHub to contact you in case of issues.
    session: Optional[:class:`aiohttp.ClientSession`]
        The session to be passed to the :class:`~github.http.HTTPClient`.

        .. warning::

            If you don't pass your own session, a new one will be
            created and closed during every request - this is not ideal
            for creating more-or-less frequent requests to the API.

    Attributes
    ----------
    http: :class:`~github.http.HTTPClient`
        The HTTPClient for the passed token. This is only exposed for
        :meth:`~github.http.HTTPClient.request`.
    """

    __slots__ = ("http",)

    def __init__(self, token: str, *, base_url: str=None, user_agent: str=None, session: aiohttp.ClientSession=None):
        self.http = http.HTTPClient(token, base_url=base_url, user_agent=user_agent, session=session)

    @property
    def base_url(self) -> str:
        """
        The base url used by this wrapper. This can be changed to allow
        support for GitHub Enterprise.
        """

        return self.http.base_url

    @base_url.setter
    def base_url(self, value: str=None):
        self.http.base_url = value

    @property
    def user_agent(self) -> str:
        """
        The user-agent sent by this wrapper. This can be changed to
        allow GitHub to contact you in case of issues.
        """

        return self.http.user_agent

    @user_agent.setter
    def user_agent(self, value: str=None):
        self.http.user_agent = value

    async def fetch_authenticated_user(self) -> user.AuthenticatedUser:
        """
        |coro|


        """

        data = await self.http.fetch_authenticated_user()
        return user.AuthenticatedUser.from_data(data, self.http)

    async def fetch_code_of_conduct(self, key: str) -> codeofconduct.CodeOfConduct:
        """
        |coro|


        """

        data = await self.http.fetch_code_of_conduct(key)
        return codeofconduct.CodeOfConduct.from_data(data)

    async def fetch_codes_of_conduct(self, *keys: str) -> typing.Iterable[codeofconduct.CodeOfConduct]:
        """
        |coro|


        """

        data = await self.http.fetch_codes_of_conduct(*keys)
        return codeofconduct.CodeOfConduct.from_data(data)

    async def fetch_all_codes_of_conduct(self) -> typing.Iterable[codeofconduct.CodeOfConduct]:
        """
        |coro|


        """

        data = await self.http.fetch_all_codes_of_conduct()
        return codeofconduct.CodeOfConduct.from_data(data)

    async def fetch_license(self, key: str) -> license.License:
        """
        |coro|


        """

        data = await self.http.fetch_license(key)
        return license.License.from_data(data)

    async def fetch_licenses(self, *keys: str) -> typing.Iterable[license.License]:
        """
        |coro|


        """

        data = await self.http.fetch_licenses(*keys)
        return license.License.from_data(data)

    async def fetch_all_licenses(self) -> typing.Iterable[license.License]:
        """
        |coro|


        """

        data = await self.http.fetch_all_licenses()
        return license.License.from_data(data)

    async def fetch_metadata(self) -> metadata.Metadata:
        """
        |coro|


        """

        data = await self.http.fetch_metadata()
        return metadata.Metadata.from_data(data)

    async def fetch_node(self, id: str) -> node.Node:
        """
        |coro|


        """

        data = await self.http.fetch_node(id)
        return node.Node.from_data(data)

    async def fetch_nodes(self, *ids: str) -> typing.Iterable[node.Node]:
        """
        |coro|


        """

        data = await self.http.fetch_nodes(*ids)
        return node.Node.from_data(data)

    async def fetch_rate_limit(self) -> ratelimit.RateLimit:
        """
        |coro|


        """

        data = await self.http.fetch_rate_limit()
        return ratelimit.RateLimit.from_data(data)

    async def fetch_repository(self, owner: str, name: str) -> repository.Repository:
        """
        |coro|


        """

        data = await self.http.fetch_repository(owner, name)
        return repository.Repository.from_data(data, self.http)

    async def fetch_topic(self, name: str) -> topic.Topic:
        """
        |coro|


        """

        data = await self.http.fetch_topic(name)
        return topic.Topic.from_data(data)

    async def fetch_topics(self, *names: str) -> typing.Iterable[topic.Topic]:
        """
        |coro|


        """

        data = await self.http.fetch_topics(*names)
        return topic.Topic.from_data(data)

    async def fetch_user(self, login: str) -> user.User:
        """
        |coro|


        """

        data = await self.http.fetch_user(login)
        return user.User.from_data(data, self.http)

    async def fetch_users(self, *logins: str) -> typing.Iterable[user.User]:
        """
        |coro|


        """

        data = await self.http.fetch_users(*logins)
        return user.User.from_data(data, self.http)
    