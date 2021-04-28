from github.http import HTTPClient


class Client:
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

    __slots__ = ("http",)

    def __init__(self, token, *, session, user_agent=None):
        self.http = HTTPClient(token, session, user_agent)

    async def request(self, query, **kwargs):
        """
        |coro|

        Sends a request to GitHub's GraphQL API.

        Parameters
        ----------
        query: :class:`str`
            A GraphQL query.

            .. tip::

                If you haven't already, you should
                |GRAPHQL_LEARN_link|_. You can also read
                |GRAPHQL_GUIDE_link|_, find documentation in
                |GRAPHQL_REFERENCE_link|_, and use
                |GRAPHQL_EXPLORER_link|_.
        **kwargs
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
        ~github.errors.HTTPError
            Arbitrary HTTP error.


        :rtype: :class:`dict`
        """

        return await self.http.request(query, kwargs)


__all__ = [
    "Client",
]