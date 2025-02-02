from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.core.http import HTTPClient
    from github.git import ReferenceType

import github
from github.interfaces import Node, RepositoryNode, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.git.commit import CommitData
    from github.git.tag import TagData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.type import TypeData
    from github.repository.pull import PullData


    class ReferenceData(NodeData, RepositoryNodeData, TypeData):
        __typenmae: Literal["Ref"]

        associatedPullRequests: ConnectionData[PullData]
        # branchProtectionRule  # TODO
        # compare  # TODO
        name: str
        prefix: str
        # refUpdateRule  # TODO
        # rules  # TODO
        target: CommitData | TagData


class Reference(Node, RepositoryNode, Type):
    """
    Represents a Git ref.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: ReferenceData

    @staticmethod
    def _patch_data(
        data: ReferenceData,
        /,
    ) -> ReferenceData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: ReferenceData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = {
        "name": "name,prefix",
    }

    _graphql_type = "Ref"

    _node_prefix = "REF"

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The qualified name of the reference.

        :type: :class:`str`
        """

        return "/".join((self._data["name"], self._data["prefix"]))

    @property
    def type(
        self,
        /,
    ) -> ReferenceType:
        """
        The type of the reference.

        .. note::

            This is not an API field.

            Instead, this is calculated using
            :attr:`~github.Reference.name`, and requires that
            field to be present.

        :type: :class:`~github.ReferenceType`
        """

        if self.name.startswith("refs/heads/"):
            return github.ReferenceType.head
        elif self.name.startswith("refs/tags/"):
            return github.ReferenceType.tag
        else:
            raise NotImplementedError

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the qualified name of the reference.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        data: ReferenceData = await self._fetch_field("name,prefix")  # type: ignore
        return "/".join((data["name"], data["prefix"]))

    async def fetch_type(
        self,
        /,
    ) -> ReferenceType:
        """
        |coro|

        Fetches the type of the reference.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.ReferenceType`
        """

        data: ReferenceData = await self._fetch_field("name,prefix")  # type: ignore
        name = "/".join((data["name"], data["prefix"]))

        if name.startswith("refs/heads/"):
            return github.ReferenceType.head
        elif name.startswith("refs/tags/"):
            return github.ReferenceType.tag
        else:
            raise NotImplementedError


__all__ = [
    "Reference",
]
