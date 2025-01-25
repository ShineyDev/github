from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData


    class PackageOwnerData(TypedDict):
        # id: str  # NOTE: on Node
        packages: ConnectionData[object]


class PackageOwner:
    """
    Represents an object that can own a :class:`~github.Package`.
    """

    __slots__ = ()

    _data: PackageOwnerData


__all__: list[str] = [
    "PackageOwner",
]
