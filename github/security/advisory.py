from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.utility.types import DateTime

import github
from github.interfaces import Node, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData


    class AdvisoryData(NodeData, TypeData):
        __typename: Literal["SecurityAdvisory"]

        classification: Literal["GENERAL", "MALWARE"]
        # cvss  # TODO
        # cvssSeverities  # TODO
        # cwes  # TODO
        databaseId: int
        description: str
        # epss  # TODO
        ghsaId: str
        # identifiers  # TODO
        notificationsPermalink: str | None
        # origin  # TODO
        permalink: str | None
        publishedAt: str
        # references  # TODO
        severity: Literal["CRITICAL", "HIGH", "LOW", "MODERATE"]
        summary: str
        updatedAt: str
        # vulnerabilities  # TODO
        withdrawnAt: str | None



class Advisory(Node, Type):
    """
    Represents a GitHub Security Advisory (GHSA).


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: AdvisoryData

    @staticmethod
    def _patch_data(
        data: AdvisoryData,
        /,
    ) -> AdvisoryData:
        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: AdvisoryData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _graphql_fields: dict[str, str] = {
        # "classification": "classification",  # TODO: type
        "database_id": "databaseId",
        "description": "description",
        # "": "ghsaId",  # TODO: name
        # "": "notificationsPermalink",  # TODO: name
        # "": "permalink",  # TODO: name
        "published_at": "publishedAt",
        # "severity": "severity",  # TODO: type
        "summary": "summary",
        "updated_at": "updatedAt",
        "withdrawn_at": "withdrawnAt",
    }

    _node_prefix = "GSA"

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the advisory.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def description(
        self: Self,
        /,
    ) -> str:
        """
        The description of the advisory.

        :type: :class:`str`
        """

        return self._data["description"]

    @property
    def published_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the advisory was published.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["publishedAt"])

    @property
    def summary(
        self: Self,
        /,
    ) -> str:
        """
        The summary of the advisory.

        :type: :class:`str`
        """

        return self._data["summary"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the advisory was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    @property
    def withdrawn_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the advisory was withdrawn, if any.

        :type: :class:`~datetime.datetime` | None
        """

        withdrawn_at = self._data["withdrawnAt"]

        if withdrawn_at is None:
            return None

        return github.utility.iso_to_datetime(withdrawn_at)

    async def fetch_database_id(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the advisory.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_description(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the description of the advisory.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_published_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the advisory was published.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        published_at = await self._fetch_field("publishedAt")

        if TYPE_CHECKING:
            published_at = cast(str, published_at)

        return github.utility.iso_to_datetime(published_at)

    async def fetch_summary(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the summary of the advisory.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("summary")  # type: ignore

    async def fetch_updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the advisory was last
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

    async def fetch_withdrawn_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the advisory was withdrawn,
        if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        withdrawn_at = await self._fetch_field("withdrawnAt")

        if withdrawn_at is None:
            return None

        if TYPE_CHECKING:
            withdrawn_at = cast(str, withdrawn_at)

        return github.utility.iso_to_datetime(withdrawn_at)


__all__ = [
    "Advisory",
]
