from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict


    class GitNodeData(TypedDict):
        abbreviatedOid: str
        commitResourcePath: str
        commitUrl: str
        # id  # NOTE: on Node
        oid: str
        # repository  # NOTE: on RepositoryNode


class GitNode:
    """
    Represents a Git object.
    """

    __slots__ = ()

    _data: GitNodeData

    _graphql_fields: dict[str, str] = {
        # "": "abbreviatedOid",  # TODO: name
        # "": "commitResourcePath",  # TODO: name
        # "": "commitUrl",  # TODO: name
        "object_id": "oid",
    }

    @property
    def object_id(
        self: Self,
        /,
    ) -> str:
        """
        The Git object ID.

        :type: :class:`str`
        """

        return self._data["oid"]

    async def fetch_object_id(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the Git object ID.

        :rtype: :class:`str`
        """

        return await self._fetch_field("oid")  # type: ignore


__all__ = [
    "GitNode",
]
