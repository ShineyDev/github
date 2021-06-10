import graphql


class ClientError(graphql.client.ClientError):
    __doc__ = graphql.client.ClientError.__doc__
    __slots__ = ()


class ClientResponseError(graphql.client.ClientResponseError, ClientError):
    __doc__ = graphql.client.ClientResponseError.__doc__
    __slots__ = ()


class ClientResponseHTTPError(graphql.client.ClientResponseHTTPError, ClientResponseError):
    __doc__ = graphql.client.ClientResponseHTTPError.__doc__
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


class ClientResponseGraphQLError(graphql.client.ClientResponseGraphQLError, ClientResponseError):
    __doc__ = graphql.client.ClientResponseGraphQLError.__doc__
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


class ClientResponseGraphQLUnprocessableError(ClientResponseGraphQLError):
    """
    Represents a GraphQL ``"UNPROCESSABLE"`` response.

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
    "UNPROCESSABLE": ClientResponseGraphQLUnprocessableError,
}


__all__ = [
    "ClientError",
    "ClientResponseError",
    "ClientResponseHTTPError",
    "ClientResponseHTTPUnauthorizedError",
    "ClientResponseGraphQLError",
    "ClientResponseGraphQLForbiddenError",
    "ClientResponseGraphQLInternalError",
    "ClientResponseGraphQLNotFoundError",
    "ClientResponseGraphQLUnprocessableError",
]
