class Starrable:
    """
    Represents an object that can be starred.
    """

    __slots__ = ()

    _graphql_fields = {
        "stargazer_count": "stargazerCount",
        "viewer_has_starred": "viewerHasStarred",
    }

    @property
    def stargazer_count(self):
        """
        The number of stars on the starrable.

        :type: :class:`int`
        """

        return self._get_field("stargazerCount")

    @property
    def viewer_has_starred(self):
        """
        Whether the viewer has starred the starrable.

        :type: :class:`bool`
        """

        return self._get_field("viewerHasStarred")

    async def fetch_stargazer_count(self):
        """
        |coro|

        Fetches the number of stars on the starrable.

        :rtype: :class:`int`
        """

        return await self._fetch_field("stargazerCount")

    async def fetch_viewer_has_starred(self):
        """
        |coro|

        Fetches whether the viewer has starred the starrable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerHasStarred")


__all__ = [
    "Starrable",
]
