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

    async def fetch_avatar_url(self, *, size=None):
        """
        |coro|

        Fetches a URL to the avatar of the actor.

        Parameters
        ----------
        size: :class:`int`
            The width of the square image in pixels.


        :rtype: :class:`str`
        """

        if size is not None:
            field = f"avatarUrl(size:{size})"
            save = False
        else:
            field = "avatarUrl"
            save = True

        return await self._fetch_field(field, save=save)

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
