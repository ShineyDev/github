from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.interfaces import Node


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

    _graphql_fields = {
        "package_count": "packages{totalCount}",
    }

    @property
    def package_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of packages on the package owner.

        :type: :class:`int`
        """

        return self._data["packages"]["totalCount"]

    async def fetch_package_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of packages on the package owner.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return await self._fetch_field("packages{totalCount}")  # type: ignore


__all__: list[str] = [
    "PackageOwner",
]
