from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self
    from github.utility.types import DateTime

import github
from github.interfaces import Node, Type


if TYPE_CHECKING:
    from typing import TypedDict

    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData


    class OptionalUserStatusData(TypedDict, total=False):
        pass


    class UserStatusData(OptionalUserStatusData, NodeData, TypeData):
        createdAt: str
        emoji: str | None
        emojiHTML: str | None
        expiresAt: str | None
        indicatesLimitedActivity: bool
        message: str | None
        updatedAt: str


class UserStatus(Node, Type):
    """
    Represents a GitHub user's status.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: UserStatusData

    _repr_fields: list[str] = [
        "message",
        "is_busy",
    ]

    _graphql_fields: dict[str, str] = {
        "created_at": "createdAt",
        "emoji": "emoji",
        "emoji_html": "emojiHTML",
        "expires_at": "expiresAt",
        "is_busy": "indicatesLimitedActivity",
        "message": "message",
        "updated_at": "updatedAt",
    }

    _node_prefix: str = "US"

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the status was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def emoji(
        self: Self,
        /,
    ) -> str | None:
        """
        The emoji of the status.

        :type: Optional[:class:`str`]
        """

        return self._data["emoji"]

    @property
    def emoji_html(
        self: Self,
        /,
    ) -> str | None:
        """
        The emoji of the status as HTML.

        :type: Optional[:class:`str`]
        """

        return self._data["emojiHTML"]

    @property
    def expires_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the status will expire.

        :type: Optional[:class:`~datetime.datetime`]
        """

        expires_at = self._data["expiresAt"]

        if expires_at is None:
            return None

        return github.utility.iso_to_datetime(expires_at)

    @property
    def is_busy(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the status indicates that the user is busy.

        :type: :class:`bool`
        """

        return self._data["indicatesLimitedActivity"]

    @property
    def message(
        self: Self,
        /,
    ) -> str | None:
        """
        The message of the status.

        :type: Optional[:class:`str`]
        """

        return self._data["message"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the status was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the status was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        value = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            value = cast(str, value)

        return github.utility.iso_to_datetime(value)

    async def fetch_emoji(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the emoji of the status.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("emoji")  # type: ignore

    async def fetch_emoji_html(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the emoji of the status as HTML.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("emojiHTML")  # type: ignore

    async def fetch_expires_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the status will expire.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`~datetime.datetime`]
        """

        expires_at = await self._fetch_field("expiresAt")

        if expires_at is None:
            return None

        if TYPE_CHECKING:
            expires_at = cast(str, expires_at)

        return github.utility.iso_to_datetime(expires_at)

    async def fetch_is_busy(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the status indicates that the user is busy.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("indicatesLimitedActivity")  # type: ignore

    async def fetch_message(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the message of the status.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("message")  # type: ignore

    async def fetch_updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the status was last updated.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        value = await self._fetch_field("updatedAt")

        if TYPE_CHECKING:
            value = cast(str, value)

        return github.utility.iso_to_datetime(value)


__all__: list[str] = [
    "UserStatus",
]
