class GitHubError(Exception):
    """
    The base exception class for the library.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    """

    __slots__ = ("message",)

    def __init__(self, message):
        self.message = message

        super().__init__(message)

    def __repr__(self):
        r = list()
        for name in self.__class__.__slots__:
            value = getattr(self, name)
            r.append(f"{name}={value}")

        s = " ".join(r)
        return f"<{self.__class__.__name__} {s}>"


class HTTPError(GitHubError):
    """
    Represents an error in a HTTP response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: Optional[:class:`dict`]
        The response data.
    """

    __slots__ = ("message", "response", "data")

    def __init__(self, message, response, data):
        self.response = response
        self.data = data

        super().__init__(f"{response.status}: {message}")


class HTTPUnauthorizedError(HTTPError):
    """
    Represents a HTTP 401 response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: Optional[:class:`dict`]
        The response data.
    """

    __slots__ = ("message", "response", "data")


class GraphQLError(HTTPError):
    """
    Represents an error in a GraphQL response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ("message", "response", "data")


class GraphQLForbiddenError(GraphQLError):
    """
    Represents a GraphQL ``"FORBIDDEN"`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ("message", "response", "data")


class GraphQLInternalError(GraphQLError):
    """
    Represents a GraphQL ``"INTERNAL"`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ("message", "response", "data")


class GraphQLNotFoundError(GraphQLError):
    """
    Represents a GraphQL ``"NOT_FOUND"`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The HTTP response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ("message", "response", "data")


error_exception_map = {
    # HTTP error code
    401: HTTPUnauthorizedError,

    # GraphQL error type
    "FORBIDDEN": GraphQLForbiddenError,
    "INTERNAL": GraphQLInternalError,
    "NOT_FOUND": GraphQLNotFoundError,
}


__all__ = [
    "GitHubError",
    "HTTPError",
    "HTTPUnauthorizedError",
    "GraphQLError",
    "GraphQLForbiddenError",
    "GraphQLInternalError",
    "GraphQLNotFoundError",
]
