from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

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

    _graphql_fields: dict[str, str] = {
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


__all__ = [
    "Closable",
]
