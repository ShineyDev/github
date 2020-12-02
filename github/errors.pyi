from typing import Optional

from aiohttp import ClientResponse


class GitHubError(Exception):
    message: str

class HTTPError(GitHubError):
    message: str
    data: Optional[dict]
    response: ClientResponse

class HTTPUnauthorized(HTTPError):
    pass

HTTPUnauthorised = HTTPUnauthorized

class GraphQLError(HTTPError):
    message: str
    data: dict
    response: ClientResponse

class GraphQLForbidden(GraphQLError):
    pass

class GraphQLInternal(GraphQLError):
    pass

class GraphQLNotFound(GraphQLError):
    pass
