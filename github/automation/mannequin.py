from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

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
    from github.user.user import User


    class MannequinData(ActorData, NodeData, ResourceData, TypeData):
        __typename: Literal["Mannequin"]

        claimant: User | None
        createdAt: str
        databaseId: int
        email: str | None
        updatedAt: str


class Mannequin(Actor, Node, Resource, Type):
    """
    Represents a placeholder user.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: MannequinData

    @staticmethod
    def _patch_data(
        data: MannequinData,
        /,
    ) -> MannequinData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: MannequinData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "created_at": "createdAt",
        "database_id": "databaseId",
        # "email": "email",  # TODO: find
        "updated_at": "updatedAt",
    }

    _node_prefix = "M"

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the mannequin was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self,
        /,
    ) -> int:
        """
        The database ID of the mannequin.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the mannequin was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the mannequin was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        created_at = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            created_at = cast(str, created_at)

        return github.utility.iso_to_datetime(created_at)

    async def fetch_database_id(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the mannequin.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_updated_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the mannequin was last
        updated.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        updated_at = await self._fetch_field("updatedAt")

        if TYPE_CHECKING:
            updated_at = cast(str, updated_at)

        return github.utility.iso_to_datetime(updated_at)


__all__ = [
    "Mannequin",
]
