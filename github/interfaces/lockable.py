from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.interfaces import Node
    from github.repository import LockReason

import github


if TYPE_CHECKING:
    from typing import TypedDict

    from github.repository.lockreason import LockReasonData


    class LockableData(TypedDict):
        activeLockReason: LockReasonData
        locked: bool


class Lockable:
    """
    Represents an object that can be locked.
    """

    __slots__ = ()

    _data: LockableData

    _graphql_fields = {
        "locked_reason": "activeLockReason",
        "is_locked": "locked",
    }

    @property
    def is_locked(
        self,
        /,
    ) -> bool:
        """
        Whether the lockable is locked.

        :type: :class:`bool`
        """

        return self._data["locked"]

    @property
    def locked_reason(
        self,
        /,
    ) -> LockReason | None:
        """
        The reason the lockable is locked, if it is.

        :type: :class:`~github.LockReason` | None
        """

        reason = self._data["activeLockReason"]

        if reason is None:
            return None

        return github.LockReason(reason)

    async def fetch_is_locked(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the lockable is locked.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("locked")  # type: ignore

    async def fetch_locked_reason(
        self,
        /,
    ) -> LockReason | None:
        """
        |coro|

        Fetches the reason the lockable is locked, if it is.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.LockReason` | None
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        reason = await self._fetch_field("activeLockReason")

        if reason is None:
            return None

        return github.LockReason(reason)


__all__ = [
    "Lockable",
]
