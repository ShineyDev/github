from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

from github.interfaces import Assignable, Closable, Comment, Deletable, Labelable, Node, RepositoryNode, Resource, Subscribable, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.interfaces.assignable import AssignableData
    from github.interfaces.closable import ClosableData
    from github.interfaces.comment import CommentData
    from github.interfaces.deletable import DeletableData
    from github.interfaces.labelable import LabelableData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.subscribable import SubscribableData
    from github.user.user import UserData


    class IssueData(
        AssignableData,
        ClosableData,
        CommentData,
        # CommentableData,  # TODO
        DeletableData,
        LabelableData,
        # LockableData,  # TODO
        NodeData,
        # ProjectOwnerData,  # TODO
        # ReactableData,  # TODO
        RepositoryNodeData,
        ResourceData,
        SubscribableData,
        # UpdatableData,  # TODO
    ):
        __typename: Literal["Issue"]

        bodyResourcePath: str
        bodyUrl: str
        # closedByPullRequestsReferences  # TODO
        fullDatabaseId: str
        # hovercard  # TODO
        isPinned: bool
        isReadByViewer: bool
        # linkedBranches  # TODO
        # milestone: MilestoneData  # TODO
        number: int
        parent: IssueData | None
        participants: ConnectionData[UserData]
        state: str
        stateReason: str
        # subIssues  # TODO
        # subIssuesSummary  # TODO
        # timelineItems  # TODO
        title: str
        titleHTML: str
        # trackedInIssues  # TODO
        # trackedIssues  # TODO
        # trackedIssuesCount  # TODO
        viewerThreadSubscriptionFormAction: str
        viewerThreadSubscriptionStatus: str


class Issue(
    Assignable,
    Closable,
    Comment,
    Deletable,
    Labelable,
    Node,
    RepositoryNode,
    Resource,
    Subscribable,
    Type,
):
    """
    Represents an issue.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: IssueData

    _repr_fields: list[str] = [
        "number",
    ]

    _graphql_fields: dict[str, str] = {
        # "": "bodyResourcePath",  # TODO: name
        # "": "bodyUrl",  # TODO: name
        "database_id": "fullDatabaseId",
        "is_pinned": "isPinned",
        "is_read": "isReadByViewer",
        "number": "number",
        # "state": "state",  # TODO: type
        # "": "stateReason",  # TODO: name, type
        "title": "title",
        "title_html": "titleHTML",
        # "": "viewerThreadSubscriptionFormAction",  # TODO: name, type
        # "": "viewerThreadSubscriptionStatus",  # TODO: name, type
    }

    _node_prefix: str = "I"

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the issue.

        :type: :class:`int`
        """

        return int(self._data["fullDatabaseId"])

    @property
    def is_pinned(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the issue is pinned.

        :type: :class:`bool`
        """

        return self._data["isPinned"]

    @property
    def is_read(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the issue has been read by the authenticated user.

        :type: :class:`bool`
        """

        return self._data["isReadByViewer"]

    @property
    def number(
        self: Self,
        /,
    ) -> int:
        """
        The number of the issue.

        :type: :class:`int`
        """

        return self._data["number"]

    @property
    def title(
        self: Self,
        /,
    ) -> str:
        """
        The title of the issue.

        :type: :class:`str`
        """

        return self._data["title"]

    @property
    def title_html(
        self: Self,
        /,
    ) -> str:
        """
        The title of the issue as HTML.

        :type: :class:`str`
        """

        return self._data["titleHTML"]

    async def fetch_database_id(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the issue.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_is_pinned(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the issue is pinned.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isPinned")  # type: ignore

    async def fetch_is_read(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the issue has been read by the authenticated
        user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isReadByViewer")  # type: ignore

    async def fetch_number(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of the issue.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("number")  # type: ignore

    async def fetch_title(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the title of the issue.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("title")  # type: ignore

    async def fetch_title_html(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the title of the issue as HTML.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("titleHTML")  # type: ignore


__all__ = [
    "Issue",
]
