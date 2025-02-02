from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.connection import Connection, PullOrder
    from github.core.http import HTTPClient
    from github.git import ReferenceType
    from github.repository import Pull

import github
from github.interfaces import Node, RepositoryNode, Type
from github.utility import MISSING


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

    def fetch_pulls(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: PullOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Pull]:
        """
        |aiter|

        Fetches pull requests associated with the reference.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.PullOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Pull`]
        """

        return github.Connection(
            self._http.collect_reference_pulls,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Pull._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )


__all__ = [
    "Reference",
]
