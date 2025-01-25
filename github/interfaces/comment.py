from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.automation import Bot, Mannequin
    from github.interfaces import Node
    from github.user import User
    from github.utility.types import DateTime

import github


if TYPE_CHECKING:
    from typing import TypeVar, TypedDict

    from github.automation.bot import BotData
    from github.automation.mannequin import MannequinData
    from github.connection.connection import ConnectionData
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
        userContentEdits: ConnectionData[object]  # TODO
        viewerDidAuthor: bool


    _CommentData_T_co = TypeVar("_CommentData_T_co", bound=CommentData, covariant=True)


class Comment:
    """
    Represents a comment.
    """

    __slots__ = ()

    _data: CommentData

    @staticmethod
    def _patch_data(
        data: _CommentData_T_co,
        /,
    ) -> _CommentData_T_co:
        if data.get("body", False) == "":
            data["body"] = None

        if data.get("bodyHTML", False) == "":
            data["bodyHTML"] = None

        if data.get("bodyText", False) == "":
            data["bodyText"] = None

        return data

    _graphql_fields = {
        # "": "authorAssociation",  # TODO: name, type
        "body": "body",
        "body_html": "bodyHTML",
        "body_text": "bodyText",
        "created_at": "createdAt",
        "is_email": "createdViaEmail",
        "edit_count": "userContentEdits{totalCount}",
        # "": "includesCreatedEdit",  # TODO: name
        "edited_at": "lastEditedAt",
        "published_at": "publishedAt",
        "updated_at": "updatedAt",
        "viewer_is_author": "viewerDidAuthor",
    }

    @property
    def body(
        self,
        /,
    ) -> str | None:
        """
        The body of the comment.

        :type: :class:`str` | None
        """

        return self._data["body"]

    @property
    def body_html(
        self,
        /,
    ) -> str | None:
        """
        The body of the comment as HTML.

        :type: :class:`str` | None
        """

        return self._data["bodyHTML"]

    @property
    def body_text(
        self,
        /,
    ) -> str | None:
        """
        The body of the comment as text.

        :type: :class:`str` | None
        """

        return self._data["bodyText"]

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the comment was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def edit_count(
        self,
        /,
    ) -> int:
        """
        The number of edits to the comment, not including the created
        edit.

        :type: :class:`int`
        """

        edits = self._data["userContentEdits"]["totalCount"]

        # NOTE: if the comment has not been edited, the edits
        #       connection is empty. if the comment has been edited
        #       once, the edits connection contains both the created
        #       edit and the single edit.

        if edits == 0:
            return 0
        else:
            # TODO: this might require a check here for whether we
            #       should be removing the (1) created edit. ie.
            #       if self._data["includesCreatedEdit"]: e-1; else: e

            return edits - 1

    @property
    def edited_at(
        self,
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
    def is_email(
        self,
        /,
    ) -> bool:
        """
        Whether the comment was created via email.

        :type: :class:`bool`
        """

        return self._data["createdViaEmail"]

    @property
    def published_at(
        self,
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
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the comment was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    @property
    def viewer_is_author(
        self,
        /,
    ) -> bool:
        """
        Whether the authenticated user authored the comment.

        :type: :class:`bool`
        """

        return self._data["viewerDidAuthor"]

    async def fetch_body(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the comment.

        :rtype: :class:`str` | None
        """

        return await self._fetch_field("body")  # type: ignore

    async def fetch_body_html(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the comment as HTML.

        :rtype: :class:`str` | None
        """

        return await self._fetch_field("bodyHTML")  # type: ignore

    async def fetch_body_text(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the body of the comment as text.

        :rtype: :class:`str` | None
        """

        return await self._fetch_field("bodyText")  # type: ignore

    async def fetch_created_at(
        self,
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

    async def fetch_edit_count(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of edits to the comment.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._fetch_field("userContentEdits{totalCount}")

        # NOTE: see ~.edit_count for notes on this logic.

        edits: int = data["userContentEdits"]["totalCount"]  # type: ignore

        if edits == 0:
            return 0
        else:
            return edits - 1

    async def fetch_edited_at(
        self,
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

    async def fetch_is_email(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the comment was created via email.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("createdViaEmail")  # type: ignore

    async def fetch_published_at(
        self,
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
        self,
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
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user authored the comment.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerDidAuthor")  # type: ignore

    async def fetch_author(
        self,
        /,
        **kwargs,  # TODO
    ) -> Bot | Mannequin | User:
        """
        |coro|

        Fetches the author of the comment.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Bot` | :class:`~github.Mannequin` | :class:`~github.User`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.fetch_comment_author(self.id, **kwargs)

        # TODO[type-from-data]

        graphql_type = data["__typename"]

        if graphql_type == "Bot":
            return github.Bot._from_data(data, http=self._http)
        elif graphql_type == "Mannequin":
            return github.Mannequin._from_data(data, http=self._http)
        elif graphql_type == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {graphql_type} for Comment.author")

    async def fetch_editor(
        self,
        /,
        **kwargs,  # TODO
    ) -> Bot | User | None:
        """
        |coro|

        Fetches the last editor of the comment.

        ..
           TODO: note that you probably want edit.author instead


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Bot` | :class:`~github.User` | None
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.fetch_comment_editor(self.id, **kwargs)

        if data is None:
            return None

        # TODO[type-from-data]

        graphql_type = data["__typename"]

        if graphql_type == "Bot":
            return github.Bot._from_data(data, http=self._http)
        elif graphql_type == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {graphql_type} for Comment.author")


__all__ = [
    "Comment",
]
