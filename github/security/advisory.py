from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.connection import Connection, VulnerabilityOrder
    from github.core.http import HTTPClient
    from github.security import AdvisoryClassification, AdvisorySeverity, Vulnerability
    from github.utility.types import DateTime

import github
from github.interfaces import Node, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData
    from github.security.advisoryclassification import AdvisoryClassificationData
    from github.security.advisoryseverity import AdvisorySeverityData
    from github.security.vulnerability import VulnerabilityData


    class AdvisoryData(NodeData, TypeData):
        __typename: Literal["SecurityAdvisory"]

        classification: AdvisoryClassificationData
        # cvss  # TODO
        # cvssSeverities  # TODO
        # cwes  # TODO
        databaseId: int
        description: str
        # epss  # TODO
        ghsaId: str
        # identifiers  # TODO
        notificationsPermalink: str | None
        origin: str
        permalink: str | None
        publishedAt: str
        # references  # TODO
        severity: AdvisorySeverityData
        summary: str
        updatedAt: str
        vulnerabilities: ConnectionData[VulnerabilityData]
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
        cls,
        data: AdvisoryData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "classification": "classification",
        "database_id": "databaseId",
        "description": "description",
        # "": "ghsaId",  # TODO: name
        # "": "notificationsPermalink",  # TODO: name
        # "": "permalink",  # TODO: name
        "published_at": "publishedAt",
        "severity": "severity",
        "title": "summary",
        "updated_at": "updatedAt",
        "withdrawn_at": "withdrawnAt",
    }

    _graphql_type = "SecurityAdvisory"

    _node_prefix = "GSA"

    @property
    def classification(
        self,
        /,
    ) -> AdvisoryClassification:
        """
        The classification of the advisory.

        :type: :class:`~github.AdvisoryClassification`
        """

        return github.AdvisoryClassification(self._data["classification"])

    @property
    def database_id(
        self,
        /,
    ) -> int:
        """
        The database ID of the advisory.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def description(
        self,
        /,
    ) -> str:
        """
        The description of the advisory.

        :type: :class:`str`
        """

        return self._data["description"]

    @property
    def published_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the advisory was published.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["publishedAt"])

    @property
    def severity(
        self,
        /,
    ) -> AdvisorySeverity:
        """
        The severity of the advisory.

        :type: :class:`~github.AdvisorySeverity`
        """

        return github.AdvisorySeverity(self._data["severity"])

    @property
    def title(
        self,
        /,
    ) -> str:
        """
        The title of the advisory.

        :type: :class:`str`
        """

        return self._data["summary"]

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the advisory was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    @property
    def withdrawn_at(
        self,
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

    async def fetch_classification(
        self,
        /,
    ) -> AdvisoryClassification:
        """
        |coro|

        Fetches the classification of the advisory.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.AdvisoryClassification`
        """

        return github.AdvisoryClassification(await self._fetch_field("classification"))

    async def fetch_database_id(
        self,
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
        self,
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
        self,
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

    async def fetch_severity(
        self,
        /,
    ) -> AdvisorySeverity:
        """
        |coro|

        Fetches the severity of the advisory.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.AdvisorySeverity`
        """

        return github.AdvisorySeverity(await self._fetch_field("severity"))

    async def fetch_title(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the title of the advisory.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("summary")  # type: ignore

    async def fetch_updated_at(
        self,
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
        self,
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

    def fetch_vulnerabilities(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order: VulnerabilityOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Vulnerability]:
        """
        |aiter|

        Fetches individual vulnerabilities from the advisory.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order: :class:`~github.VulnerabilityOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection` of :class:`~github.Vulnerability`
        """

        return github.Connection(
            self._http.collect_advisory_vulnerabilities,
            self.id,
            order.value if order is not MISSING else None,
            data_map=lambda d: github.Vulnerability._from_data(d),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )


__all__ = [
    "Advisory",
]
