from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal, cast
    from typing_extensions import Self

    from github.connection import Connection, DiscussionOrder, IssueOrder, LabelOrder, RepositoryOrder
    from github.content import CodeOfConduct, License
    from github.organization import Organization
    from github.repository import Discussion, Issue, Label, Topic
    from github.repository.discussion import DiscussionData
    from github.repository.issue import IssueData
    from github.user import User
    from github.utility.types import DateTime

import github
from github.interfaces import Node, PackageOwner, Starrable, Subscribable, Resource, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.content.codeofconduct import CodeOfConductData
    from github.content.license import LicenseData
    from github.interfaces.node import NodeData
    from github.interfaces.packageowner import PackageOwnerData
    from github.interfaces.starrable import StarrableData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.resource import ResourceData
    from github.interfaces.type import TypeData
    from github.organization.organization import OrganizationData
    from github.repository.label import LabelData
    from github.repository.topic import TopicData
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
        # defaultBranchRef  # TODO
        deleteBranchOnMerge: bool
        # dependencyGraphManifests  # TODO
        # deployKeys  # TODO
        # deployments  # TODO
        description: str | None
        descriptionHTML: str | None
        # discussion  # TODO
        # discussionCategories  # TODO
        # discussionCategory  # TODO
        # discussions  # TODO
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
        # issue  # TODO
        # issueOrPullRequest  # TODO
        # issueTemplates  # TODO
        # issues  # TODO
        label: LabelData
        labels: ConnectionData[LabelData]
        # languages  # TODO
        # latestRelease  # TODO
        licenseInfo: LicenseData | None
        # lockReason  # TODO
        mentionableUsers: ConnectionData[UserData]
        mergeCommitAllowed: bool
        mergeCommitMessage: Literal["BLANK", "PR_BODY", "PR_TITLE"]
        mergeCommitTitle: Literal["MERGE_MESSAGE", "PR_TITLE"]
        # mergeQueue  # TODO
        # milestone  # TODO
        # milestones  # TODO
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
        # pullRequest  # TODO
        # pullRequestTemplates  # TODO
        # pullRequests  # TODO
        pushedAt: str | None
        rebaseMergeAllowed: bool
        # ref  # TODO
        # refs  # TODO
        # release  # TODO
        # releases  # TODO
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
        # vulnerabilityAlert  # TODO
        # vulnerabilityAlerts  # TODO
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

    _repr_fields: list[str] = [
        "name",
    ]

    _graphql_fields: dict[str, str] = {
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
        # "visibility": "visibility",  # TODO: type
        # "": "webCommitSignoffRequired",  # TODO: name
    }

    _node_prefix: str = "R"

    @property
    def allows_fork(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository allows forks of itself to be created.

        :type: :class:`bool`
        """

        return self._data["forkingAllowed"]

    @property
    def allows_merge(
        self: Self,
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
        self: Self,
        /,
    ) -> bool:
        """
        TODO.

        :type: :class:`bool`
        """

        return self._data["squashMergeAllowed"]

    @property
    def allows_squash(
        self: Self,
        /,
    ) -> bool:
        """
        TODO.

        :type: :class:`bool`
        """

        return self._data["rebaseMergeAllowed"]

    @property
    def archived_at(
        self: Self,
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
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the repository was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the repository.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def description(
        self: Self,
        /,
    ) -> str | None:
        """
        The description of the repository.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def description_html(
        self: Self,
        /,
    ) -> str | None:
        """
        The description of the repository as HTML.

        :type: :class:`str` | None
        """

        return self._data["descriptionHTML"]

    @property
    def disk_usage(  # TODO: KB or KiB  # TODO: rounding
        self: Self,
        /,
    ) -> int:
        """
        The number of kilobytes the repository occupies on disk.

        :type: :class:`int`
        """

        return self._data["diskUsage"]

    @property
    def fork_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of forks the repository has.

        :type: :class:`int`
        """

        return self._data["forkCount"]

    @property
    def has_discussions_enabled(
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository has wiki enabled.

        :type: :class:`bool`
        """

        return self._data["hasWikiEnabled"]

    @property
    def is_archived(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is archived.

        :type: :class:`bool`
        """

        return self._data["isArchived"]

    @property
    def is_disabled(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is disabled.

        :type: :class:`bool`
        """

        return self._data["isDisabled"]

    @property
    def is_empty(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is empty.

        :type: :class:`bool`
        """

        return self._data["isEmpty"]

    @property
    def is_fork(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is a fork of another.

        :type: :class:`bool`
        """

        return self._data["isFork"]

    @property
    def is_locked(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is locked.

        :type: :class:`bool`
        """

        return self._data["isLocked"]

    @property
    def is_mirror(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is a mirror of another.

        :type: :class:`bool`
        """

        return self._data["isMirror"]

    @property
    def is_private(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is private.

        :type: :class:`bool`
        """

        return self._data["isPrivate"]

    @property
    def is_template(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the repository is a template.

        :type: :class:`bool`
        """

        return self._data["isTemplate"]

    @property
    def name(
        self: Self,
        /,
    ) -> str:
        """
        The name of the repository.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def pushed_at(
        self: Self,
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
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the repository was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_allows_fork(
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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

    async def fetch_code_of_conduct(
        self: Self,
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
        self: Self,
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
        self: Self,
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

    async def fetch_label(
        self: Self,
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

    async def fetch_license(
        self: Self,
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

    async def fetch_owner(
        self: Self,
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

        graphql_type = data["__typename"]

        if graphql_type == "Organization":
            return github.Organization._from_data(data, http=self._http)
        elif graphql_type == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"invalid type {graphql_type} for Repository.owner")

    async def fetch_parent(
        self: Self,
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

    async def fetch_template(
        self: Self,
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

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_repository_assignable_users,
            self.id,
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_collaborators(
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

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_repository_collaborators,
            self.id,
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_discussions(
        self: Self,
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

        def discussiondata_to_discussion(discussiondata: DiscussionData, /) -> Discussion:
            return github.Discussion._from_data(discussiondata, http=self._http)

        return github.Connection(
            self._http.collect_repository_discussions,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=discussiondata_to_discussion,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_forks(
        self: Self,
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

        def repositorydata_to_repository(repositorydata: RepositoryData, /) -> Repository:
            return github.Repository._from_data(repositorydata, http=self._http)

        return github.Connection(
            self._http.collect_repository_forks,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=repositorydata_to_repository,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_issues(
        self: Self,
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

        def issuedata_to_issue(issuedata: IssueData, /) -> Issue:
            return github.Issue._from_data(issuedata, http=self._http)

        return github.Connection(
            self._http.collect_repository_issues,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=issuedata_to_issue,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_labels(
        self: Self,
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

        def labeldata_to_label(labeldata: LabelData, /) -> Label:
            return github.Label._from_data(labeldata, http=self._http)

        return github.Connection(
            self._http.collect_repository_labels,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=labeldata_to_label,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_mentionable_users(
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

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_repository_mentionable_users,
            self.id,
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_topics(
        self: Self,
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

        def topicdata_to_topic(userdata: TopicData, /) -> Topic:
            return github.Topic._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_repository_topics,
            self.id,
            data_map=topicdata_to_topic,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_watchers(
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

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_repository_watchers,
            self.id,
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )


__all__: list[str] = [
    "Repository",
]
