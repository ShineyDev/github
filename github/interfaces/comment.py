from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.interfaces import Node
    from github.utility.types import DateTime

import github


if TYPE_CHECKING:
    from typing import TypedDict

    from github.automation.bot import BotData
    from github.automation.mannequin import MannequinData
    from github.user.user import UserData


    class CommentData(TypedDict):
        author: BotData | MannequinData | UserData
        authorAssociation: str
        body: str | None
        bodyHTML: str | None
        bodyText: str | None
        createdAt: str
        createdViaEmail: bool
        editor: BotData | UserData | None
        includesCreatedEdit: bool
        lastEditedAt: str | None
        publishedAt: str | None
        updatedAt: str
        # userContentEdits  # TODO
        viewerDidAuthor: bool


class Comment:
    """
    Represents a comment.
    """

    __slots__ = ()

    _data: CommentData

    _graphql_fields: dict[str, str] = {
        # "": "authorAssociation",  # TODO: name, type
        "body": "body",
        "body_html": "bodyHTML",
        "body_text": "bodyText",
        "created_at": "createdAt",
        # "": "createdViaEmail",  # TODO: name
        # "": "includesCreatedEdit",  # TODO: name
        "edited_at": "lastEditedAt",
        "published_at": "publishedAt",
        "updated_at": "updatedAt",
        "viewer_is_author": "viewerDidAuthor",
    }

    @property
    def body(
        self: Self,
        /,
    ) -> str | None:
        """
        The body of the comment.

        :type: :class:`str` | None
        """

        return self._data["body"]

    @property
    def body_html(
        self: Self,
        /,
    ) -> str | None:
        """
        The body of the comment as HTML.

        :type: :class:`str` | None
        """

        return self._data["bodyHTML"]

    @property
    def body_text(
        self: Self,
        /,
    ) -> str | None:
        """
        The body of the comment as text.

        :type: :class:`str` | None
        """

        return self._data["bodyText"]

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the comment was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def edited_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the comment was last edited.

        :type: Optional[:class:`~datetime.datetime`]
        """

        edited_at = self._data["lastEditedAt"]

        if edited_at is None:
            return None

        return github.utility.iso_to_datetime(edited_at)

    @property
    def published_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the comment was published.

        :type: Optional[:class:`~datetime.datetime`]
        """

        published_at = self._data["publishedAt"]

        if published_at is None:
            return None

        return github.utility.iso_to_datetime(published_at)

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the comment was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    @property
    def viewer_is_author(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user authored the comment.

        :type: :class:`bool`
        """

        return self._data["viewerDidAuthor"]

    async def fetch_body(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the comment.

        :rtype: :class:`str` | None
        """

        return await self._fetch_field("body")  # type: ignore

    async def fetch_body_html(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the comment as HTML.

        :rtype: :class:`str` | None
        """

        return await self._fetch_field("bodyHTML")  # type: ignore

    async def fetch_body_text(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the comment as text.

        :rtype: :class:`str` | None
        """

        return await self._fetch_field("bodyText")  # type: ignore

    async def fetch_created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the comment was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        created_at = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            created_at = cast(str, created_at)

        return github.utility.iso_to_datetime(created_at)

    async def fetch_edited_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the comment was last edited.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        edited_at = await self._fetch_field("lastEditedAt")

        if edited_at is None:
            return None

        if TYPE_CHECKING:
            edited_at = cast(str, edited_at)

        return github.utility.iso_to_datetime(edited_at)

    async def fetch_published_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the comment was published.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        published_at = await self._fetch_field("publishedAt")

        if published_at is None:
            return None

        if TYPE_CHECKING:
            published_at = cast(str, published_at)

        return github.utility.iso_to_datetime(published_at)

    async def fetch_updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the comment was last
        updated.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        updated_at = await self._fetch_field("updatedAt")

        if TYPE_CHECKING:
            updated_at = cast(str, updated_at)

        return github.utility.iso_to_datetime(updated_at)

    async def fetch_viewer_is_author(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user authored the comment.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerDidAuthor")  # type: ignore


__all__ = [
    "Comment",
]
