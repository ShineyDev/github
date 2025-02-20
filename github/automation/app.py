from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.core.http import HTTPClient
    from github.utility.types import DateTime

import github
from github.interfaces import Node, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData


    class AppData(NodeData, TypeData):
        __typename: Literal["App"]

        clientId: str
        createdAt: str
        databaseId: int
        description: str | None
        # ipAllowListEntries  # TODO
        logoBackgroundColor: str
        logoUrl: str
        name: str
        slug: str
        updatedAt: str
        url: str


class App(Node, Type):
    """
    Represents a GitHub App.

    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: AppData

    @staticmethod
    def _patch_data(
        data: AppData,
        /,
    ) -> AppData:
        if data.get("description", False) == "":
            data["description"] = None

        return data

    @classmethod
    def _from_data(
        cls,
        data: AppData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        # "": "clientId",  # TODO: name
        "created_at": "createdAt",
        "database_id": "databaseId",
        "description": "description",
        # "": "logoBackgroundColor",  # TODO: name
        # "": "logoUrl",  # TODO: name
        "name": "name",
        "slug": "slug",
        "updated_at": "updatedAt",
        # "": "url",  # TODO: name
    }

    _node_prefix = "A"

    _repr_fields = [
        "slug"
    ]

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the app was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self,
        /,
    ) -> int:
        """
        The database ID of the app.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def description(
        self,
        /,
    ) -> str | None:
        """
        The description of the app.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The name of the app.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def slug(
        self,
        /,
    ) -> str:
        """
        The slug of the app.

        :type: :class:`str`
        """

        return self._data["slug"]

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the app was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the app was created.


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

        Fetches the database ID of the app.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_description(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the description of the app.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the app.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_slug(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the slug of the app.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("slug")  # type: ignore

    async def fetch_updated_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the app was last updated.


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
    "App",
]
