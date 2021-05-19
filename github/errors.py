import graphql


class GitHubError(graphql.client.errors.ClientError):
    __doc__ = graphql.client.errors.ClientError.__doc__
    __slots__ = ()


class ClientResponseError(graphql.client.errors.ClientResponseError, GitHubError):
    __doc__ = graphql.client.errors.ClientResponseError.__doc__
    __slots__ = ()


class ClientResponseHTTPError(graphql.client.errors.ClientResponseHTTPError, ClientResponseError):
    __doc__ = graphql.client.errors.ClientResponseHTTPError.__doc__
    __slots__ = ()


class ClientResponseHTTPUnauthorizedError(ClientResponseHTTPError):
    """
    Represents an HTTP 401 response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    data: Optional[:class:`dict`]
        The response data.
    """

    __slots__ = ()


class ClientResponseGraphQLError(graphql.client.errors.ClientResponseGraphQLError, ClientResponseError):
    __doc__ = graphql.client.errors.ClientResponseGraphQLError.__doc__
    __slots__ = ()


class ClientResponseGraphQLForbiddenError(ClientResponseGraphQLError):
    """
    Represents a GraphQL ``"FORBIDDEN"`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ()


class ClientResponseGraphQLInternalError(ClientResponseGraphQLError):
    """
    Represents a GraphQL ``"INTERNAL"`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ()


class ClientResponseGraphQLNotFoundError(ClientResponseGraphQLError):
    """
    Represents a GraphQL ``"NOT_FOUND"`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    data: :class:`dict`
        The response data.
    """

    __slots__ = ()


_response_error_map = {
    401: ClientResponseHTTPUnauthorizedError,
    "FORBIDDEN": ClientResponseGraphQLForbiddenError,
    "INTERNAL": ClientResponseGraphQLInternalError,
    "NOT_FOUND": ClientResponseGraphQLNotFoundError,
}


__all__ = [
    "GitHubError",
    "ClientResponseError",
    "ClientResponseHTTPError",
    "ClientResponseHTTPUnauthorizedError",
    "ClientResponseGraphQLError",
    "ClientResponseGraphQLForbiddenError",
    "ClientResponseGraphQLInternalError",
    "ClientResponseGraphQLNotFoundError",
]
