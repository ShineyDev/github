from __future__ import annotations
from typing import TYPE_CHECKING


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


__all__: list[str] = [
    "AnnouncementOwner",
]
