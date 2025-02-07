from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.content import Announcement
    from github.interfaces import Node

import github


if TYPE_CHECKING:
    from typing import TypedDict

    from github.content.announcement import AnnouncementData


    class AnnouncementOwnerData(TypedDict):
        announcementBanner: AnnouncementData | None


class AnnouncementOwner:
    """
    Represents an object that can have an announcement banner.
    """

    __slots__ = ()

    _data: AnnouncementOwnerData

    async def fetch_announcement(
        self,
        /,
        **kwargs,  # TODO
    ) -> Announcement | None:
        """
        |aiter|

        Fetches the announcement from the announcement owner.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Announcement` | None
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.fetch_announcementowner_announcement(self.id, **kwargs)

        if data is None:
            return None

        return github.Announcement._from_data(data)


__all__ = [
    "AnnouncementOwner",
]
