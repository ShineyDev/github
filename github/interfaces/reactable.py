from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.connection import Connection, ReactionOrder
    from github.content import Reaction, ReactionContent
    from github.interfaces import Node

import github
from github.utility import MISSING


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

    def fetch_reactions(
        self: Self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: ReactionOrder = MISSING,
        reverse: bool = MISSING,
    ) -> Connection[Reaction]:
        """
        |aiter|

        Fetches reactions from the reactable.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.ReactionOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Reaction`]
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return github.Connection(
            self._http.collect_reactable_reactions,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Reaction._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
        )

    async def add_reaction(
        self: Self,
        content: ReactionContent,
        /,
    ) -> Reaction:
        """
        |coro|

        Adds a reaction to the reactable.

        .. note::

            This mutation requires the following token scopes:

            - ``public_repo`` (on a :class:`~github.RepositoryNode`)
            - ``write:discussions`` (on a :class:`~github.TeamDiscussion` or a :class:`~github.TeamDiscussionComment`)


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.reaction_count`


        Parameters
        ----------

        content: :class:`~github.ReactionContent`
            The content of the reaction.


        :rtype: :class:`~github.Reaction`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        reactable_data, reaction_data = await self._http.mutate_reactable_add_reaction(self.id, content.value, reactable_fields=("reactions{totalCount}",))

        if "reactions" not in self._data.keys():
            self._data["reactions"] = dict()  # type: ignore

        self._data["reactions"]["totalCount"] = reactable_data["reactions"]["totalCount"]

        return github.Reaction._from_data(reaction_data, http=self._http)

    async def remove_reaction(
        self: Self,
        content: ReactionContent,
        /,
    ) -> None:
        """
        |coro|

        Removes a reaction from the reactable.

        .. note::

            This mutation requires the following token scopes:

            - ``public_repo`` (on a :class:`~github.RepositoryNode`)
            - ``write:discussions`` (on a :class:`~github.TeamDiscussion` or a :class:`~github.TeamDiscussionComment`)


        .. warning::

            For reasons beyond my comprehension, this mutation will
            raise FORBIDDEN when the reaction you attempt to remove
            does not exist, despite having the required permission.


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.reaction_count`


        Parameters
        ----------

        content: :class:`~github.ReactionContent`
            The content of the reaction.
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        reactable_data = await self._http.mutate_reactable_remove_reaction(self.id, content.value, fields=("reactions{totalCount}",))

        if "reactions" not in self._data.keys():
            self._data["reactions"] = dict()  # type: ignore

        self._data["reactions"]["totalCount"] = reactable_data["reactions"]["totalCount"]


__all__ = [
    "Reactable",
]
