class Actor:
    """
    Represents an object that can take action.
    """

    __slots__ = ()

    _repr_fields = [
        "login",
    ]

    _graphql_type = "Actor"

    _graphql_fields = [
        "avatarUrl",
        "login",
    ]

    @property
    def avatar_url(self):
        """
        A URL to the avatar of the actor.

        :type: :class:`str`
        """

        return self._get_field("avatarUrl")

    @property
    def login(self):
        """
        The login of the actor.

        :type: :class:`str`
        """

        return self._get_field("login")

    async def fetch_avatar_url(self):
        """
        |coro|

        Fetches a URL to the avatar of the actor.

        :rtype: :class:`str`
        """

        return await self._fetch_field("avatarUrl")

    async def fetch_login(self):
        """
        |coro|

        Fetches the login of the actor.

        :rtype: :class:`str`
        """

        return await self._fetch_field("login")


__all__ = [
    "Actor",
]
