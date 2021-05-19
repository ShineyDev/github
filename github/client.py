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

    __slots__ = ("_http",)

    def __init__(self, token, *, session, user_agent=None):
        self._http = HTTPClient(token, session, user_agent)


__all__ = [
    "Client",
]
