from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.content import Announcement
    from github.interfaces import Node

import github


if TYPE_CHECKING:
    from typing import TypedDict


    class OptionalAnnouncementOwnerData(TypedDict, total=False):
        pass


    class AnnouncementOwnerData(OptionalAnnouncementOwnerData):
        pass


class AnnouncementOwner:
    """
    Represents an object that can have an announcement banner.
    """

    __slots__ = ()

    _data: AnnouncementOwnerData

    async def fetch_announcement(
        self: Self,
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


        :rtype: Optional[:class:`~github.content.Announcement`]
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.fetch_announcementowner_announcement(self.id, **kwargs)

        if data is None:
            return None

        return github.Announcement._from_data(data, http=self._http)


__all__: list[str] = [
    "AnnouncementOwner",
]
