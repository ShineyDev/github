from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from aiohttp import ClientSession

    from github.utility.types import T_json_object

import graphql

from github.client.http import HTTPClient
from github.content import CodeOfConduct, License
from github.connection import Metadata, RateLimit
from github.repository import Topic


class Client(graphql.client.Client):
    """
    The base class for interaction with the API.


    Parameters
    ----------

    token: :class:`str`
        A GitHub personal access token.

        .. seealso::

            - `Creating a personal access token <link_token_create_>`_
            - `View your personal access tokens <link_token_view_>`_

    session: :class:`aiohttp.ClientSession`
        A client session.

    user_agent: :class:`str`
        A user agent. Defaults to ``ShineyDev/github@VERSION:UUID``.

        .. note::

            GitHub requests that you use your GitHub username or the
            name of the application for the User-Agent header value to
            allow them to contact you should there be a problem. Using
            ``USERNAME; ShineyDev/github@{version}:{uuid}``, replacing
            USERNAME with your username, would suffice for both.
    """

    __slots__ = ()

    def __init__(
        self: Self,
        /,
        token: str,
        *,
        session: ClientSession,
        user_agent: str | None = None,
    ) -> None:
        self._http: HTTPClient = HTTPClient(token, session, user_agent)

    async def request(
        self: Self,
        document: str,
        operation: str | None = None,
        /,
        **variables: T_json_object,
    ) -> T_json_object:
        """
        |coro|

        Sends a request to GitHub's GraphQL API.


        Parameters
        ----------

        document: :class:`str`
            A GraphQL document.

            .. tip::

                If you haven't already, you should
                `learn GraphQL <link_graphql_learn_>`_. You can also
                read GitHub's `GraphQL guides <link_graphql_guide_>`_,
                find documentation in the
                `GraphQL API reference <link_graphql_reference_>`_, and
                use the `GraphiQL Explorer <link_graphql_explorer_>`_
                to experiment with the API.

        operation: :class:`str`
            The name of the operation from the document to execute.
            Defaults to ``None``, which implies that the document
            contains only one operation.

        **variables
            A mapping of GraphQL variables.


        Raises
        ------

        ~github.client.errors.ClientResponseHTTPError
            Arbitrary HTTP error.

        ~github.client.errors.ClientResponseGraphQLError
            Arbitrary GraphQL error.


        Examples
        --------

        .. code:: python

            >>> await client.request("{viewer{login}}")
            {'viewer': {'login': 'nat'}}

        .. code:: python

            >>> await client.request("query($login:String!){user(login:$login){name}}", login="nat")
            {'user': {'name': 'Nat Friedman'}}


        :rtype: :class:`dict`
        """

        return await super().request(document, operation, **variables)

    async def fetch_all_codes_of_conduct(
        self: Self,
        /,
        **kwargs,  # TODO
    ) -> list[CodeOfConduct]:
        """
        |coro|

        Fetches all codes of conduct.


        Raises
        ------

        ~github.client.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch a code of conduct body.


        :rtype: List[:class:`~github.CodeOfConduct`]
        """

        data = await self._http.fetch_query_all_codes_of_conduct(**kwargs)
        return CodeOfConduct._from_data(data, http=self._http)

    async def fetch_all_licenses(
        self: Self,
        /,
        **kwargs,  # TODO
    ) -> list[License]:
        """
        |coro|

        Fetches all licenses.


        Raises
        ------

        ~github.client.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch a license body.


        :rtype: List[:class:`~github.License`]
        """

        data = await self._http.fetch_query_all_licenses(**kwargs)
        return License._from_data(data, http=self._http)

    async def fetch_code_of_conduct(
        self: Self,
        key: str,
        /,
        **kwargs,  # TODO
    ) -> CodeOfConduct:
        """
        |coro|

        Fetches a code of conduct by its key.


        Parameters
        ----------

        key: :class:`str`
            See :attr:`CodeOfConduct.key`.


        Raises
        ------

        ~github.client.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch the code of conduct body.

        ~github.client.errors.ClientResponseGraphQLNotFoundError
            A code of conduct with the provided key does not exist.


        :rtype: :class:`~github.CodeOfConduct`
        """

        data = await self._http.fetch_query_code_of_conduct(key, **kwargs)
        return CodeOfConduct._from_data(data, http=self._http)

    async def fetch_license(
        self: Self,
        key: str,
        /,
        **kwargs,  # TODO
    ) -> License:
        """
        |coro|

        Fetches a license by its key.


        Parameters
        ----------

        key: :class:`str`
            See :attr:`License.key`.


        Raises
        ------

        ~github.client.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch the license body.

        ~github.client.errors.ClientResponseGraphQLNotFoundError
            A license with the provided key does not exist.


        :rtype: :class:`~github.License`
        """

        data = await self._http.fetch_query_license(key, **kwargs)
        return License._from_data(data, http=self._http)

    async def fetch_metadata(
        self: Self,
        /,
        **kwargs,  # TODO
    ) -> Metadata:
        """
        |coro|

        Fetches instance metadata.

        :rtype: :class:`~github.Metadata`
        """

        data = await self._http.fetch_query_metadata(**kwargs)
        return Metadata._from_data(data)

    async def fetch_rate_limit(
        self: Self,
        /,
        **kwargs,  # TODO
    ) -> RateLimit:
        """
        |coro|

        Fetches instance rate limit data.

        :rtype: :class:`~github.RateLimit`
        """

        data = await self._http.fetch_query_rate_limit(**kwargs)
        return RateLimit._from_data(data)

    async def fetch_topic(
        self: Self,
        name: str,
        /,
        **kwargs,  # TODO
    ) -> Topic:
        """
        |coro|

        Fetches a topic by its name.


        Parameters
        ----------

        name: :class:`str`
            See :attr:`Topic.name <github.Topic.name>`.


        Raises
        ------

        ~github.client.errors.ClientResponseGraphQLNotFoundError
            A topic with the provided name does not exist.


        :rtype: :class:`~github.Topic`
        """

        data = await self._http.fetch_query_topic(name, **kwargs)
        return Topic._from_data(data, http=self._http)


__all__: list[str] = [
    "Client",
]
