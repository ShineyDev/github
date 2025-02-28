from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.connection import Connection, PackageOrder
    from github.interfaces import Node
    from github.repository import Package

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData


    class PackageOwnerData(TypedDict):
        # id: str  # NOTE: on Node
        packages: ConnectionData[Package]


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
        self,
        /,
    ) -> int:
        """
        The number of packages on the package owner.

        :type: :class:`int`
        """

        return self._data["packages"]["totalCount"]

    async def fetch_package_count(
        self,
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

    def fetch_packages(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: PackageOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Package]:
        """
        |aiter|

        Fetches packages on the package owner.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.PackageOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection` of :class:`~github.Package`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return github.Connection(
            self._http.collect_packageowner_packages,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Package._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )


__all__ = [
    "PackageOwner",
]
