"""
/github/client.py

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

from github.http import HTTPClient
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


class Client():
    """
    Represents a GitHub connection (client).

    This is the base class of the wrapper and is used to interact with
    the GitHub API.

    Parameters
    ----------
    token: :class:`str`
        The authentication token. Do not prefix this token with
        anything, the wrapper will do this for you.

        .. note::

            You'll need a personal access token to use this wrapper,
            you can get one from https://github.com/settings/tokens.

    base_url: :class:`str`
        The base url used by this wrapper. This can be changed to allow
        support for GitHub Enterprise Server.
    user_agent: :class:`str`
        The user-agent sent by this wrapper.

        "We request that you use your GitHub username, or the name of
        your application, for the User-Agent header value. This allows
        us to contact you if there are problems."
    session: :class:`aiohttp.ClientSession`
        The session to be passed to the
        :class:`~github.http.HTTPClient`.

        .. warning::

            If you do not pass your own session, a new one will be
            created and closed during every request - this is not ideal
            for creating frequent requests to the API.

    Attributes
    ----------
    http: :class:`~github.http.HTTPClient`
        The HTTPClient for the passed token. This is exposed for
        :meth:`~github.http.HTTPClient.request`.
    """

    def __init__(self, token, *, base_url=None, user_agent=None, session=None):
        self.http = HTTPClient(token, base_url=base_url, user_agent=user_agent, session=session)

    @property
    def base_url(self):
        """
        The base url used by this wrapper. This can be changed to allow
        support for GitHub Enterprise Server.

        :type: :class:`str`
        """

        return self.http.base_url

    @base_url.setter
    def base_url(self, value):
        self.http.base_url = value

    @property
    def user_agent(self):
        """
        The user-agent sent by this wrapper.

        "We request that you use your GitHub username, or the name of
        your application, for the User-Agent header value. This allows
        us to contact you if there are problems."

        :type: :class:`str`
        """

        return self.http.user_agent

    @user_agent.setter
    def user_agent(self, value):
        self.http.user_agent = value

    async def fetch_all_codes_of_conduct(self):
        """
        |coro|

        Fetches a list of all GitHub code of conduct.

        Returns
        -------
        List[:class:`~github.CodeOfConduct`]
            A list of GitHub code of conduct.
        """

        data = await self.http.fetch_all_codes_of_conduct()
        return CodeOfConduct.from_data(data)

    async def fetch_all_licenses(self):
        """
        |coro|

        Fetches a list of all GitHub licenses.

        Returns
        -------
        List[:class:`~github.License`]
            A list of GitHub licenses.
        """

        data = await self.http.fetch_all_licenses()
        return License.from_data(data)

    async def fetch_authenticated_user(self):
        """
        |coro|

        Fetches the authenticated GitHub user, "viewer".

        Returns
        -------
        :class:`~github.AuthenticatedUser`
            The authenticated user.
        """

        data = await self.http.fetch_authenticated_user()
        return AuthenticatedUser.from_data(data, self.http)

    async def fetch_code_of_conduct(self, key):
        """
        |coro|

        Fetches a GitHub code of conduct by its key.

        Parameters
        ----------
        key: :class:`str`
            The code of conduct's key.

        Raises
        ------
        ~github.errors.NotFound
            A code of conduct with the given key does not exist.

        Returns
        -------
        :class:`~github.CodeOfConduct`
            A GitHub code of conduct.
        """

        data = await self.http.fetch_code_of_conduct(key)
        return CodeOfConduct.from_data(data)

    async def fetch_license(self, key):
        """
        |coro|

        Fetches a GitHub license by its key.

        Parameters
        ----------
        key: :class:`str`
            The license's key.

        Raises
        ------
        ~github.errors.NotFound
            A license with the given key does not exist.

        Returns
        -------
        :class:`~github.License`
            A GitHub license.
        """

        data = await self.http.fetch_license(key)
        return License.from_data(data)

    async def fetch_metadata(self):
        """
        |coro|

        Fetches GitHub metadata.

        Returns
        -------
        :class:`~github.Metadata`
            GitHub metadata.
        """

        data = await self.http.fetch_metadata()
        return Metadata.from_data(data)

    async def fetch_node(self, id):
        """
        |coro|

        Fetches a node by its ID.

        Parameters
        ----------
        id: :class:`str`
            The node's ID.

        Raises
        ------
        ~github.errors.NotFound
            A node with the given ID does not exist.

        Returns
        -------
        :class:`~github.abc.Node`
            A node.
        """

        # https://docs.github.com/en/graphql/guides/using-global-node-ids
        # TODO: implement features as described above

        data = await self.http.fetch_node(id)
        return Node.from_data(data)

    async def fetch_nodes(self, *ids):
        """
        |coro|

        Fetches a list of nodes from their IDs.

        Parameters
        ----------
        *ids: :class:`str`
            The nodes' IDs.

        Raises
        ------
        ~github.errors.NotFound
            A node with one or more of the given IDs does not exist.

        Returns
        -------
        List[:class:`~github.abc.Node`]
            A list of nodes.
        """

        # https://docs.github.com/en/graphql/guides/using-global-node-ids
        # TODO: implement features as described above

        data = await self.http.fetch_nodes(ids)
        return Node.from_data(data)

    async def fetch_organization(self, login):
        """
        |coro|

        Fetches a GitHub organization by its login.

        Requires the ``read:org`` scope.

        Raises
        ------
        ~github.errors.NotFound
            An organization with the given login does not exist.

        Returns
        -------
        :class:`~github.Organization`
            A GitHub organization.
        """

        data = await self.http.fetch_organization(login)
        return Organization.from_data(data, self.http)

    async def fetch_rate_limit(self):
        """
        |coro|

        Fetches the current rate limit.

        .. note::

            This API call does not cost you a rate limit point.

        Returns
        -------
        :class:`~github.RateLimit`
            The current rate limit.
        """

        data = await self.http.fetch_rate_limit()
        return RateLimit.from_data(data)

    async def fetch_repository(self, owner, name):
        """
        |coro|

        Fetches a GitHub repository by its owner and name.

        Parameters
        ----------
        owner: :class:`str`
            The owner's login.
        name: :class:`str`
            The repository's name.

        Raises
        ------
        ~github.errors.NotFound
            A repository with the given owner and name does not exist.

        Returns
        -------
        :class:`~github.Repository`
            A GitHub repository.
        """

        data = await self.http.fetch_repository(owner, name)
        return Repository.from_data(data, self.http)

    async def fetch_scopes(self):
        """
        |coro|

        Fetches a list of scopes given to the authenticated token.

        Returns
        -------
        List[:class:`str`]
            A list of scopes.
        """

        data = await self.http.fetch_scopes()
        return data

    async def fetch_topic(self, name):
        """
        |coro|

        Fetches a GitHub topic from its name.

        Parameters
        ----------
        name: :class:`str`
            The topic's name.

        Raises
        ------
        ~github.errors.NotFound
            A topic with the given name does not exist.

        Returns
        -------
        :class:`~github.Topic`
            A GitHub topic.
        """

        data = await self.http.fetch_topic(name)
        return Topic.from_data(data, self.http)

    async def fetch_user(self, login):
        """
        |coro|

        Fetches a GitHub user from its login.

        Parameters
        ----------
        login: :class:`str`
            The user's login.

        Raises
        ------
        ~github.errors.NotFound
            A user with the given login does not exist.

        Returns
        -------
        :class:`~github.User`
            A GitHub user.
        """

        data = await self.http.fetch_user(login)
        return User.from_data(data, self.http)
    