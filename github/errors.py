import re

import graphql


class ClientError(graphql.client.ClientError):
    __doc__ = graphql.client.ClientError.__doc__
    __slots__ = ()


class ClientObjectMissingFieldError(AttributeError, ClientError):
    """
    Represents an :exc:`AttributeError` caused by a missing field.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    fields: Tuple[:class:`str`]
        The missing fields.
    """

    __slots__ = ()

    def __init__(self, *fields):
        self.fields = fields

        message = f"missing field{'' if len(fields) == 1 else 's'}{' ' if fields else ''}{', '.join(repr(f) for f in fields)}"

        super().__init__(message)


class ClientResponseError(graphql.client.ClientResponseError, ClientError):
    __doc__ = graphql.client.ClientResponseError.__doc__
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


class ClientResponseGraphQLInsufficientScopesError(ClientResponseGraphQLError):
    """
    Represents a GraphQL ``"INSUFFICIENT_SCOPES"`` response.

    Attributes
    ----------
    message: :class:`str`
        The error message.
    response: :class:`aiohttp.ClientResponse`
        The client response.
    data: :class:`dict`
        The response data.
    granted_scopes: List[:class:`str`]
        The granted scopes.
    required_scopes: List[:class:`str`]
        The required scopes.
    """

    __slots__ = ()

    def __init__(self, message, response, data):
        super().__init__(message, response, data)

        oauth_scopes = response.headers.get("X-OAuth-Scopes")

        if oauth_scopes:
            self.granted_scopes = oauth_scopes.split(",")
        else:
            self.granted_scopes = list()

        match = re.search(r"requires.+?: ?\[(.+?)\]", message)
        if match:
            required_scopes = match.group(1).replace("'", "").replace(" ", "")

            if required_scopes:
                self.required_scopes = required_scopes.split(",")
            else:
                self.required_scopes = list()
        else:
            self.required_scopes = list()


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


class ClientResponseGraphQLMaximumNodeLimitExceededError(ClientResponseGraphQLError):
    """
    Represents a GraphQL ``"MAX_NODE_LIMIT_EXCEEDED"`` response.

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


_response_error_map = {
    "FORBIDDEN": ClientResponseGraphQLForbiddenError,
    "INSUFFICIENT_SCOPES": ClientResponseGraphQLInsufficientScopesError,
    "INTERNAL": ClientResponseGraphQLInternalError,
    "MAX_NODE_LIMIT_EXCEEDED": ClientResponseGraphQLMaximumNodeLimitExceededError,
    "NOT_FOUND": ClientResponseGraphQLNotFoundError,
    "UNPROCESSABLE": ClientResponseGraphQLUnprocessableError,
    401: ClientResponseHTTPUnauthorizedError,
}


class ClientDeprecationWarning(graphql.client.ClientDeprecationWarning):
    __doc__ = graphql.client.ClientDeprecationWarning.__doc__
    __slots__ = ()


class ServerDeprecationWarning(graphql.client.ServerDeprecationWarning):
    __doc__ = graphql.client.ServerDeprecationWarning.__doc__
    __slots__ = ()


__all__ = [
    "ClientError",
    "ClientObjectMissingFieldError",
    "ClientResponseError",
    "ClientResponseGraphQLError",
    "ClientResponseGraphQLForbiddenError",
    "ClientResponseGraphQLInsufficientScopesError",
    "ClientResponseGraphQLInternalError",
    "ClientResponseGraphQLMaximumNodeLimitExceededError",
    "ClientResponseGraphQLNotFoundError",
    "ClientResponseGraphQLUnprocessableError",
    "ClientResponseHTTPError",
    "ClientResponseHTTPUnauthorizedError",
    "ClientDeprecationWarning",
    "ServerDeprecationWarning",
]
