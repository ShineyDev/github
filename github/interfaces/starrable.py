from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.client.http import HTTPClient
    from github.interfaces import Node


if TYPE_CHECKING:
    from typing import TypedDict

    # TODO: from ??? import UserData
    # TODO: from ??? import ConnectionData


    class OptionalStarrableData(TypedDict, total=False):
        pass
        # TODO: stargazers: ConnectionData[UserData]


    class StarrableData(OptionalStarrableData):
        # NOTE: id: str (on Node)
        stargazerCount: int
        viewerHasStarred: bool


class Starrable:
    """
    Represents an object that can be starred.
    """

    __slots__ = ()

    _data: StarrableData
    _http: HTTPClient

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

        return self._data["stargazerCount"]

    @property
    def viewer_has_starred(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the viewer has starred the starrable.

        :type: :class:`bool`
        """

        return self._data["viewerHasStarred"]

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

    async def star(
        self: Self,
        /,
    ) -> None:
        """
        |coro|

        Stars the starrable.

        Use of this mutation will also update the following fields:

        - :attr:`~.viewer_has_starred`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.mutate_starrable_star(self.id, fields=["viewerHasStarred"])

        self._data["viewerHasStarred"] = data["viewerHasStarred"]

    async def unstar(
        self: Self,
        /,
    ) -> None:
        """
        |coro|

        Unstars the starrable.

        Use of this mutation will also update the following fields:

        - :attr:`~.viewer_has_starred`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.mutate_starrable_unstar(self.id, fields=["viewerHasStarred"])

        self._data["viewerHasStarred"] = data["viewerHasStarred"]


__all__: list[str] = [
    "Starrable",
]
