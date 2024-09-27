from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.utility.types import DateTime

import github
from github.interfaces import Actor, AnnouncementOwner, DiscussionAuthor, Node, PackageOwner, ProfileOwner, RepositoryOwner, Resource, Sponsorable, Type


if TYPE_CHECKING:
    from typing import TypedDict

    from github.interfaces.actor import ActorData
    from github.interfaces.announcementowner import AnnouncementOwnerData
    from github.interfaces.discussionauthor import DiscussionAuthorData
    from github.interfaces.node import NodeData
    from github.interfaces.packageowner import PackageOwnerData
    from github.interfaces.profileowner import ProfileOwnerData
    from github.interfaces.repositoryowner import RepositoryOwnerData
    from github.interfaces.resource import ResourceData
    from github.interfaces.sponsorable import SponsorableData
    from github.interfaces.type import TypeData


    class OptionalOrganizationData(TypedDict, total=False):
        pass


    class OrganizationData(
        OptionalOrganizationData,
        ActorData,
        AnnouncementOwnerData,
        DiscussionAuthorData,
        # MemberStausableData,  # TODO
        NodeData,
        PackageOwnerData,
        ProfileOwnerData,
        # ProjectOwnerData,  # TODO
        RepositoryOwnerData,
        ResourceData,
        SponsorableData,
        TypeData,
    ):
        archivedAt: str | None
        createdAt: str
        databaseId: int
        description: str | None
        descriptionHTML: str | None
        # ipAllowListEnabledSetting
        # ipAllowListForInstalledAppsEnabledSetting
        isVerified: bool
        # membersCanForkPrivateRepositories
        # newTeamResourcePath
        # newTeamUrl
        # notificationDeliveryRestrictionEnabledSetting
        # requiresTwoFactorAuthentication
        # teamsResourcePath
        # teamsUrl
        twitterUsername: str | None
        updatedAt: str
        viewerCanAdminister: bool
        viewerCanCreateTeams: bool
        viewerIsAMember: bool
        viewerIsFollowing: bool


class Organization(
    Actor,
    AnnouncementOwner,
    DiscussionAuthor,
    # MemberStatusable,  # TODO
    Node,
    PackageOwner,
    ProfileOwner,
    # ProjectOwner,  # TODO
    RepositoryOwner,
    Resource,
    Sponsorable,
    Type,
):
    """
    Represents a GitHub organization.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: OrganizationData

    _graphql_fields: dict[str, str] = {
        "archived_at": "archivedAt",
        "can_viewer_administer": "viewerCanAdminister",
        "can_viewer_create_teams": "viewerCanCreateTeams",
        "created_at": "createdAt",
        "database_id": "databaseId",
        "description": "description",
        "description_html": "descriptionHTML",
        "is_verified": "isVerified",
        "is_viewer_following": "viewerIsFollowing",
        "is_viewer_member": "viewerIsAMember",
        "twitter_username": "twitterUsername",
        "updated_at": "updatedAt",
    }

    _node_prefix: str = "O"

    @property
    def archived_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the organization was archived.

        :type: Optional[:class:`~datetime.datetime`]
        """

        archived_at = self._data["archivedAt"]

        if archived_at is None:
            return None

        return github.utility.iso_to_datetime(archived_at)

    @property
    def can_viewer_administer(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can administer the organization.

        :type: :class:`bool`
        """

        return self._data["viewerCanAdminister"]

    @property
    def can_viewer_create_teams(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can create new teams in this
        organization.

        :type: :class:`bool`
        """

        return self._data["viewerCanCreateTeams"]

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the organization was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the organization.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def description(
        self: Self,
        /,
    ) -> str | None:
        """
        The description of the organization.

        :type: Optional[:class:`str`]
        """

        return self._data["description"]

    @property
    def description_html(
        self: Self,
        /,
    ) -> str | None:
        """
        The description of the organization as HTML.

        This variant of :attr:`~github.Organization.description` does
        the following:

        - Replaces ``:name:`` in the string with emoji.
        - Sanitizes the string such that it cannot contain HTML tags.
        - Wraps the string in ``<div>`` tags.

        :type: Optional[:class:`str`]
        """

        return self._data["descriptionHTML"]

    @property
    def is_verified(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the organization has verified its domain and email.

        :type: :class:`bool`
        """

        return self._data["isVerified"]

    @property
    def is_viewer_following(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user is following the organization.

        :type: :class:`bool`
        """

        return self._data["viewerIsFollowing"]

    @property
    def is_viewer_member(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user is a member of the organization.

        :type: :class:`bool`
        """

        return self._data["viewerIsAMember"]

    @property
    def twitter_username(
        self: Self,
        /,
    ) -> str | None:
        """
        The Twitter username of the organization.

        :type: Optional[:class:`str`]
        """

        return self._data["twitterUsername"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the organization was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_archived_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the organization was
        archived.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`~datetime.datetime`]
        """

        archived_at = await self._fetch_field("archivedAt")

        if archived_at is None:
            return None

        if TYPE_CHECKING:
            archived_at = cast(str, archived_at)

        return github.utility.iso_to_datetime(archived_at)

    async def fetch_can_viewer_administer(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can administer the
        organization.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanAdminister")  # type: ignore

    async def fetch_can_viewer_create_teams(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can create new teams in
        the organization.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanCreateTeams")  # type: ignore

    async def fetch_created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the organization was
        created.


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

        Fetches the database ID of the organization.


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

        Fetches the description of the organization.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_description_html(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the description of the organization as HTML.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("descriptionHTML")  # type: ignore

    async def fetch_is_verified(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the organization has verified its domain and
        email.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isVerified")  # type: ignore

    async def fetch_is_viewer_following(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user is following the
        organization.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerIsFollowing")  # type: ignore

    async def fetch_is_viewer_member(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user is a member of the
        organization.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerIsAMember")  # type: ignore

    async def fetch_twitter_username(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the Twitter username of the organization


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("twitterUsername")  # type: ignore

    async def fetch_updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the organization was last
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


__all__ = [
    "Organization",
]
