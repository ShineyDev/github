from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self, cast

    from github.core.http import HTTPClient
    from github.utility.types import T_json_key, T_json_value, DateTime

import github
from github.core.errors import ClientObjectMissingFieldError
from github.interfaces import Type
from github.utility import MISSING


if TYPE_CHECKING:
    from github.interfaces.type import TypeData


    class AnnouncementData(TypeData):
        announcement: str
        announcementCreatedAt: str
        announcementExpiresAt: str | None
        announcementUserDismissible: bool
        id: str


class Announcement(Type):
    """
    Represents an announcement banner on an Enterprise or Organization.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: AnnouncementData
    _http: HTTPClient

    _graphql_fields: dict[str, str] = {
        "text": "announcement",
        "created_at": "announcementCreatedAt",
        "expires_at": "announcementExpiresAt",
        "can_viewer_dismiss": "announcementUserDismissible",
        "id": "id",
    }

    _graphql_type = "Organization"  # NOTE: this is a lie.

    @property
    def can_viewer_dismiss(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can dismiss the announcement.

        :type: :class:`bool`
        """

        return self._data["announcementUserDismissible"]

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the announcement was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["announcementCreatedAt"])

    @property
    def expires_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the announcement will expire.

        :type: Optional[:class:`~datetime.datetime`]
        """

        expires_at = self._data["announcementExpiresAt"]

        if expires_at is None:
            return None

        return github.utility.iso_to_datetime(expires_at)

    @property
    def text(
        self: Self,
        /,
    ) -> str:
        """
        The text of the announcement.

        :type: :class:`str`
        """

        return self._data["announcement"]

    async def _fetch_field(
        self: Self,
        field: T_json_key,
        /,
        *,
        save: bool = MISSING,
    ) -> T_json_value:
        save = save if save is not MISSING else True

        try:
            id = self._data["id"]
        except KeyError:
            raise ClientObjectMissingFieldError from None

        data = await self._http.fetch_query_node(self.__class__, id, fields=(field,))

        value = data[field]

        if save:
            self._data[field] = value

        return value

    async def fetch_can_viewer_dismiss(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches whether the authenticated user can dismiss the
        announcement.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("announcementUserDismissable")  # type: ignore

    async def fetch_created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the announcement was
        created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        created_at = await self._fetch_field("announcementCreatedAt")

        if TYPE_CHECKING:
            created_at = cast(str, created_at)

        return github.utility.iso_to_datetime(created_at)

    async def fetch_expires_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the announcement will
        expire.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`~datetime.datetime`]
        """

        expires_at = await self._fetch_field("announcementExpiresAt")

        if expires_at is None:
            return None

        if TYPE_CHECKING:
            expires_at = cast(str, expires_at)

        return github.utility.iso_to_datetime(expires_at)

    async def fetch_text(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the text of the announcement.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("announcement")  # type: ignore


__all__: list[str] = [
    "Announcement",
]
