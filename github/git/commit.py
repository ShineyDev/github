from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.utility.types import DateTime

import github
from github.interfaces import GitNode, Node, RepositoryNode, Resource, Subscribable, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.git.tree import TreeData
    from github.interfaces.gitnode import GitNodeData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.type import TypeData
    from github.organization.organization import OrganizationData
    from github.repository.pull import PullData


    class CommitData(GitNodeData, NodeData, RepositoryNodeData, ResourceData, SubscribableData, TypeData):
        __typename: Literal["Commit"]

        additions: int
        associatedPullRequests: ConnectionData[PullData]
        # author  # TODO
        authoredByCommitter: bool
        authoredDate: str
        # authors  # TODO
        # blame  # TODO
        changedFiles: int
        changedFilesIfAvailable: int | None
        # checkSuites  # TODO
        committedDate: str
        committedViaWeb: bool
        # committer  # TODO
        deletions: int
        # deployments  # TODO
        # file  # TODO
        # history  # TODO
        message: str
        messageBody: str
        messageBodyHTML: str
        messageHeadline: str
        messageHeadlineHTML: str
        onBehalfOf: OrganizationData | None
        parents: ConnectionData[CommitData]
        pushedDate: str | None
        # signature  # TODO
        # status  # TODO
        # statusCheckRollup  # TODO
        # submodules  # TODO
        tarballUrl: str
        tree: TreeData
        treeResourcePath: str
        treeUrl: str
        updatesChannel: str | None
        zipballUrl: str


class Commit(GitNode, Node, RepositoryNode, Resource, Subscribable, Type):
    """
    Represents a Git commit.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: CommitData

    @staticmethod
    def _patch_data(
        data: CommitData,
        /,
    ) -> CommitData:
        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: CommitData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _graphql_fields: dict[str, str] = {
        "addition_count": "additions",
        # "": "authoredByCommitter",  # TODO: name
        "authored_at": "authoredDate",
        "file_count": "changedFilesIfAvailable",
        "committed_at": "committedDate",
        # "": "committedViaWeb",  # TODO: name
        "deletion_count": "deletions",
        "message": "message",
        # "": "messageBody",  # TODO: name
        # "": "messageBodyHTML",  # TODO: name
        # "": "messageHeadline",  # TODO: name
        # "": "messageHeadlineHTML",  # TODO: name
        # "": "pushedDate",  # TODO: deprecated
        # "": "tarballUrl",  # TODO: name
        # "": "treeResourcePath",  # TODO: name
        # "": "treeUrl",  # TODO: name
        # "": "updatesChannel",  # TODO: iunno
        # "": "zipballUrl",  # TODO: name
    }

    _node_prefix: str = "C"

    @property
    def addition_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of additions in this commit.

        :type: :class:`int`
        """

        return self._data["additions"]

    @property
    def authored_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the commit was authored.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["authoredDate"])

    @property
    def committed_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the commit was committed.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["committedDate"])

    @property
    def deletion_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of deletions in this commit.

        :type: :class:`int`
        """

        return self._data["deletions"]

    @property
    def file_count(
        self: Self,
        /,
    ) -> int | None:
        """
        The number of files changed in this commit, or ``None`` if
        GitHub is unable to calculate the number of changed files.


        :type: :class:`int` | None
        """

        return self._data["changedFilesIfAvailable"]

    @property
    def message(
        self: Self,
        /,
    ) -> str:
        """
        The message of the commit.

        :type: :class:`str`
        """

        return self._data["message"]

    async def fetch_addition_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of additions in this commit.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("additions")  # type: ignore

    async def fetch_authored_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the commit was authored.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        authored_at = await self._fetch_field("authoredDate")

        if TYPE_CHECKING:
            authored_at = cast(str, authored_at)

        return github.utility.iso_to_datetime(authored_at)

    async def fetch_committed_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the commit was committed.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        committed_at = await self._fetch_field("committedDate")

        if TYPE_CHECKING:
            committed_at = cast(str, committed_at)

        return github.utility.iso_to_datetime(committed_at)

    async def fetch_deletion_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of deletions in this commit.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("deletions")  # type: ignore

    async def fetch_file_count(
        self: Self,
        /,
    ) -> int | None:
        """
        |coro|

        Fetches the number of files changed in this commit, or ``None``
        if GitHub is unable to calculate the number of changed files.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int` | None
        """

        return await self._fetch_field("changedFilesIfAvailable")  # type: ignore

    async def fetch_message(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the message of the commit.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("message")  # type: ignore


__all__ = [
    "Commit",
]
