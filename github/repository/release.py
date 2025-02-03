from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.core.http import HTTPClient
    from github.utility.types import DateTime

import github
from github.interfaces import Node, Reactable, RepositoryNode, Resource, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.git.commit import CommitData
    from github.git.tag import TagData
    from github.interfaces.node import NodeData
    from github.interfaces.reactable import ReactableData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.type import TypeData
    from github.user.user import UserData


    class ReleaseData(NodeData, ReactableData, RepositoryNodeData, ResourceData, TypeData):
        __typename: Literal["Release"]

        author: UserData
        createdAt: str
        databaseId: int
        description: str | None
        descriptionHTML: str | None
        isDraft: bool
        isLatest: bool
        isPrerelease: bool
        mentions: ConnectionData[UserData]
        name: str
        publishedAt: str | None
        releaseAssets: ConnectionData[object]  # TODO
        shortDescriptionHTML: str | None
        tag: TagData | None
        tagCommit: CommitData | None
        tagName: str
        updatedAt: str


class Release(Node, Reactable, RepositoryNode, Resource, Type):
    """
    Represents a release.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: ReleaseData

    @staticmethod
    def _patch_data(
        data: ReleaseData,
        /,
    ) -> ReleaseData:
        if data.get("description", False) == "":
            data["description"] = None

        if data.get("descriptionHTML", False) == "<div></div>":
            data["descriptionHTML"] = None

        if data.get("shortDescriptionHTML", False) == "":
            data["shortDescriptionHTML"] = None

        return data

    @classmethod
    def _from_data(
        cls,
        data: ReleaseData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "created_at": "createdAt",
        "database_id": "databaseId",
        "body": "description",
        "body_html": "descriptionHTML",
        "is_draft": "isDraft",
        "is_latest": "isLatest",
        "is_production": "isPrerelease",
        "title": "name",
        "published_at": "publishedAt",
        # "": "shortDescriptionHTML",  # TODO: name
        # "": "tagName",  # TODO: name
        "updated_at": "updatedAt",
    }

    _node_prefix = "RE"

    _repr_fields = [
        "name",
    ]

    @property
    def body(
        self,
        /,
    ) -> str | None:
        """
        The body of the release.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def body_html(
        self,
        /,
    ) -> str | None:
        """
        The body of the release as HTML.

        :type: :class:`str` | None
        """

        return self._data["descriptionHTML"]

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the release was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self,
        /,
    ) -> int:
        """
        The database ID of the release.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def is_draft(
        self,
        /,
    ) -> bool:
        """
        Whether the release is a draft.

        :type: :class:`bool`
        """

        return self._data["isDraft"]

    @property
    def is_latest(
        self,
        /,
    ) -> bool:
        """
        Whether the release is the latest.

        :type: :class:`bool`
        """

        return self._data["isLatest"]

    @property
    def is_production(
        self,
        /,
    ) -> bool:
        """
        Whether the release is ready for production.

        :type: :class:`bool`
        """

        return not self._data["isPrerelease"]

    @property
    def published_at(
        self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the release was published, if ever.

        :type: :class:`~datetime.datetime` | None
        """

        published_at = self._data["publishedAt"]

        if published_at is None:
            return None

        return github.utility.iso_to_datetime(published_at)

    @property
    def title(
        self,
        /,
    ) -> str:
        """
        The title of the release.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the release was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_body(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the release.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_body_html(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the release as HTML.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("descriptionHTML")  # type: ignore

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the release was created.


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

        Fetches the database ID of the release.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_is_draft(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the release is a draft.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isDraft")  # type: ignore

    async def fetch_is_latest(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the release is the latest.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isLatest")  # type: ignore

    async def fetch_is_production(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the release is ready for production.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return not await self._fetch_field("isPrerelease")

    async def fetch_published_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the release was published,
        if ever.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        published_at = await self._fetch_field("publishedAt")

        if published_at is None:
            return None

        if TYPE_CHECKING:
            published_at = cast(str, published_at)

        return github.utility.iso_to_datetime(published_at)

    async def fetch_title(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the title of the release.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_updated_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the release was last
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
    "Release",
]
