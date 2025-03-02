from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.connection import Connection, PullOrder
    from github.core.http import HTTPClient
    from github.git import Commit, ReferenceType, Tag
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

        return "".join((self._data["prefix"], self._data["name"]))

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
        return "".join((data["prefix"], data["name"]))

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
        name = "".join((data["prefix"], data["name"]))

        if name.startswith("refs/heads/"):
            return github.ReferenceType.head
        elif name.startswith("refs/tags/"):
            return github.ReferenceType.tag
        else:
            raise NotImplementedError

    async def fetch_target(
        self,
        /,
        **kwargs,  # TODO
    ) -> Commit | Tag:
        """
        |coro|

        Fetches the target of the reference.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Commit` | :class:`~github.Tag`
        """

        data = await self._http.fetch_reference_target(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Commit":
            return github.Commit._from_data(data, http=self._http)
        elif data["__typename"] == "Tag":
            return github.Tag._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"invalid type {data['__typename']} for Ref.target")

    def fetch_pulls(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order: PullOrder = MISSING,
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
        order: :class:`~github.PullOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection` of :class:`~github.Pull`
        """

        return github.Connection(
            self._http.collect_reference_pulls,
            self.id,
            order.value if order is not MISSING else None,
            data_map=lambda d: github.Pull._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )


__all__ = [
    "Reference",
]
