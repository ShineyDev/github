from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.connection import Connection
    from github.core.http import HTTPClient
    from github.repository import IssueCloseReason, IssueState, Milestone
    from github.user import User
    from github.user.user import UserData

import github
from github.interfaces import Assignable, Closable, Comment, Deletable, Labelable, Lockable, Node, ProjectOwner, Reactable, RepositoryNode, Resource, Subscribable, Type, Updatable
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.git.reference import ReferenceData
    from github.interfaces.assignable import AssignableData
    from github.interfaces.closable import ClosableData
    from github.interfaces.comment import CommentData
    from github.interfaces.deletable import DeletableData
    from github.interfaces.labelable import LabelableData
    from github.interfaces.lockable import LockableData
    from github.interfaces.node import NodeData
    from github.interfaces.projectowner import ProjectOwnerData
    from github.interfaces.reactable import ReactableData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.type import TypeData
    from github.interfaces.updatable import UpdatableData
    from github.repository.issueclosereason import IssueCloseReasonData
    from github.repository.issuestate import IssueStateData
    from github.repository.milestone import MilestoneData
    from github.repository.pull import PullData


    class IssueData(
        AssignableData,
        ClosableData,
        CommentData,
        # CommentableData,  # TODO
        DeletableData,
        LabelableData,
        LockableData,
        NodeData,
        ProjectOwnerData,
        ReactableData,
        RepositoryNodeData,
        ResourceData,
        SubscribableData,
        TypeData,
        UpdatableData,
    ):
        __typename: Literal["Issue"]

        bodyResourcePath: str
        bodyUrl: str
        closedByPullRequestsReferences: ConnectionData[PullData]
        fullDatabaseId: str
        # hovercard  # TODO
        isPinned: bool
        isReadByViewer: bool
        linkedBranches: ConnectionData[ReferenceData]
        milestone: MilestoneData | None
        number: int
        parent: IssueData | None
        participants: ConnectionData[UserData]
        state: IssueStateData
        stateReason: IssueCloseReasonData
        subIssues: ConnectionData[IssueData]
        # subIssuesSummary  # TODO
        # timelineItems  # TODO
        title: str
        titleHTML: str
        # trackedInIssues  # TODO
        # trackedIssues  # TODO
        # trackedIssuesCount  # TODO
        viewerThreadSubscriptionFormAction: Literal["NONE", "SUBSCRIBE", "UNSUBSCRIBE"]
        viewerThreadSubscriptionStatus: Literal["DISABLED", "IGNORING_LIST", "IGNORING_THREAD", "NONE", "SUBSCRIBED_TO_LIST", "SUBSCRIBED_TO_THREAD", "SUBSCRIBED_TO_THREAD_EVENTS", "SUBSCRIBED_TO_THREAD_TYPE", "UNAVAILABLE"]


class Issue(
    Assignable,
    Closable,
    Comment,
    Deletable,
    Labelable,
    Lockable,
    Node,
    ProjectOwner,
    Reactable,
    RepositoryNode,
    Resource,
    Subscribable,
    Type,
    Updatable,
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

    @staticmethod
    def _patch_data(
        data: IssueData,
        /,
    ) -> IssueData:
        data = Comment._patch_data(data)

        return data

    @classmethod
    def _from_data(
        cls,
        data: IssueData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _repr_fields = [
        "number",
    ]

    _graphql_fields = {
        # "": "bodyResourcePath",  # TODO: name
        # "": "bodyUrl",  # TODO: name
        "database_id": "fullDatabaseId",
        "is_pinned": "isPinned",
        "is_read": "isReadByViewer",
        "number": "number",
        "state": "state",
        "closed_reason": "stateReason",
        "title": "title",
        "title_html": "titleHTML",
        # "": "viewerThreadSubscriptionFormAction",  # TODO: name, type
        # "": "viewerThreadSubscriptionStatus",  # TODO: name, type
    }

    _node_prefix = "I"

    @property
    def closed_reason(
        self,
        /,
    ) -> IssueCloseReason | None:
        """
        The reason the issue is closed, if it is.

        :type: :class:`~github.IssueCloseReason` | None
        """

        reason = self._data["stateReason"]

        if reason == "REOPENED":
            return None

        return github.IssueCloseReason(reason)

    @property
    def database_id(
        self,
        /,
    ) -> int:
        """
        The database ID of the issue.

        :type: :class:`int`
        """

        return int(self._data["fullDatabaseId"])

    @property
    def is_pinned(
        self,
        /,
    ) -> bool:
        """
        Whether the issue is pinned.

        :type: :class:`bool`
        """

        return self._data["isPinned"]

    @property
    def is_read(
        self,
        /,
    ) -> bool:
        """
        Whether the issue has been read by the authenticated user.

        :type: :class:`bool`
        """

        return self._data["isReadByViewer"]

    @property
    def number(
        self,
        /,
    ) -> int:
        """
        The number of the issue.

        :type: :class:`int`
        """

        return self._data["number"]

    @property
    def state(
        self,
        /,
    ) -> IssueState:
        """
        The state of the issue.

        :type: :class:`~github.IssueState`
        """

        return github.IssueState(self._data["state"])

    @property
    def title(
        self,
        /,
    ) -> str:
        """
        The title of the issue.

        :type: :class:`str`
        """

        return self._data["title"]

    @property
    def title_html(
        self,
        /,
    ) -> str:
        """
        The title of the issue as HTML.

        :type: :class:`str`
        """

        return self._data["titleHTML"]

    async def fetch_closed_reason(
        self,
        /,
    ) -> IssueCloseReason | None:
        """
        |coro|

        Fetches the reason the issue is closed, if it is.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.IssueCloseReason` | None
        """

        reason = await self._fetch_field("stateReason")

        if reason == "REOPENED":
            return None

        return github.IssueCloseReason(reason)

    async def fetch_database_id(
        self,
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

        return int(await self._fetch_field("fullDatabaseId"))  # type: ignore

    async def fetch_is_pinned(
        self,
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
        self,
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
        self,
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

    async def fetch_state(
        self,
        /,
    ) -> IssueState:
        """
        |coro|

        Fetches the state of the issue.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.IssueState`
        """

        return github.IssueState(await self._fetch_field("state"))

    async def fetch_title(
        self,
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
        self,
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

    async def fetch_milestone(
        self,
        /,
        **kwargs,  # TODO
    ) -> Milestone | None:
        """
        |coro|

        Fetches the milestone the issue is contributing toward, if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Milestone` | None
        """

        data = await self._http.fetch_issue_milestone(self.id, **kwargs)

        if data is None:
            return None

        return github.Milestone._from_data(data, http=self._http)

    def fetch_participants(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[User]:
        """
        |aiter|

        Fetches participants from the issue.


        Parameters
        ----------

        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.connection.Connection`[:class:`github.User`]
        """

        return github.Connection(
            self._http.collect_issue_participants,
            self.id,
            data_map=lambda d: github.User._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else None,
            **kwargs,
        )


__all__ = [
    "Issue",
]
