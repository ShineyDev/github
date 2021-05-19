import graphql

from github.http import HTTPClient


class Client(graphql.client.Client):
    """
    The base class for interaction with the API.

    Parameters
    ----------
    token: :class:`str`
        A |PAT_link|_.
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

    request = graphql.client.Client.request
    request.__doc__ = """
        |coro|

        Sends a request to GitHub's GraphQL API.

        Parameters
        ----------
        document: :class:`str`
            A GraphQL document.

            .. tip::
                If you haven't already, you should |graphql_learn|_.
                You can also read |graphql_guides|_, find documentation
                in |graphql_reference|_, and use |graphql_explorer|_.
        operation: :class:`str`
            The name of the operation from the document to execute.
        **variables
            A mapping of GraphQL variables.

        Examples
        --------

        .. code-block:: python3

            >>> await client.request("{viewer{login}}")
            {'viewer': {'login': 'nat'}}

        .. code-block:: python3

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


__all__ = [
    "Client",
]
