from typing import Optional

from aiohttp import ClientResponse


class GitHubError(Exception):
    message: str
    data: Optional[dict]
    response: Optional[ClientResponse]

    def __init__(self, message: str, *, data: dict=..., response: Optional[ClientResponse]=...) -> None: ...

class HTTPException(GitHubError):
    pass

class Forbidden(HTTPException):
    pass

class Internal(HTTPException):
    pass

class NotFound(HTTPException):
    pass

class Unauthorized(HTTPException):
    pass
