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
    Represents an object that can own a Package.

    ..                                  :class:`~github.Package`
    """

    __slots__ = ()

    _data: PackageOwnerData

    async def fetch_packages(
        self: Self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches packages from the package owner.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Package]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Package`]
        """

        raise NotImplementedError  # TODO: PackageOwner.packages


__all__: list[str] = [
    "PackageOwner",
]
