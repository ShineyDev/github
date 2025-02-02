from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.core.http import HTTPClient

from github.interfaces import GitNode, Node, RepositoryNode, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.git.treeentry import TreeEntryData
    from github.interfaces.gitnode import GitNodeData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.type import TypeData


    class TreeData(GitNodeData, NodeData, RepositoryNodeData, TypeData):
        __typename: Literal["Tree"]

        entries: list[TreeEntryData]


class Tree(GitNode, Node, RepositoryNode, Type):
    """
    Represents a Git tree.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: TreeData

    @staticmethod
    def _patch_data(
        data: TreeData,
        /,
    ) -> TreeData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: TreeData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _node_prefix = "TREE"


__all__ = [
    "Tree",
]
