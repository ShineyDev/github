from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.utility.types import DateTime

import github
from github.interfaces import Actor, Node, Resource, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.actor import ActorData
    from github.interfaces.node import NodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.type import TypeData


    class BotData(ActorData, NodeData, ResourceData, TypeData):
        __typename: Literal["Bot"]

        createdAt: str
        databaseId: int
        updatedAt: str


class Bot(Actor, Node, Resource, Type):
    """
    Represents a bot.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: BotData

    @staticmethod
    def _patch_data(
        data: BotData,
        /,
    ) -> BotData:
        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: BotData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _graphql_fields: dict[str, str] = {
        "created_at": "createdAt",
        "database_id": "databaseId",
        "updated_at": "updatedAt",
    }

    _node_prefix: str = "BOT"

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the bot was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the bot.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the bot was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])


__all__ = [
    "Bot",
]
