from typing import NamedTuple

from github.client import Client
from github.errors import GitHubError, HTTPError, HTTPUnauthorizedError, GraphQLError, GraphQLForbiddenError, GraphQLInternalError, GraphQLNotFoundError


class _VersionInfo(NamedTuple):
    prime: int
    major: int
    minor: int
    micro: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
