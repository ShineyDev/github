"""
/github/github.py

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

import typing

import aiohttp

from github import http
from github.abc import Node
from github.objects import AuthenticatedUser
from github.objects import CodeOfConduct
from github.objects import License
from github.objects import Metadata
from github.objects import Organization
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

        .. note::

            You can get a personal access token, needed for this
            wrapper, from https://github.com/settings/tokens.
    base_url: Optional[:class:`str`]
        The base url used by this wrapper. This can be changed to allow
        support for GitHub Enterprise.
    user_agent: Optional[:class:`str`]
        The user-agent sent by this wrapper. This can be changed to
        allow GitHub to contact you in case of issues.
    session: Optional[:class:`aiohttp.ClientSession`]
        The session to be passed to the
        :class:`~github.http.HTTPClient`.

        .. warning::

            If you do not pass your own session, a new one will be
            created and closed during every request - this is not ideal
            for creating frequent requests to the API.

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

        Fetches the authenticated GitHub user.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.AuthenticatedUser`
            The authenticated GitHub user.
        """

        data = await self.http.fetch_authenticated_user()
        return AuthenticatedUser.from_data(data, self.http)

    async def fetch_code_of_conduct(self, key: str) -> CodeOfConduct:
        """
        |coro|

        Fetches a GitHub code of conduct.

        Parameters
        ----------
        key: :class:`str`
            The code of conduct key.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A code of conduct with the given key does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.CodeOfConduct`
            A GitHub code of conduct.
        """

        data = await self.http.fetch_code_of_conduct(key)
        return CodeOfConduct.from_data(data)

    async def fetch_all_codes_of_conduct(self) -> typing.List[CodeOfConduct]:
        """
        |coro|

        Fetches a list of GitHub codes of conduct.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.CodeOfConduct`]
            A list of GitHub codes of conduct.
        """

        data = await self.http.fetch_all_codes_of_conduct()
        return CodeOfConduct.from_data(data)

    async def fetch_license(self, key: str) -> License:
        """
        |coro|

        Fetches a GitHub license.

        Parameters
        ----------
        key: :class:`str`
            The license key.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A license with the given key does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.License`
            A GitHub license.
        """

        data = await self.http.fetch_license(key)
        return License.from_data(data)

    async def fetch_all_licenses(self) -> typing.List[License]:
        """
        |coro|

        Fetches a list of GitHub licenses.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.License`]
            A list of GitHub licenses.
        """

        data = await self.http.fetch_all_licenses()
        return License.from_data(data)

    async def fetch_metadata(self) -> Metadata:
        """
        |coro|

        Fetches GitHub metadata.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.Metadata`
            GitHub metadata.
        """

        data = await self.http.fetch_metadata()
        return Metadata.from_data(data)

    async def fetch_node(self, id: str) -> Node:
        """
        |coro|

        Fetches a GitHub node.

        Parameters
        ----------
        id: :class:`str`
            The node ID.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A node with the given id does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.abc.Node`
            A GitHub node.
        """

        # https://developer.github.com/v4/guides/using-global-node-ids/
        # TODO: implement features as described above

        data = await self.http.fetch_node(id)
        return Node.from_data(data)

    async def fetch_nodes(self, *ids: str) -> typing.List[Node]:
        """
        |coro|

        Fetches a list of GitHub nodes.

        Parameters
        ----------
        *ids: :class:`str`
            The node IDs.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A node with the given id does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.abc.Node`]
            A list of GitHub nodes.
        """

        # https://developer.github.com/v4/guides/using-global-node-ids/
        # TODO: implement features as described above

        data = await self.http.fetch_nodes(ids)
        return Node.from_data(data)

    async def fetch_organization(self, login: str) -> Organization:
        """
        |coro|

        Fetches a GitHub organization.

        Requires the ``read:org`` scope.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            An organization with the given login does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.Organization`
            A GitHub organization.
        """

        data = await self.http.fetch_organization(login)
        return Organization.from_data(data, self.http)

    async def fetch_rate_limit(self) -> RateLimit:
        """
        |coro|

        Fetches the current GitHub rate limit.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.RateLimit`
            The current GitHub rate limit.
        """

        data = await self.http.fetch_rate_limit()
        return RateLimit.from_data(data)

    async def fetch_repository(self, owner: str, name: str) -> Repository:
        """
        |coro|

        Fetches a GitHub repository.

        Parameters
        ----------
        owner: :class:`str`
            The owner's login.
        name: :class:`str`
            The repository name.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A repository with the given owner and name does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.Repository`
            A GitHub repository.
        """

        data = await self.http.fetch_repository(owner, name)
        return Repository.from_data(data, self.http)

    async def fetch_scopes(self) -> typing.List[str]:
        """
        |coro|

        Fetches a list of scopes associated with the token.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`str`]
            A list of scopes associated with the token
        """

        data = await self.http.fetch_scopes()
        return data

    async def fetch_topic(self, name: str) -> Topic:
        """
        |coro|

        Fetches a GitHub topic.

        Parameters
        ----------
        name: :class:`str`
            The topic name.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A topic with the given name does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.Topic`
            A GitHub topic.
        """

        data = await self.http.fetch_topic(name)
        return Topic.from_data(data)

    async def fetch_user(self, login: str) -> User:
        """
        |coro|

        Fetches a GitHub user.

        Parameters
        ----------
        login: :class:`str`
            The user's login.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A user with the given login does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`~github.User`
            A GitHub user.
        """

        data = await self.http.fetch_user(login)
        return User.from_data(data, self.http)
    