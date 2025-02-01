from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.core.http import HTTPClient
    from github.utility.types import DateTime

import github
from github.interfaces import Node, Resource, Starrable, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.interfaces.node import NodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.starrable import StarrableData
    from github.interfaces.type import TypeData
    from github.organization.organization import OrganizationData
    from github.user.user import UserData


    class GistData(NodeData, ResourceData, StarrableData, TypeData):
        __typename: Literal["Gist"]

        # comments  # TODO
        createdAt: str
        description: str | None
        # files  # TODO
        forks: ConnectionData[GistData]
        isFork: bool
        isPublic: bool
        name: str
        owner: OrganizationData | UserData
        pushedAt: str | None
        updatedAt: str


class Gist(Node, Resource, Starrable, Type):
    """
    Represents a GitHub Gist.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: GistData

    @staticmethod
    def _patch_data(
        data: GistData,
        /,
    ) -> GistData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: GistData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "created_at": "createdAt",
        "description": "description",
        "is_fork": "isFork",
        "is_public": "isPublic",
        "name": "name",
        "pushed_at": "pushedAt",
        "updated_at": "updatedAt",
    }

    _node_prefix = "G"

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the gist was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def description(
        self,
        /,
    ) -> str | None:
        """
        The description of the gist.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def is_fork(
        self,
        /,
    ) -> bool:
        """
        Whether the gist is a fork of another.

        :type: :class:`bool`
        """

        return self._data["isFork"]

    @property
    def is_public(
        self,
        /,
    ) -> bool:
        """
        Whether the gist is public.

        :type: :class:`bool`
        """

        return self._data["isPublic"]

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The name of the gist.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def pushed_at(
        self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the gist was last pushed, if ever.

        :type: :class:`~datetime.datetime` | None
        """

        pushed_at = self._data["pushedAt"]

        if pushed_at is None:
            return None

        return github.utility.iso_to_datetime(pushed_at)

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the gist was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the gist was created.


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

    async def fetch_description(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the description of the gist.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_is_fork(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the gist is a fork of another.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isFork")  # type: ignore

    async def fetch_is_public(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the gist is public.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isPublic")  # type: ignore

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the gist.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_pushed_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the gist was last pushed, if
        ever.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        pushed_at = await self._fetch_field("pushedAt")

        if pushed_at is None:
            return None

        if TYPE_CHECKING:
            pushed_at = cast(str, pushed_at)

        return github.utility.iso_to_datetime(pushed_at)

    async def fetch_updated_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the gist was last updated.


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
    "Gist",
]
