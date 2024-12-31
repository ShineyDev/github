from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData
    from github.repository.label import LabelData


    class LabelableData(TypedDict):
        labels: ConnectionData[LabelData]
        viewerCanLabel: bool


class Labelable:
    """
    Represents an object that can have :class:`labels <github.Label>`
    applied to it.
    """

    __slots__ = ()

    _data: LabelableData

    _graphql_fields: dict[str, str,] = {
        "viewer_can_label": "viewerCanLabel",
    }

    @property
    def viewer_can_label(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can update labels on the
        labelable.

        :type: :class:`bool`
        """

        return self._data["viewerCanLabel"]

    async def fetch_viewer_can_label(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can update labels on the
        labelable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanLabel")  # type: ignore


__all__ = [
    "Labelable",
]
