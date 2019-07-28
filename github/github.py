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
from github.abc import Node
from github.objects import AuthenticatedUser
from github.objects import CodeOfConduct
from github.objects import License
from github.objects import Metadata
from github.objects import RateLimit
from github.objects import Repository
from github.objects import Topic
from github.objects import User


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

    async def fetch_authenticated_user(self) -> AuthenticatedUser:
        """
        |coro|


        """

        data = await self.http.fetch_authenticated_user()
        return AuthenticatedUser.from_data(data, self.http)

    async def fetch_code_of_conduct(self, key: str) -> CodeOfConduct:
        """
        |coro|


        """

        data = await self.http.fetch_code_of_conduct(key)
        return CodeOfConduct.from_data(data)

    async def fetch_codes_of_conduct(self, *keys: str) -> typing.List[CodeOfConduct]:
        """
        |coro|


        """

        data = await self.http.fetch_codes_of_conduct(*keys)
        return CodeOfConduct.from_data(data)

    async def fetch_all_codes_of_conduct(self) -> typing.List[CodeOfConduct]:
        """
        |coro|


        """

        data = await self.http.fetch_all_codes_of_conduct()
        return CodeOfConduct.from_data(data)

    async def fetch_license(self, key: str) -> License:
        """
        |coro|


        """

        data = await self.http.fetch_license(key)
        return License.from_data(data)

    async def fetch_licenses(self, *keys: str) -> typing.List[License]:
        """
        |coro|


        """

        data = await self.http.fetch_licenses(*keys)
        return License.from_data(data)

    async def fetch_all_licenses(self) -> typing.List[License]:
        """
        |coro|


        """

        data = await self.http.fetch_all_licenses()
        return License.from_data(data)

    async def fetch_metadata(self) -> Metadata:
        """
        |coro|


        """

        data = await self.http.fetch_metadata()
        return Metadata.from_data(data)

    async def fetch_node(self, id: str) -> Node:
        """
        |coro|


        """

        data = await self.http.fetch_node(id)
        return Node.from_data(data)

    async def fetch_nodes(self, *ids: str) -> typing.List[Node]:
        """
        |coro|


        """

        data = await self.http.fetch_nodes(*ids)
        return Node.from_data(data)

    async def fetch_rate_limit(self) -> RateLimit:
        """
        |coro|


        """

        data = await self.http.fetch_rate_limit()
        return RateLimit.from_data(data)

    async def fetch_repository(self, owner: str, name: str) -> Repository:
        """
        |coro|


        """

        data = await self.http.fetch_repository(owner, name)
        return Repository.from_data(data, self.http)

    async def fetch_topic(self, name: str) -> Topic:
        """
        |coro|


        """

        data = await self.http.fetch_topic(name)
        return Topic.from_data(data)

    async def fetch_topics(self, *names: str) -> typing.List[Topic]:
        """
        |coro|


        """

        data = await self.http.fetch_topics(*names)
        return Topic.from_data(data)

    async def fetch_user(self, login: str) -> User:
        """
        |coro|


        """

        data = await self.http.fetch_user(login)
        return User.from_data(data, self.http)

    async def fetch_users(self, *logins: str) -> typing.List[User]:
        """
        |coro|


        """

        data = await self.http.fetch_users(*logins)
        return User.from_data(data, self.http)
    