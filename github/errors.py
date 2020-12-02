"""
/github/errors.py

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

class GitHubError(Exception):
    """
    The base exception class for github.py.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(message)

class HTTPError(GitHubError):
    """
    Represents an error in a HTTP response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    data: Optional[:class:`dict`]
        The JSON data from the API.
    response: :class:`~aiohttp.ClientResponse`
        The response.
    """

    def __init__(self, message, *, response, data):
        self.message = message
        self.response = response
        self.data = data

        super().__init__(f"{response.status}: {message}")

class HTTPUnauthorized(HTTPError):
    """
    Represents a HTTP 401 response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    data: Optional[:class:`dict`]
        The JSON data from the API.
    response: :class:`~aiohttp.ClientResponse`
        The response.
    """

HTTPUnauthorised = HTTPUnauthorized

class GraphQLError(HTTPError):
    """
    Represents an error in a GraphQL response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    data: :class:`dict`
        The JSON data from the API.
    response: :class:`~aiohttp.ClientResponse`
        The response.
    """

class GraphQLForbidden(GraphQLError):
    """
    Represents a GitHub ``FORBIDDEN`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    data: :class:`dict`
        The JSON data from the API.
    response: :class:`~aiohttp.ClientResponse`
        The response.
    """

class GraphQLInternal(GraphQLError):
    """
    Represents a GitHub ``INTERNAL`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    data: :class:`dict`
        The JSON data from the API.
    response: :class:`~aiohttp.ClientResponse`
        The response.
    """

class GraphQLNotFound(GraphQLError):
    """
    Represents a GitHub ``NOT_FOUND`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    data: :class:`dict`
        The JSON data from the API.
    response: :class:`~aiohttp.ClientResponse`
        The response.
    """
