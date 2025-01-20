from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.core.http import HTTPClient

from github.interfaces import GitNode, Node, RepositoryNode, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.gitnode import GitNodeData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.type import TypeData


    class BlobData(GitNodeData, NodeData, RepositoryNodeData, TypeData):
        __typename: Literal["Blob"]

        byteSize: int
        isBinary: bool | None
        isTruncated: bool
        text: str | None


class Blob(GitNode, Node, RepositoryNode, Type):
    """
    Represents a Git blob.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: BlobData

    @staticmethod
    def _patch_data(
        data: BlobData,
        /,
    ) -> BlobData:
        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: BlobData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _graphql_fields =  {
        "size": "byteSize",
        "is_text": "isBinary",
        # "": "isTruncated",  # TODO: [blob-content]
        # "": "text",  # TODO: [blob-content]
    }

    _node_prefix = "B"

    @property
    def is_text(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the blob is text.

        :type: :class:`bool`
        """

        is_binary = self._data["isBinary"]

        if is_binary is None:
            return False

        return not is_binary

    @property
    def size(
        self: Self,
        /,
    ) -> int:
        """
        The size of the blob in bytes.

        :type: :class:`int`
        """

        return self._data["byteSize"]

    async def fetch_is_text(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the blob is text.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        is_binary = await self._fetch_field("isBinary")

        if TYPE_CHECKING:
            is_binary = cast(bool | None, is_binary)

        if is_binary is None:
            return False

        return not is_binary

    async def fetch_size(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the size of the blob in bytes.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("byteSize")  # type: ignore


__all__ = [
    "Blob",
]
