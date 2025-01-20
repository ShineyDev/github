from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import Literal, TypedDict


    class LockableData(TypedDict):
        activeLockReason: Literal["OFF_TOPIC", "RESOLVED", "SPAM", "TOO_HEATED"]
        locked: bool


class Lockable:
    """
    Represents an object that can be locked.
    """

    __slots__ = ()

    _data: LockableData

    _graphql_fields = {
        # "": "activeLockReason",  # TODO: name, type
        "is_locked": "locked",
    }

    @property
    def is_locked(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the lockable is locked.

        :type: :class:`bool`
        """

        return self._data["locked"]

    async def fetch_is_locked(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the lockable is locked.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("locked")  # type: ignore


__all__ = [
    "Lockable",
]
