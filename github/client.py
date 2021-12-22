import graphql

from github.http import HTTPClient
from github.content import CodeOfConduct, License
from github.metadata import Metadata, RateLimit
from github.repository import Topic


class Client(graphql.client.Client):
    """
    The base class for interaction with the API.

    Parameters
    ----------
    token: :class:`str`
        A |PAT|.
    session: :class:`aiohttp.ClientSession`
        A client session.
    user_agent: :class:`str`
        A user agent. Defaults to ``ShineyDev/github@VERSION:UUID``.

        .. note::

            We request that you use your GitHub username or the name of
            your application for the User-Agent header value. This
            allows us to contact you should there be a problem.
    """

    __slots__ = ()

    def __init__(self, token, *, session, user_agent=None):
        self._http = HTTPClient(token, session, user_agent)

    async def request(self, document, operation=None, **variables):
        """
        |coro|

        Sends a request to GitHub's GraphQL API.

        Parameters
        ----------
        document: :class:`str`
            A GraphQL document.

            .. tip::
                If you haven't already, you should |graphql_learn|.
                You can also read |graphql_guides|, find documentation
                in |graphql_reference|, and use |graphql_explorer|.
        operation: :class:`str`
            The name of the operation from the document to execute.
        **variables
            A mapping of GraphQL variables.

        Examples
        --------

        .. code:: python

            >>> await client.request("{viewer{login}}")
            {'viewer': {'login': 'nat'}}

        .. code:: python

            >>> await client.request("query($login:String!){user(login:$login){name}}", login="nat")
            {'user': {'name': 'Nat Friedman'}}

        Raises
        ------
        ~github.errors.ClientResponseHTTPError
            Arbitrary HTTP error.
        ~github.errors.ClientResponseGraphQLError
            Arbitrary GraphQL error.


        :rtype: :class:`dict`
        """

        return await super().request(document, operation, **variables)

    async def fetch_all_codes_of_conduct(self, **kwargs):
        """
        |coro|

        Fetches all codes of conduct.

        Raises
        ------
        ~github.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch a code of conduct body.


        :rtype: List[:class:`~github.CodeOfConduct`]
        """

        data = await self._http.fetch_query_all_codes_of_conduct(**kwargs)
        return CodeOfConduct(data, self._http)

    async def fetch_all_licenses(self, **kwargs):
        """
        |coro|

        Fetches all licenses.

        Raises
        ------
        ~github.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch a license body.


        :rtype: List[:class:`~github.License`]
        """

        data = await self._http.fetch_query_all_licenses(**kwargs)
        return License(data, self._http)

    async def fetch_code_of_conduct(self, key, **kwargs):
        """
        |coro|

        Fetches a code of conduct by its key.

        Parameters
        ----------
        key: :class:`str`
            See :attr:`CodeOfConduct.key`.

        Raises
        ------
        ~github.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch the code of conduct body.
        ~github.errors.ClientResponseGraphQLNotFoundError
            A code of conduct with the provided key does not exist.


        :rtype: :class:`~github.CodeOfConduct`
        """

        data = await self._http.fetch_query_code_of_conduct(key, **kwargs)
        return CodeOfConduct(data, self._http)

    async def fetch_license(self, key, **kwargs):
        """
        |coro|

        Fetches a license by its key.

        Parameters
        ----------
        key: :class:`str`
            See :attr:`License.key`.

        Raises
        ------
        ~github.errors.ClientResponseGraphQLInternalError
            The GraphQL service failed to fetch the license body.
        ~github.errors.ClientResponseGraphQLNotFoundError
            A license with the provided key does not exist.


        :rtype: :class:`~github.License`
        """

        data = await self._http.fetch_query_license(key, **kwargs)
        return License(data, self._http)

    async def fetch_metadata(self, **kwargs):
        """
        |coro|

        Fetches instance metadata.

        :rtype: :class:`~github.Metadata`
        """

        data = await self._http.fetch_query_metadata(**kwargs)
        return Metadata(data)

    async def fetch_rate_limit(self, **kwargs):
        """
        |coro|

        Fetches instance rate limit data.

        :rtype: :class:`~github.RateLimit`
        """

        data = await self._http.fetch_query_rate_limit(**kwargs)
        return RateLimit(data)

    async def fetch_topic(self, name, **kwargs):
        """
        |coro|

        Fetches a topic by its name.

        Parameters
        ----------
        name: :class:`str`
            See :attr:`Topic.name <github.Topic.name>`.

        Raises
        ------
        ~github.errors.ClientResponseGraphQLNotFoundError
            A topic with the provided name does not exist.


        :rtype: :class:`~github.Topic`
        """

        data = await self._http.fetch_query_topic(name, **kwargs)
        return Topic(data, self._http)


__all__ = [
    "Client",
]
