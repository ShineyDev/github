from typing import NamedTuple

from github.client import Client as Client
from github.errors import GitHubError as GitHubError, HTTPError as HTTPError, HTTPUnauthorizedError as HTTPUnauthorizedError, GraphQLError as GraphQLError, GraphQLForbiddenError as GraphQLForbiddenError, GraphQLInternalError as GraphQLInternalError, GraphQLNotFoundError as GraphQLNotFoundError


class _VersionInfo(NamedTuple):
    prime: int
    major: int
    minor: int
    micro: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
