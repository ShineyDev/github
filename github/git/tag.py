from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.core.http import HTTPClient

from github.interfaces import GitNode, Node, RepositoryNode, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.gitnode import GitNodeData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.type import TypeData


    class TagData(GitNodeData, NodeData, RepositoryNodeData, TypeData):
        __typename: Literal["Tag"]

        message: str | None
        name: str
        # tagger  # TODO
        # target  # TODO


class Tag(GitNode, Node, RepositoryNode, Type):
    """
    Represents a Git tag.

    .. note::

        An unannotated (lightweight) tag will always yield from
        GitHub's GraphQL API as a :class:`~github.Commit` object.


    .. seealso::

        :meth:`Repository.fetch_refs <github.Repository.fetch_refs>`


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: TagData

    @staticmethod
    def _patch_data(
        data: TagData,
        /,
    ) -> TagData:
        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: TagData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _graphql_fields: list[str] = [
        "message",
        "name",
    ]

    _node_prefix: str = "TA"

    @property
    def message(
        self: Self,
        /,
    ) -> str | None:
        """
        The message of the tag, if any.

        :type: :class:`str` | None
        """

        return self._data["message"]

    @property
    def name(
        self: Self,
        /,
    ) -> str:
        """
        The name of the tag.

        :type: :class:`str`
        """

        return self._data["name"]

    async def fetch_message(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the message of the tag, if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("message")  # type: ignore

    async def fetch_name(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the tag.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore


__all__ = [
    "Tag",
]
