from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Iterable
    from typing_extensions import Self

    from aiohttp import ClientResponse

    from github.utilities.types import T_json_object

import re

import graphql


class ClientError(graphql.client.ClientError):
    __doc__ = graphql.client.ClientError.__doc__
    __slots__ = ()


class ClientObjectMissingFieldError(ClientError):
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

    def __init__(
        self: Self,
        /,
        *fields: str,
    ) -> None:
        self.fields: Iterable[str] = fields

        message = f"missing field{'' if len(fields) == 1 else 's'}{' ' if fields else ''}{', '.join(repr(f) for f in fields)}"

        super().__init__(message)


class ClientResponseError(graphql.client.ClientResponseError, ClientError):
    __doc__ = graphql.client.ClientResponseError.__doc__
    __slots__ = ()


class ClientResponseGraphQLError(graphql.client.ClientResponseGraphQLError, ClientResponseError):
    __doc__ = graphql.client.ClientResponseGraphQLError.__doc__
    __slots__ = ()


class ClientResponseGraphQLArgumentValueRangeExceededError(ClientResponseGraphQLError):
    """
    Represents a GraphQL ``"ARGUMENT_LIMIT"`` response.


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

    def __init__(
        self: Self,
        /,
        message: str,
        response: ClientResponse,
        data: T_json_object,
    ) -> None:
        super().__init__(message, response, data)

        oauth_scopes = response.headers.get("X-OAuth-Scopes")

        granted_scopes = list()

        if oauth_scopes:
            granted_scopes = oauth_scopes.split(",")

        self.granted_scopes: list[str] = granted_scopes

        required_scopes = list()

        match = re.search(r"requires.+?: ?\[(.+?)\]", message)
        if match:
            matched_scopes = match.group(1).replace("'", "").replace(" ", "")

            if matched_scopes:
                required_scopes = matched_scopes.split(",")

        self.required_scopes: list[str] = required_scopes


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


_response_error_map: dict[int | str, type[ClientError]] = {
    "ARGUMENT_LIMIT": ClientResponseGraphQLArgumentValueRangeExceededError,
    "EXCESSIVE_PAGINATION": ClientResponseGraphQLArgumentValueRangeExceededError,
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


__all__: list[str] = [
    "ClientError",
    "ClientObjectMissingFieldError",
    "ClientResponseError",
    "ClientResponseGraphQLError",
    "ClientResponseGraphQLArgumentValueRangeExceededError",
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
