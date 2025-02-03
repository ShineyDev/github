from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal, overload, cast

    from github.connection import Connection, DiscussionOrder, IssueOrder, LabelOrder, MilestoneOrder, PullOrder, ReferenceOrder, ReleaseOrder, RepositoryOrder
    from github.content import CodeOfConduct, License
    from github.core.http import HTTPClient
    from github.git import Reference, ReferenceType, Tag
    from github.organization import Organization
    from github.repository import Discussion, Issue, Label, Milestone, Pull, Release, RepositoryVisibility, Topic
    from github.repository.discussion import DiscussionData
    from github.repository.issue import IssueData
    from github.repository.milestone import MilestoneData
    from github.repository.pull import PullData
    from github.user import User
    from github.utility.types import DateTime

import random

import github
from github.interfaces import Node, PackageOwner, Starrable, Subscribable, Resource, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.content.codeofconduct import CodeOfConductData
    from github.content.license import LicenseData
    from github.git.reference import ReferenceData
    from github.interfaces.node import NodeData
    from github.interfaces.packageowner import PackageOwnerData
    from github.interfaces.starrable import StarrableData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.resource import ResourceData
    from github.interfaces.type import TypeData
    from github.organization.organization import OrganizationData
    from github.repository.label import LabelData
    from github.repository.release import ReleaseData
    from github.repository.topic import TopicData
    from github.security.vulnerability import VulnerabilityData
    from github.user.user import UserData


    class RepositoryData(
        NodeData,
        PackageOwnerData,
        # ProjectOwnerData,  # TODO
        StarrableData,
        SubscribableData,
        ResourceData,
        TypeData,
    ):
        __typename: Literal["Repository"]

        allowUpdateBranch: bool
        archivedAt: str | None
        assignableUsers: ConnectionData[UserData]
        autoMergeAllowed: bool
        # branchProtectionRules  # TODO
        codeOfConduct: CodeOfConductData | None
        # codeowners  # TODO
        collaborators: ConnectionData[UserData]
        # commitComments  # TODO
        # contactLinks  # TODO
        # contributingGuidelines  # TODO
        createdAt: str
        databaseId: int
        defaultBranchRef: ReferenceData | None
        deleteBranchOnMerge: bool
        # dependencyGraphManifests  # TODO
        # deployKeys  # TODO
        # deployments  # TODO
        description: str | None
        descriptionHTML: str | None
        discussion: DiscussionData
        # discussionCategories  # TODO
        # discussionCategory  # TODO
        discussions: ConnectionData[DiscussionData]
        diskUsage: int
        # environment  # TODO
        # environments  # TODO
        forkCount: int
        forkingAllowed: bool
        forks: ConnectionData[RepositoryData]
        # fundingLinks  # TODO
        hasDiscussionsEnabled: bool
        hasIssuesEnabled: bool
        hasProjectsEnabled: bool
        hasSponsorshipsEnabled: bool
        hasVulnerabilityAlertsEnabled: bool
        hasWikiEnabled: bool
        homepageUrl: str
        # interactionAbility  # TODO
        isArchived: bool
        isBlankIssuesEnabled: bool
        isDisabled: bool
        isEmpty: bool
        isFork: bool
        isInOrganization: bool
        isLocked: bool
        isMirror: bool
        isPrivate: bool
        isSecurityPolicyEnabled: bool
        isTemplate: bool
        isUserConfigurationRepository: bool
        issue: IssueData
        issueOrPullRequest: IssueData | PullData
        # issueTemplates  # TODO
        issues: ConnectionData[IssueData]
        label: LabelData
        labels: ConnectionData[LabelData]
        # languages  # TODO
        latestRelease: ReleaseData | None
        licenseInfo: LicenseData | None
        # lockReason  # TODO
        mentionableUsers: ConnectionData[UserData]
        mergeCommitAllowed: bool
        mergeCommitMessage: Literal["BLANK", "PR_BODY", "PR_TITLE"]
        mergeCommitTitle: Literal["MERGE_MESSAGE", "PR_TITLE"]
        # mergeQueue  # TODO
        milestone: MilestoneData
        milestones: ConnectionData[MilestoneData]
        mirrorUrl: str | None
        name: str
        nameWithOwner: str
        # object  # TODO
        openGraphImageUrl: str
        owner: OrganizationData | UserData
        parent: RepositoryData | None
        # pinnedDiscussions  # TODO
        # pinnedEnvironments  # TODO
        # pinnedIssues  # TODO
        # planFeatures  # TODO
        # primaryLanguage  # TODO
        pullRequest: PullData
        # pullRequestTemplates  # TODO
        pullRequests: ConnectionData[PullData]
        pushedAt: str | None
        rebaseMergeAllowed: bool
        ref: ReferenceData
        refs: ConnectionData[ReferenceData]
        release: ReleaseData
        releases: ConnectionData[ReleaseData]
        repositoryTopics: ConnectionData[TopicData]  # TODO: this is a lie
        # ruleset  # TODO
        # rulesets  # TODO
        securityPolicyUrl: str | None
        shortDescriptionHTML: str | None
        squashMergeAllowed: bool
        squashMergeCommitMessage: Literal["BLANK", "COMMIT_MESSAGES", "PR_BODY"]
        squashMergeCommitTitle: Literal["COMMIT_OR_PR_TITLE", "PR_TITLE"]
        sshUrl: str
        # submodules  # TODO
        # tempCloneToken  # TODO
        templateRepository: RepositoryData | None
        updatedAt: str
        usesCustomOpenGraphImage: bool
        viewerCanAdminister: bool
        viewerCanUpdateTopics: bool
        viewerDefaultCommitEmail: str | None
        viewerDefaultMergeMethod: Literal["MERGE", "REBASE", "SQUASH"]
        viewerPermission: Literal["ADMIN", "MAINTAIN", "READ", "TRIAGE", "WRITE"]
        viewerPossibleCommitEmails: list[str]
        visibility: Literal["INTERNAL", "PRIVATE", "PUBLIC"]
        vulnerabilityAlert: VulnerabilityData
        vulnerabilityAlerts: ConnectionData[VulnerabilityData]
        watchers: ConnectionData[UserData]
        webCommitSignoffRequired: bool


class Repository(
    Node,
    PackageOwner,
    # ProjectOwner,  # TODO
    Starrable,
    Subscribable,
    Resource,
    Type,
):
    """
    Represents a repository.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: RepositoryData

    @staticmethod
    def _patch_data(
        data: RepositoryData,
        /,
    ) -> RepositoryData:
        if data.get("descriptionHTML", False) == "<div></div>":
            data["descriptionHTML"] = None

        if data.get("shortDescriptionHTML", False) == "":
            data["shortDescriptionHTML"] = None

        return data

    @classmethod
    def _from_data(
        cls,
        data: RepositoryData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _repr_fields = [
        "name",
    ]

    _graphql_fields = {
        # "": "allowUpdateBranch",  # TODO: name
        "archived_at": "archivedAt",
        # "": "autoMergeAllowed",  # TODO: name
        "created_at": "createdAt",
        "database_id": "databaseId",
        # "": "deleteBranchOnMerge",  # TODO: name
        "description": "description",
        "description_html": "descriptionHTML",
        "disk_usage": "diskUsage",
        "fork_count": "forkCount",
        "allows_fork": "forkingAllowed",
        "has_discussions_enabled": "hasDiscussionsEnabled",
        "has_issues_enabled": "hasIssuesEnabled",
        "has_projects_enabled": "hasProjectsEnabled",
        "has_sponsors_enabled": "hasSponsorshipsEnabled",
        # "": "hasVulnerabilityAlertsEnabled",  # TODO: name
        "has_wiki_enabled": "hasWikiEnabled",
        # "": "homepageUrl",  # TODO: name
        "is_archived": "isArchived",
        # "": "isBlankIssuesEnabled",  # TODO: name
        "is_disabled": "isDisabled",
        "is_empty": "isEmpty",
        "is_fork": "isFork",
        # "": "isInOrganization",  # TODO: name
        "is_locked": "isLocked",
        "is_mirror": "isMirror",
        "is_private": "isPrivate",
        # "": "isSecurityPolicyEnabled",  # TODO: name
        "is_template": "isTemplate",
        "allows_merge": "mergeCommitAllowed",
        # "": "mergeCommitMessage",  # TODO: name, type
        # "": "mergeCommitTitle",  # TODO: name, type
        # "": "mirrorUrl",  # TODO: name
        "name": "name",
        # "": "nameWithOwner",  # TODO: name
        # "": "openGraphImageUrl",  # TODO: name: name
        "pushed_at": "pushedAt",
        "allows_rebase": "rebaseMergeAllowed",
        # "": "securityPolicyUrl",  # TODO: name
        # "": "shortDescriptionHTML",  # TODO: name
        "allows_squash": "squashMergeAllowed",
        # "": "squashMergeCommitMessage",  # TODO: name, type
        # "": "squashMergeCommitTitle",  # TODO: name, type
        # "": "sshUrl",  # TODO: name
        "updated_at": "updatedAt",
        # "": "usesCustomOpenGraphImage",  # TODO: name
        # "": "viewerCanAdminister",  # TODO: name
        # "": "viewerCanUpdateTopics",  # TODO: name
        # "": "viewerDefaultCommitEmail",  # TODO: name
        # "": "viewerDefaultMergeMethod",  # TODO: name, type
        # "": "viewerPermission",  # TODO: name, type
        # "": "viewerPossibleCommitEmails",  # TODO: name
        "visibility": "visibility",
        # "": "webCommitSignoffRequired",  # TODO: name
    }

    _node_prefix = "R"

    @property
    def allows_fork(
        self,
        /,
    ) -> bool:
        """
        Whether the repository allows forks of itself to be created.

        :type: :class:`bool`
        """

        return self._data["forkingAllowed"]

    @property
    def allows_merge(
        self,
        /,
    ) -> bool:
        """
        Whether the repository allows merge commits to be created by
        merged pull requests.

        :type: :class:`bool`
        """

        return self._data["mergeCommitAllowed"]

    @property
    def allows_rebase(
        self,
        /,
    ) -> bool:
        """
        TODO.

        :type: :class:`bool`
        """

        return self._data["squashMergeAllowed"]

    @property
    def allows_squash(
        self,
        /,
    ) -> bool:
        """
        TODO.

        :type: :class:`bool`
        """

        return self._data["rebaseMergeAllowed"]

    @property
    def archived_at(
        self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the repository was archived, if any.

        :type: :class:`~datetime.datetime` | None
        """

        archived_at = self._data["archivedAt"]

        if archived_at is None:
            return None

        return github.utility.iso_to_datetime(archived_at)

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the repository was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self,
        /,
    ) -> int:
        """
        The database ID of the repository.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def description(
        self,
        /,
    ) -> str | None:
        """
        The description of the repository.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def description_html(
        self,
        /,
    ) -> str | None:
        """
        The description of the repository as HTML.

        :type: :class:`str` | None
        """

        return self._data["descriptionHTML"]

    @property
    def disk_usage(  # TODO: KB or KiB  # TODO: rounding
        self,
        /,
    ) -> int:
        """
        The number of kilobytes the repository occupies on disk.

        :type: :class:`int`
        """

        return self._data["diskUsage"]

    @property
    def fork_count(
        self,
        /,
    ) -> int:
        """
        The number of forks the repository has.

        :type: :class:`int`
        """

        return self._data["forkCount"]

    @property
    def has_discussions_enabled(
        self,
        /,
    ) -> bool:
        """
        Whether the repository has
        :class:`GitHub Discussions <github.Discussion>` enabled.

        :type: :class:`bool`
        """

        return self._data["hasDiscussionsEnabled"]

    @property
    def has_issues_enabled(
        self,
        /,
    ) -> bool:
        """
        Whether the repository has
        :class:`GitHub Issues <github.Issue>` enabled.

        :type: :class:`bool`
        """

        return self._data["hasIssuesEnabled"]

    @property
    def has_projects_enabled(
        self,
        /,
    ) -> bool:
        """
        Whether the repository has
        :class:`GitHub Projects <github.Project>` enabled.

        :type: :class:`bool`
        """

        return self._data["hasProjectsEnabled"]

    @property
    def has_sponsors_enabled(
        self,
        /,
    ) -> bool:
        """
        Whether the repository has
        :class:`GitHub Sponsors <github.Sponsor>` enabled.

        :type: :class:`bool`
        """

        return self._data["hasSponsorshipsEnabled"]

    @property
    def has_wiki_enabled(
        self,
        /,
    ) -> bool:
        """
        Whether the repository has wiki enabled.

        :type: :class:`bool`
        """

        return self._data["hasWikiEnabled"]

    @property
    def is_archived(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is archived.

        :type: :class:`bool`
        """

        return self._data["isArchived"]

    @property
    def is_disabled(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is disabled.

        :type: :class:`bool`
        """

        return self._data["isDisabled"]

    @property
    def is_empty(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is empty.

        :type: :class:`bool`
        """

        return self._data["isEmpty"]

    @property
    def is_fork(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is a fork of another.

        :type: :class:`bool`
        """

        return self._data["isFork"]

    @property
    def is_locked(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is locked.

        :type: :class:`bool`
        """

        return self._data["isLocked"]

    @property
    def is_mirror(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is a mirror of another.

        :type: :class:`bool`
        """

        return self._data["isMirror"]

    @property
    def is_private(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is private.

        :type: :class:`bool`
        """

        return self._data["isPrivate"]

    @property
    def is_template(
        self,
        /,
    ) -> bool:
        """
        Whether the repository is a template.

        :type: :class:`bool`
        """

        return self._data["isTemplate"]

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The name of the repository.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def pushed_at(
        self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the repository was last pushed, if
        any.

        :type: :class:`~datetime.datetime` | None
        """

        pushed_at = self._data["pushedAt"]

        if pushed_at is None:
            return None

        return github.utility.iso_to_datetime(pushed_at)

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the repository was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    @property
    def visibility(
        self,
        /,
    ) -> RepositoryVisibility:
        """
        The visibility of the repository.

        :type: :class:`~github.RepositoryVisibility`
        """

        return github.RepositoryVisibility(self._data["visibility"])

    async def fetch_allows_fork(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository allows forks of itself to be
        created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("forkingAllowed")  # type: ignore

    async def fetch_allows_merge(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository allows merge commits to be
        created by merged pull requests.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("mergeCommitAllowed")  # type: ignore

    async def fetch_allows_rebase(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches TODO.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("rebaseMergeAllowed")  # type: ignore

    async def fetch_allows_squash(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches TODO.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("squashMergeAllowed")  # type: ignore

    async def fetch_archived_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the repository was archived,
        if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        archived_at = await self._fetch_field("archivedAt")

        if archived_at is None:
            return None

        if TYPE_CHECKING:
            archived_at = cast(str, archived_at)

        return github.utility.iso_to_datetime(archived_at)

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the repository was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        created_at = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            created_at = cast(str, created_at)

        return github.utility.iso_to_datetime(created_at)

    async def fetch_database_id(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the repository.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_description(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the description of the repository.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_description_html(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the description of the repository as HTML.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("descriptionHTML")  # type: ignore

    async def fetch_disk_usage(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of kilobytes the repository occupies on
        disk.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("diskUsage")  # type: ignore

    async def fetch_fork_count(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of forks the repository has.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("forkCount")  # type: ignore

    async def fetch_has_discussions_enabled(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository has
        :class:`GitHub Discussions <github.Discussion>` enabled.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("hasDiscussionsEnabled")  # type: ignore

    async def fetch_has_issues_enabled(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository has
        :class:`GitHub Issues <github.Issue>` enabled.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("hasIssuesEnabled")  # type: ignore

    async def fetch_has_projects_enabled(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository has
        :class:`GitHub Projects <github.Project>` enabled.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("hasProjectsEnabled")  # type: ignore

    async def fetch_has_sponsors_enabled(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository has
        :class:`GitHub Sponsors <github.Sponsor>` enabled.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("hasSponsorshipsEnabled")  # type: ignore

    async def fetch_has_wiki_enabled(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository has wiki enabled.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("hasWikiEnabled")  # type: ignore

    async def fetch_is_archived(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is archived.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isArchived")  # type: ignore

    async def fetch_is_disabled(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is disabled.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isDisabled")  # type: ignore

    async def fetch_is_empty(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is empty.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isEmpty")  # type: ignore

    async def fetch_is_fork(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is a fork of another.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isFork")  # type: ignore

    async def fetch_is_locked(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is locked.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isLocked")  # type: ignore

    async def fetch_is_mirror(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is a mirror of another.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isMirror")  # type: ignore

    async def fetch_is_private(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is private.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isPrivate")  # type: ignore

    async def fetch_is_template(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the repository is a template.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isTemplate")  # type: ignore

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the repository.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_pushed_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the repository was last
        pushed, if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        pushed_at = await self._fetch_field("pushedAt")

        if pushed_at is None:
            return None

        if TYPE_CHECKING:
            pushed_at = cast(str, pushed_at)

        return github.utility.iso_to_datetime(pushed_at)

    async def fetch_updated_at(
        self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the repository was last
        updated.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        updated_at = await self._fetch_field("updatedAt")

        if TYPE_CHECKING:
            updated_at = cast(str, updated_at)

        return github.utility.iso_to_datetime(updated_at)

    async def fetch_visibility(
        self,
        /,
    ) -> RepositoryVisibility:
        """
        |coro|

        Fetches the visibility of the repository.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.RepositoryVisibility`
        """

        return github.RepositoryVisibility(await self._fetch_field("visibility"))

    async def fetch_code_of_conduct(
        self,
        /,
        **kwargs,  # TODO
    ) -> CodeOfConduct | None:
        """
        |coro|

        Fetches the code of conduct for the repository, if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.CodeOfConduct` | None
        """

        data = await self._http.fetch_repository_code_of_conduct(self.id, **kwargs)

        if data is None:
            return None

        return github.CodeOfConduct._from_data(data, http=self._http)

    async def fetch_discussion(
        self,
        number: int,
        /,
        **kwargs,  # TODO
    ) -> Discussion:
        """
        |coro|

        Fetches a discussion in the repository.


        Parameters
        ----------
        number: :class:`int`
            The number of the discussion.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Discussion`
        """

        data = await self._http.fetch_repository_discussion(self.id, number, **kwargs)
        return github.Discussion._from_data(data, http=self._http)

    async def fetch_issue(
        self,
        number: int,
        /,
        **kwargs,  # TODO
    ) -> Issue:
        """
        |coro|

        Fetches an issue in the repository.


        Parameters
        ----------
        number: :class:`int`
            The number of the issue.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Issue`
        """

        data = await self._http.fetch_repository_issue(self.id, number, **kwargs)
        return github.Issue._from_data(data, http=self._http)

    async def fetch_issue_or_pull(
        self,
        number: int,
        /,
        **kwargs,  # TODO
    ) -> Issue | Pull:
        """
        |coro|

        Fetches an issue or a pull request in the repository.


        Parameters
        ----------
        number: :class:`int`
            The number of the issue or pull request.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Issue` | :class:`~github.Pull`
        """

        data = await self._http.fetch_repository_issue_or_pull(self.id, number, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Issue":
            return github.Issue._from_data(data, http=self._http)
        elif data["__typename"] == "PullRequest":
            return github.Pull._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"invalid type {data['__typename']} for Repository.issueOrPullRequest")

    async def fetch_label(
        self,
        name: str,
        /,
        **kwargs,  # TODO
    ) -> Label:
        """
        |coro|

        Fetches a label in the repository.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Label`
        """

        data = await self._http.fetch_repository_label(self.id, name, **kwargs)
        return github.Label._from_data(data, http=self._http)

    async def fetch_latest_release(
        self,
        /,
        **kwargs,  # TODO
    ) -> Release | None:
        """
        |coro|

        Fetches the latest release in the repository, if there are is
        one.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Release` | None
        """

        data = await self._http.fetch_repository_latest_release(self.id, **kwargs)

        if data is None:
            return None

        return github.Release._from_data(data, http=self._http)

    async def fetch_license(
        self,
        /,
        **kwargs,  # TODO
    ) -> License | None:
        """
        |coro|

        Fetches the license for the repository, if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.License` | None
        """

        data = await self._http.fetch_repository_license(self.id, **kwargs)

        if data is None:
            return None

        return github.License._from_data(data, http=self._http)

    async def fetch_milestone(
        self,
        number: int,
        /,
        **kwargs,  # TODO
    ) -> Milestone:
        """
        |coro|

        Fetches a milestone in the repository.


        Parameters
        ----------
        number: :class:`int`
            The number of the milestone.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Milestone`
        """

        data = await self._http.fetch_repository_milestone(self.id, number, **kwargs)
        return github.Milestone._from_data(data, http=self._http)

    async def fetch_owner(
        self,
        /,
        **kwargs,  # TODO
    ) -> Organization | User:
        """
        |coro|

        Fetches the owner of the repository.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Organization` | :class:`~github.User`
        """

        data = await self._http.fetch_repository_owner(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Organization":
            return github.Organization._from_data(data, http=self._http)
        elif data["__typename"] == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"invalid type {data['__typename']} for Repository.owner")

    async def fetch_parent(
        self,
        /,
        **kwargs,  # TODO
    ) -> Repository | None:
        """
        |coro|

        Fetches the parent of the repository, if it is a fork.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Repository` | None
        """

        data = await self._http.fetch_repository_parent(self.id, **kwargs)

        if data is None:
            return None

        return github.Repository._from_data(data, http=self._http)

    async def fetch_pull(
        self,
        number: int,
        /,
        **kwargs,  # TODO
    ) -> Pull:
        """
        |coro|

        Fetches a pull request in the repository.


        Parameters
        ----------
        number: :class:`int`
            The number of the pull request.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Pull`
        """

        data = await self._http.fetch_repository_pull(self.id, number, **kwargs)
        return github.Pull._from_data(data, http=self._http)

    async def fetch_reference(
        self,
        name: str,
        /,
        **kwargs,  # TODO
    ) -> Reference:
        """
        |coro|

        Fetches an issue in the repository.


        Parameters
        ----------
        name: :class:`str`
            The qualified name of the reference.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Reference`
        """

        data = await self._http.fetch_repository_reference(self.id, name, **kwargs)
        return github.Reference._from_data(data, http=self._http)

    async def fetch_release(
        self,
        /,
        tag: Tag,
        **kwargs,  # TODO
    ) -> Release:
        """
        |coro|

        Fetches a release in the repository.


        Parameters
        ----------

        tag: :class:`~github.Tag`
            The tag associated with the release.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Release`
        """

        data = await self._http.fetch_repository_release(self.id, tag.name, **kwargs)
        return github.Release._from_data(data, http=self._http)

    async def fetch_template(
        self,
        /,
        **kwargs,  # TODO
    ) -> Repository | None:
        """
        |coro|

        Fetches the template the repository used, if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Repository` | None
        """

        data = await self._http.fetch_repository_template(self.id, **kwargs)

        if data is None:
            return None

        return github.Repository._from_data(data, http=self._http)

    def fetch_assignable_users(
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

        Fetches assignable users from the repository.


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


        :rtype: :class:`~github.connection.Connection`[:class:`~github.User`]
        """

        return github.Connection(
            self._http.collect_repository_assignable_users,
            self.id,
            data_map=lambda d: github.User._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_collaborators(
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

        Fetches collaborators from the repository.

        .. note::

            This query requires the following token scopes:

            - ``public_repo``


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


        :rtype: :class:`~github.connection.Connection`[:class:`~github.User`]
        """

        return github.Connection(
            self._http.collect_repository_collaborators,
            self.id,
            data_map=lambda d: github.User._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_discussions(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: DiscussionOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Discussion]:
        """
        |aiter|

        Fetches discussions in the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.DiscussionOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Discussion`]
        """

        return github.Connection(
            self._http.collect_repository_discussions,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Discussion._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_forks(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: RepositoryOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Repository]:
        """
        |aiter|

        Fetches forks of the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.RepositoryOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.connection.Connection`[:class:`~github.Repository`]
        """

        return github.Connection(
            self._http.collect_repository_forks,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Repository._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_issues(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: IssueOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Issue]:
        """
        |aiter|

        Fetches issues in the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.IssueOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Issue`]
        """

        return github.Connection(
            self._http.collect_repository_issues,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Issue._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_labels(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: LabelOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Label]:
        """
        |aiter|

        Fetches labels in the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.LabelOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.connection.Connection`[:class:`~github.Label`]
        """

        return github.Connection(
            self._http.collect_repository_labels,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Label._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_mentionable_users(
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

        Fetches mentionable users from the repository.


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


        :rtype: :class:`~github.connection.Connection`[:class:`~github.User`]
        """

        return github.Connection(
            self._http.collect_repository_mentionable_users,
            self.id,
            data_map=lambda d: github.User._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_milestones(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: MilestoneOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Milestone]:
        """
        |aiter|

        Fetches milestones in the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.MilestoneOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Milestone`]
        """

        return github.Connection(
            self._http.collect_repository_milestones,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Milestone._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

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

        Fetches pull requests in the repository.


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
            self._http.collect_repository_pulls,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Pull._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    if TYPE_CHECKING:

        @overload  # NOTE: ()
        def fetch_references(
            self,
            /,
            *,
            cursor: str | None = MISSING,
            limit: int = MISSING,
            order_by: ReferenceOrder = MISSING,
            reverse: bool = MISSING,
            **kwargs,  # TODO
        ) -> Connection[Reference]:
            ...

        @overload  # NOTE: (prefix="refs/heads/")
        def fetch_references(
            self,
            /,
            *,
            cursor: str | None = MISSING,
            limit: int = MISSING,
            order_by: ReferenceOrder = MISSING,
            prefix: str,
            reverse: bool = MISSING,
            **kwargs,  # TODO
        ) -> Connection[Reference]:
            ...

        @overload  # NOTE: (type=ReferenceType.head)
        def fetch_references(
            self,
            /,
            *,
            cursor: str | None = MISSING,
            limit: int = MISSING,
            order_by: ReferenceOrder = MISSING,
            reverse: bool = MISSING,
            type: ReferenceType,
            **kwargs,  # TODO
        ) -> Connection[Reference]:
            ...

    def fetch_references(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: ReferenceOrder = MISSING,
        prefix: str = MISSING,
        reverse: bool = MISSING,
        type: ReferenceType = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Reference]:
        """
        |aiter|

        Fetches references in the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.ReferenceOrder`
            The field by which to order the elements.
        prefix: :class:`str`
            The Git reference prefix, eg. "refs/heads/".
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.
        type: :class:`~github.ReferenceType`
            The Git reference type, eg. ReferenceType.head.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Reference`]
        """

        if type is not MISSING:
            if prefix is not MISSING:
                raise RuntimeError

            prefix = type.value
        elif prefix is MISSING:
            prefix = "refs/"

        return github.Connection(
            self._http.collect_repository_references,
            self.id,
            prefix,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Reference._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_releases(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: ReleaseOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Release]:
        """
        |aiter|

        Fetches releases in the repository.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.ReleaseOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Release`]
        """

        return github.Connection(
            self._http.collect_repository_releases,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Release._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_topics(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Topic]:
        """
        |aiter|

        Fetches topics from the repository.


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


        :rtype: :class:`~github.connection.Connection`[:class:`~github.Topic`]
        """

        return github.Connection(
            self._http.collect_repository_topics,
            self.id,
            data_map=lambda d: github.Topic._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_watchers(
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

        Fetches watchers of the repository.


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


        :rtype: :class:`~github.connection.Connection`[:class:`~github.User`]
        """

        return github.Connection(
            self._http.collect_repository_watchers,
            self.id,
            data_map=lambda d: github.User._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    async def archive(
        self,
        /,
    ) -> None:
        """
        |coro|

        Archives the repository.


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.is_archived`
        """

        data = await self._http.mutate_repository_archive(self.id, fields=("isArchived",))

        self._data["isArchived"] = data["isArchived"]

    async def create_label(
        self,
        /,
        name: str,
        *,
        color: int = MISSING,
        description: str = MISSING,
        fields = MISSING,  # TODO
    ) -> Label:
        """
        |coro|

        Creates a label on the repository.


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.label_count`


        Parameters
        ----------
        name: :class:`str`
            The name of the label.
        color: :class:`int`
            The color of the label. Defaults to a random value,
            generated using the same method as the GitHub UI.
        description: :class:`str`
            The description of the label.


        :rtype: :class:`~github.Label`
        """

        if color is MISSING:
            # NOTE: generated using the same method as the GitHub UI.
            #       yes, randomRGBColor is 0-254 for no reason.
            r, g, b = (random.randint(0, 254) for _ in range(3))
            color = (r << 16) + (g << 8) + b

        color_string = f"{color:06x}"

        repository_data, label_data = await self._http.mutate_repository_create_label(
            self.id,
            name,
            color_string,
            description if description is not MISSING else None,
            label_fields=fields,
            repository_fields=("labels{totalCount}",),
        )

        if "labels" not in self._data.keys():
            self._data["labels"] = dict()  # type: ignore

        self._data["labels"]["totalCount"] = repository_data["labels"]["totalCount"]

        return github.Label._from_data(label_data, http=self._http)

    async def unarchive(
        self,
        /,
    ) -> None:
        """
        |coro|

        Unarchives the repository.


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.is_archived`
        """

        data = await self._http.mutate_repository_unarchive(self.id, fields=("isArchived",))

        self._data["isArchived"] = data["isArchived"]


__all__ = [
    "Repository",
]
