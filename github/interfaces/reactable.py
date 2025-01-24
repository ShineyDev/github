from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData


    class ReactableData(TypedDict):
        # databaseId  # TODO: elsewhere
        # id  # NOTE: on Node
        # reactionGroups  # TODO
        reactions: ConnectionData[object]  # TODO
        viewerCanReact: bool


class Reactable:
    """
    Represents an object that can be reacted upon.
    """

    __slots__ = ()

    _data: ReactableData

    _graphql_fields = {
        "viewer_can_react": "viewerCanReact",
    }

    @property
    def viewer_can_react(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can react to the reactable.

        :type: :class:`bool`
        """

        return self._data["viewerCanReact"]

    async def fetch_viewer_can_react(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can react to the
        reactable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanReact")  # type: ignore


__all__ = [
    "Reactable",
]
