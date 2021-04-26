from typing import Optional

import aiohttp


class GitHubError(Exception):
    message: str


class HTTPError(GitHubError):
    message: str
    response: aiohttp.ClientResponse
    data: Optional[dict]


class HTTPUnauthorizedError(HTTPError):
    message: str
    response: aiohttp.ClientResponse
    data: Optional[dict]


class GraphQLError(HTTPError):
    message: str
    response: aiohttp.ClientResponse
    data: dict


class GraphQLForbiddenError(GraphQLError):
    message: str
    response: aiohttp.ClientResponse
    data: dict


class GraphQLInternalError(GraphQLError):
    message: str
    response: aiohttp.ClientResponse
    data: dict


class GraphQLNotFoundError(GraphQLError):
    message: str
    response: aiohttp.ClientResponse
    data: dict
