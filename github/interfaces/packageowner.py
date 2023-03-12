from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypedDict

    # TODO: from github.???.package import PackageData
    # TODO: from github.utilities.types import ConnectionData


    class OptionalPackageOwnerData(TypedDict, total=False):
        pass
        # TODO: packages: ConnectionData[PackageData]


    class PackageOwnerData(OptionalPackageOwnerData):
        pass
        # NOTE: id: str (on Node)


class PackageOwner:
    """
    Represents an object that can own a Package.

    ..                                  :class:`~github.Package`
    """

    __slots__ = ()

    _data: PackageOwnerData


__all__: list[str] = [
    "PackageOwner",
]
