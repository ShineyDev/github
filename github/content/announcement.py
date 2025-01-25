from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.utility.types import DateTime

import github
from github.interfaces import Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.type import TypeData


    class AnnouncementData(TypeData):
        __typename: Literal["AnnouncementBanner"]

        createdAt: str
        expiresAt: str | None
        isUserDismissible: bool
        message: str


class Announcement(Type):
    """
    Represents an announcement banner on an Enterprise or Organization.
    """

    __slots__ = ()

    _data: AnnouncementData

    @staticmethod
    def _patch_data(
        data: AnnouncementData,
        /,
    ) -> AnnouncementData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: AnnouncementData,
        /,
    ):
        return cls(cls._patch_data(data))

    _graphql_fields = {
        "created_at": "createdAt",
        "expires_at": "expiresAt",
        "can_viewer_dismiss": "isUserDismissible",
        "message": "message",
    }

    _graphql_type = "AnnouncementBanner"

    @property
    def can_viewer_dismiss(
        self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can dismiss the announcement.

        :type: :class:`bool`
        """

        return self._data["isUserDismissible"]

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the announcement was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def expires_at(
        self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the announcement will expire.

        :type: Optional[:class:`~datetime.datetime`]
        """

        expires_at = self._data["expiresAt"]

        if expires_at is None:
            return None

        return github.utility.iso_to_datetime(expires_at)

    @property
    def message(
        self,
        /,
    ) -> str:
        """
        The message of the announcement.

        :type: :class:`str`
        """

        return self._data["message"]


__all__ = [
    "Announcement",
]
