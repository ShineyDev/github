from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypedDict


    class UpdatableData(TypedDict):
        viewerCanUpdate: bool


class Updatable:
    """
    Represents an object that can be updated.
    """

    __slots__ = ()

    _data: UpdatableData

    _graphql_fields = {
        "viewer_can_update": "viewerCanUpdate",
    }

    @property
    def viewer_can_update(
        self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can update to the updatable.

        :type: :class:`bool`
        """

        return self._data["viewerCanUpdate"]

    async def fetch_viewer_can_update(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can update to the
        updatable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanUpdate")  # type: ignore


__all__ = [
    "Updatable",
]
