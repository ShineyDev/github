from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.interfaces import Node


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
        "reaction_count": "reactions{totalCount}",
        "viewer_can_react": "viewerCanReact",
    }

    @property
    def reaction_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of reactions on the reactable.

        :type: :class:`int`
        """

        return self._data["reactions"]["totalCount"]

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

    async def fetch_reaction_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of reactions on the reactable.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return await self._fetch_field("reactions{totalCount}")  # type: ignore

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
