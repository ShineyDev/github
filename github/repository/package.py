from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.core.http import HTTPClient

from github.interfaces import Node, RepositoryNode, Type


if TYPE_CHECKING:
    from typing import Literal, TypedDict

    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.type import TypeData


    class _PackageStatisticsData(TypedDict):
        downloadsTotalCount: int


    class PackageData(NodeData, RepositoryNodeData, TypeData):
        __typename: Literal["Package"]

        # latestVersion  # TODO
        name: str
        packageType: str
        statistics: _PackageStatisticsData
        # version  # TODO
        # versions  # TODO


class Package(Node, RepositoryNode, Type):
    """
    Represents a package.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: PackageData

    @staticmethod
    def _patch_data(
        data: PackageData,
        /,
    ) -> PackageData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: PackageData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "download_count": "statistics{downloadsTotalCount}",
        "name": "name",
        # "type": "packageType",  # TODO: type
    }

    _node_prefix = "P"

    _repr_fields = [
        "name",
    ]

    @property
    def download_count(
        self,
        /,
    ) -> int:
        """
        The number of times the package has been downloaded.

        :type: :class:`int`
        """

        return self._data["statistics"]["downloadsTotalCount"]

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The name of the package.

        :type: :class:`str`
        """

        return self._data["name"]

    async def fetch_download_count(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of times the package has been downloaded.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("statistics{downloadsTotalCount}")  # type: ignore

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the package.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore


__all__ = [
    "Package",
]
