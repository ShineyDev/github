from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.connection import Connection
    from github.user import User
    from github.utility.types import DateTime

import github
from github.interfaces import Assignable, Closable, Comment, Labelable, Lockable, Node, Reactable, RepositoryNode, Resource, Type, Subscribable, Updatable
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.automation.bot import BotData
    from github.automation.mannequin import MannequinData
    from github.connection.connection import ConnectionData
    from github.interfaces.assignable import AssignableData
    from github.interfaces.closable import ClosableData
    from github.interfaces.comment import CommentData
    from github.interfaces.labelable import LabelableData
    from github.interfaces.lockable import LockableData
    from github.interfaces.node import NodeData
    from github.interfaces.reactable import ReactableData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.type import TypeData
    from github.interfaces.updatable import UpdatableData
    from github.organization.organization import OrganizationData
    from github.repository.issue import IssueData
    from github.repository.repository import RepositoryData
    from github.user.user import UserData


    class PullData(
        AssignableData,
        ClosableData,
        CommentData,
        # CommentableData,  # TODO
        LabelableData,
        LockableData,
        NodeData,
        # ProjectOwnerData,  # TODO
        ReactableData,
        RepositoryNodeData,
        ResourceData,
        TypeData,
        SubscribableData,
        UpdatableData,
    ):
        __typename: Literal["PullRequest"]

        additions: int
        # autoMergeRequest  # TODO
        # baseRef  # TODO
        baseRefName: str
        baseRefOid: str
        baseRepository: RepositoryData | None
        canBeRebased: bool
        changedFiles: int
        checksResourcePath: str
        checksUrl: str
        closingIssuesReferences: ConnectionData[IssueData]
        # commits  # TODO
        deletions: int
        # files  # TODO
        fullDatabaseId: str
        # headRef  # TODO
        headRefName: str
        headRefOid: str
        headRepository: RepositoryData | None
        headRepositoryOwner: OrganizationData | UserData | None
        # hovercard  # TODO
        isCrossRepository: bool
        isDraft: bool
        isInMergeQueue: bool
        isMergeQueueEnabled: bool
        isReadByViewer: bool
        # latestOpinionatedReviews  # TODO
        # latestReviews  # TODO
        maintainerCanModify: bool
        # mergeCommit  # TODO
        # mergeQueue  # TODO
        # mergeQueueEntry  # TODO
        mergeStateStatus: Literal["BEHIND", "BLOCKED", "CLEAN", "DIRTY", "HAS_HOOKS", "UNKNOWN", "UNSTABLE"]
        mergeable: Literal["CONFLICTING", "MERGEABLE", "UNKNOWN"]
        merged: bool
        mergedAt: str | None
        mergedBy: BotData | MannequinData | UserData | None
        # milestone  # TODO
        number: int
        participants: ConnectionData[UserData]
        permalink: str
        # potentialMergeCommit  # TODO
        revertResourcePath: str
        revertUrl: str
        reviewDecision: Literal["APPROVED", "CHANGES_REQUESTED", "REVIEW_REQUIRED"]
        # reviewRequests  # TODO
        # reviewThreads  # TODO
        # reviews  # TODO
        state: Literal["CLOSED", "MERGED", "OPEN"]
        # statusCheckRollup  # TODO
        # timelineItems  # TODO
        title: str
        titleHTML: str
        totalCommentsCount: int
        viewerCanApplySuggestion: bool
        viewerCanDeleteHeadRef: bool
        viewerCanDisableAutoMerge: bool
        viewerCanEditFiles: bool
        viewerCanEnableAutoMerge: bool
        viewerCanMergeAsAdmin: bool
        viewerCanUpdateBranch: bool
        # viewerLatestReview  # TODO
        # viewerLatestReviewRequest  # TODO
        viewerMergeBodyText: str
        viewerMergeHeadlineText: str


class Pull(
    Assignable,
    Closable,
    Comment,
    Labelable,
    Lockable,
    Node,
    Reactable,
    RepositoryNode,
    Resource,
    Type,
    Subscribable,
    Updatable,
):
    """
    Represents a pull request.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: PullData

    _graphql_fields: dict[str, str] = {
        "addition_count": "additions",
        # "": "baseRefName",  # TODO: name
        # "": "baseRefOid",  # TODO: name
        # "": "canBeRebased",  # TODO: name
        "file_count": "changedFiles",
        # "": "checksResourcePath",  # TODO: name
        # "": "checksUrl",  # TODO: name
        "deletion_count": "deletions",
        "database_id": "fullDatabaseId",
        # "": "headRefName",  # TODO: name
        # "": "headRefOid",  # TODO: name
        # "": "isCrossRepository",  # TODO: name
        "is_draft": "isDraft",
        # "": "isInMergeQueue",  # TODO: name
        # "": "isMergeQueueEnabled",  # TODO: name
        "is_read": "isReadByViewer",
        # "": "maintainerCanModify",  # TODO: name
        # "": "mergeStateStatus",  # TODO: name, type
        # "": "mergeable",  # TODO: name, type
        "is_merged": "merged",
        "merged_at": "mergedAt",
        "number": "number",
        # "": "permalink",  # TODO: name
        # "": "revertResourcePath",  # TODO: name
        # "": "revertUrl",  # TODO: name
        # "": "reviewDecision",  # TODO: name, type
        # "state": "state",  # TODO: type
        "title": "title",
        "title_html": "titleHTML",
        "comment_count": "totalCommentsCount",
        # "": "viewerCanApplySuggestion",  # TODO: name
        # "": "viewerCanDeleteHeadRef",  # TODO: name
        # "": "viewerCanDisableAutoMerge",  # TODO: name
        # "": "viewerCanEditFiles",  # TODO: name
        # "": "viewerCanEnableAutoMerge",  # TODO: name
        # "": "viewerCanMergeAsAdmin",  # TODO: name
        # "": "viewerCanUpdateBranch",  # TODO: name
    }

    _graphql_type: str = "PullRequest"

    _node_prefix: str = "PR"

    @property
    def addition_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of additions in this pull request.

        :type: :class:`int`
        """

        return self._data["additions"]

    @property
    def comment_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of comments on the pull request.

        :type: :class:`int`
        """

        return self._data["totalCommentsCount"]

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the pull request.

        :type: :class:`int`
        """

        return int(self._data["fullDatabaseId"])

    @property
    def deletion_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of deletions in this pull request.

        :type: :class:`int`
        """

        return self._data["deletions"]

    @property
    def file_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of files changed in this pull request.

        :type: :class:`int`
        """

        return self._data["changedFiles"]

    @property
    def is_draft(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the pull request is a draft.

        :type: :class:`bool`
        """

        return self._data["isDraft"]

    @property
    def is_merged(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the pull request is merged.

        :type: :class:`bool`
        """

        return self._data["merged"]

    @property
    def is_read(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the pull request has been read by the authenticated
        user.

        :type: :class:`bool`
        """

        return self._data["isReadByViewer"]

    @property
    def merged_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the pull requets was merged, if any.

        :type: :class:`~datetime.datetime` | None
        """

        merged_at = self._data["mergedAt"]

        if merged_at is None:
            return None

        return github.utility.iso_to_datetime(merged_at)

    @property
    def number(
        self: Self,
        /,
    ) -> int:
        """
        The number of the pull request.

        :type: :class:`int`
        """

        return self._data["number"]

    @property
    def title(
        self: Self,
        /,
    ) -> str:
        """
        The title of the pull request.

        :type: :class:`str`
        """

        return self._data["title"]

    @property
    def title_html(
        self: Self,
        /,
    ) -> str:
        """
        The title of the pull request as HTML.

        :type: :class:`str`
        """

        return self._data["titleHTML"]

    async def fetch_addition_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of additions in this pull request.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("additions")  # type: ignore

    async def fetch_comment_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of comments on the pull request.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("totalCommentsCount")  # type: ignore

    async def fetch_database_id(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the pull request.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return int(await self._fetch_field("fullDatabaseId"))  # type: ignore

    async def fetch_deletion_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of deletions in this pull request.


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
    ) -> int:
        """
        |coro|

        Fetches the number of files changed in this pull request.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("changedFiles")  # type: ignore

    async def fetch_is_draft(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the pull request is a draft.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isDraft")  # type: ignore

    async def fetch_is_merged(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the pull request is merged.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("merged")  # type: ignore

    async def fetch_is_read(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the pull request has been read by the
        authenticated user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isReadByViewer")  # type: ignore

    async def fetch_merged_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the pull request was merged,
        if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        merged_at = await self._fetch_field("mergedAt")

        if merged_at is None:
            return None

        if TYPE_CHECKING:
            merged_at = cast(str, merged_at)

        return github.utility.iso_to_datetime(merged_at)

    async def fetch_number(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of the pull request.


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

        Fetches the title of the pull request.


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

        Fetches the title of the pull request as HTML.


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

        Fetches participants from the pull request.


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


        :rtype: :class:`~github.Connection`[:class:`github.User`]
        """

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_pull_participants,
            self.id,
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else None,
            **kwargs,
        )


__all__ = [
    "Pull",
]
