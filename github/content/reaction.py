from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.content import ReactionContent
    from github.core.http import HTTPClient
    from github.user import User
    from github.utility.types import DateTime

import github
from github.interfaces import Node, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.content.reactioncontent import ReactionContentData
    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData
    from github.user.user import UserData


    class ReactionData(NodeData, TypeData):
        __typename: Literal["Reaction"]

        content: ReactionContentData
        createdAt: str
        databaseId: int
        # reactable  # TODO
        user: UserData


class Reaction(Node, Type):
    """
    Represents a reaction.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: ReactionData

    @staticmethod
    def _patch_data(
        data: ReactionData,
        /,
    ) -> ReactionData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: ReactionData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "content": "content",
        "created_at": "createdAt",
        "database_id": "databaseId",
    }

    _node_prefix = "REA"

    @property
    def content(
        self,
        /,
    ) -> ReactionContent:
        """
        The content of the reaction.

        :type: :class:`~github.ReactionContent`
        """

        return github.ReactionContent(self._data["content"])

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the reaction was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self,
        /,
    ) -> int:
        """
        The database ID of the reaction.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    async def fetch_content(
        self,
        /,
    ) -> ReactionContent:
        """
        |coro|

        Fetches the content of the reaction.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.ReactionContent`
        """

        return github.ReactionContent(await self._fetch_field("content"))

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the reaction was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        value = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            value = cast(str, value)

        return github.utility.iso_to_datetime(value)

    async def fetch_database_id(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the reaction.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_author(
        self,
        /,
        **kwargs,
    ) -> User | None:
        """
        |coro|

        Fetches the author of the reaction.

        .. warning::

            This query will yield NULL if the author was not a
            :class:`~github.User`.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.User` | None
        """

        data = await self._http.fetch_reaction_author(self.id, **kwargs)

        if data is None:
            return None

        return github.User._from_data(data, http=self._http)


__all__ = [
    "Reaction",
]
