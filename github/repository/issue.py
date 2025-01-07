from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.connection import Connection
    from github.core.http import HTTPClient
    from github.repository import IssueState
    from github.user import User
    from github.user.user import UserData

import github
from github.interfaces import Assignable, Closable, Comment, Deletable, Labelable, Lockable, Node, Reactable, RepositoryNode, Resource, Subscribable, Type, Updatable
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.interfaces.assignable import AssignableData
    from github.interfaces.closable import ClosableData
    from github.interfaces.comment import CommentData
    from github.interfaces.deletable import DeletableData
    from github.interfaces.labelable import LabelableData
    from github.interfaces.lockable import LockableData
    from github.interfaces.node import NodeData
    from github.interfaces.reactable import ReactableData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.type import TypeData
    from github.interfaces.updatable import UpdatableData
    from github.repository.issuestate import IssueStateData


    class IssueData(
        AssignableData,
        ClosableData,
        CommentData,
        # CommentableData,  # TODO
        DeletableData,
        LabelableData,
        LockableData,
        NodeData,
        # ProjectOwnerData,  # TODO
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
        state: IssueStateData
        stateReason: Literal["COMPLETED", "DUPLICATE", "NOT_PLANNED", "REOPENED"] | None
        # subIssues  # TODO
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
        cls: type[Self],
        data: IssueData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

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
        "state": "state",
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
    def state(
        self: Self,
        /,
    ) -> IssueState:
        """
        The state of the issue.

        :type: :class:`~github.IssueState`
        """

        return github.IssueState(self._data["state"])

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

        return int(await self._fetch_field("fullDatabaseId"))  # type: ignore

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

    async def fetch_state(
        self: Self,
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

    def fetch_participants(
        self: Self,
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

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_issue_participants,
            self.id,
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else None,
            **kwargs,
        )


__all__ = [
    "Issue",
]
