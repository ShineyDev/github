from __future__ import annotations
from typing import TYPE_CHECKING

import abc


if TYPE_CHECKING:
    from typing import TypedDict


    class DeletableData(TypedDict):
        viewerCanDelete: bool


class Deletable(abc.ABC):
    """
    Represents an object that can be deleted.
    """

    __slots__ = ()

    _data: DeletableData

    _graphql_fields = {
        "viewer_can_delete": "viewerCanDelete",
    }

    @property
    def viewer_can_delete(
        self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can delete the deletable.

        :type: :class:`bool`
        """

        return self._data["viewerCanDelete"]

    async def fetch_viewer_can_delete(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can delete the
        deletable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanDelete")  # type: ignore

    @abc.abstractmethod
    async def delete(
        self,
        /,
    ) -> None:
        """
        |coro|

        Deletes the deletable.
        """

        raise NotImplementedError


__all__ = [
    "Deletable",
]
