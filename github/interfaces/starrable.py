from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict

    # TODO: from ??? import UserData
    # TODO: from ??? import ConnectionData


    class OptionalStarrableData(TypedDict, total=False):
        pass
        # TODO: stargazers: ConnectionData[UserData]


    class StarrableData(OptionalStarrableData):
        stargazerCount: int
        viewerHasStarred: bool


class Starrable:
    """
    Represents an object that can be starred.
    """

    __slots__ = ()

    _data: StarrableData

    _graphql_fields: dict[str, str] = {
        "stargazer_count": "stargazerCount",
        "viewer_has_starred": "viewerHasStarred",
    }

    @property
    def stargazer_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of stars on the starrable.

        :type: :class:`int`
        """

        return self._get_field("stargazerCount")  # type: ignore

    @property
    def viewer_has_starred(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the viewer has starred the starrable.

        :type: :class:`bool`
        """

        return self._get_field("viewerHasStarred")  # type: ignore

    async def fetch_stargazer_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of stars on the starrable.

        :rtype: :class:`int`
        """

        return await self._fetch_field("stargazerCount")  # type: ignore

    async def fetch_viewer_has_starred(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the viewer has starred the starrable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerHasStarred")  # type: ignore


__all__: list[str] = [
    "Starrable",
]
