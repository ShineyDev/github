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


    class ClosableData(TypedDict):
        closed: bool
        closedAt: str | None
        viewerCanClose: bool
        viewerCanReopen: bool


class Closable:
    """
    Represents an object that can be closed.
    """

    __slots__ = ()

    _data: ClosableData

    _graphql_fields = {
        "is_closed": "closed",
        "closed_at": "closedAt",
        "viewer_can_close": "viewerCanClose",
        "viewer_can_reopen": "viewerCanReopen",
    }

    @property
    def closed_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the closable was closed, if any.

        :type: :class:`~datetime.datetime`
        """

        closed_at = self._data["closedAt"]

        if closed_at is None:
            return None

        return github.utility.iso_to_datetime(closed_at)

    @property
    def is_closed(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the closable is closed.

        :type: :class:`bool`
        """

        return self._data["closed"]

    @property
    def viewer_can_close(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can close the closable.

        :type: :class:`bool`
        """

        return self._data["viewerCanClose"]

    @property
    def viewer_can_reopen(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can reopen the closable.

        :type: :class:`bool`
        """

        return self._data["viewerCanReopen"]

    async def fetch_closed_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the closable was closed, if
        any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        closed_at = await self._fetch_field("closedAt")

        if closed_at is None:
            return None

        if TYPE_CHECKING:
            closed_at = cast(str, closed_at)

        return github.utility.iso_to_datetime(closed_at)

    async def fetch_is_closed(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the closable is closed.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("closed")  # type: ignore

    async def fetch_viewer_can_close(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can close the closable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanClose")  # type: ignore

    async def fetch_viewer_can_reopen(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can reopen the closable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanReopen")  # type: ignore


__all__ = [
    "Closable",
]
