from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.connection import Connection, DiscussionOrder
    from github.core.http import HTTPClient
    from github.repository import Discussion
    from github.utility.types import DateTime

import github
from github.interfaces import Node, RepositoryNode, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.type import TypeData


    class DiscussionCategoryData(NodeData, RepositoryNodeData, TypeData):
        __typename: Literal["DiscussionCategory"]

        createdAt: str
        description: str | None
        emoji: str
        emojiHTML: str
        isAnswerable: bool
        name: str
        slug: str
        updatedAt: str


class DiscussionCategory(Node, RepositoryNode, Type):
    """
    Represents a discussion category.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: DiscussionCategoryData

    @staticmethod
    def _patch_data(
        data: DiscussionCategoryData,
        /,
    ) -> DiscussionCategoryData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: DiscussionCategoryData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "created_at": "createdAt",
        "description": "description",
        "emoji": "emoji",
        "emoji_html": "emojiHTML",
        "is_answerable": "isAnswerable",
        "name": "name",
        "__repository_id": "repository{id}",
        "slug": "slug",
        "updated_at": "updatedAt",
    }

    _node_prefix = "DIC"

    _repr_fields = [
        "name",
    ]

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the discussion category was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def description(
        self,
        /,
    ) -> str | None:
        """
        The description of the discussion category.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def emoji(
        self,
        /,
    ) -> str:
        """
        The emoji of the discussion category.

        :type: :class:`str`
        """

        return self._data["emoji"]

    @property
    def emoji_html(
        self,
        /,
    ) -> str:
        """
        The emoji of the discussion category as HTML.

        :type: :class:`str`
        """

        return self._data["emojiHTML"]

    @property
    def is_answerable(
        self,
        /,
    ) -> bool:
        """
        Whether the discussion category contains answerable
        discussions.

        :type: :class:`bool`
        """

        return self._data["isAnswerable"]

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The name of the discussion category.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def slug(
        self,
        /,
    ) -> str:
        """
        The slug of the discussion category.

        :type: :class:`str`
        """

        return self._data["slug"]

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the discussion category was last
        updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the discussion category was
        created.


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

        Fetches the description of the discussion category.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_emoji(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the emoji of the discussion category.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("emoji")  # type: ignore

    async def fetch_emoji_html(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the emoji of the discussion category as HTML.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("emojiHTML")  # type: ignore

    async def fetch_is_answerable(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the discussion category contains answerable
        discussions.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isAnswerable")  # type: ignore

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the discussion category.


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

        Fetches the slug of the discussion category.


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
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the discussion category was
        last updated.


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

    def fetch_discussions(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: DiscussionOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Discussion]:
        """
        |aiter|

        Fetches discussions in the discussion category.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.DiscussionOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Discussion`]
        """

        return github.Repository.fetch_discussions(
            github.Dummy(id=self._data["repository"]["id"]),
            category=self,
            cursor=cursor,
            limit=limit,
            order_by=order_by,
            reverse=reverse,
            **kwargs,
        )


__all__ = [
    "DiscussionCategory",
]
