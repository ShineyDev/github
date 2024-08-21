from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypedDict

    # from github.???.package import PackageData  # TODO: [support-package]
    from github.utility.types import ConnectionData


    class OptionalPackageOwnerData(TypedDict, total=False):
        # packages: ConnectionData[PackageData]  # TODO: [support-package]
        pass


    class PackageOwnerData(OptionalPackageOwnerData):
        # NOTE: id: str (on Node)
        pass


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
