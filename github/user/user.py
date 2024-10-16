from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.organization import Organization
    from github.user import UserStatus
    from github.utility.types import DateTime

import github
from github.interfaces import Actor, DiscussionAuthor, Node, PackageOwner, ProfileOwner, RepositoryOwner, Resource, Sponsorable, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connections.connection import ConnectionData
    from github.interfaces.actor import ActorData
    from github.interfaces.discussionauthor import DiscussionAuthorData
    from github.interfaces.node import NodeData
    from github.interfaces.packageowner import PackageOwnerData
    from github.interfaces.profileowner import ProfileOwnerData
    # from github.interfaces.projectowner import ProjectOwnerData  # TODO (support-projects): GitHub Projects support
    from github.interfaces.repositoryowner import RepositoryOwnerData
    from github.interfaces.resource import ResourceData
    from github.interfaces.sponsorable import SponsorableData
    from github.interfaces.type import TypeData


    class OptionalUserData(TypedDict, total=False):
        # commitComments  # TODO
        # contributionsCollection  # TODO
        # copilotEndpoints  # TODO
        # enterprises  # TODO
        # gistComments  # TODO
        # gists  # TODO
        # issueComments  # TODO
        # issues  # TODO
        # lists  # TODO
        # organizations  # TODO
        # publicKeys  # TODO
        # pullRequests  # TODO
        # repositoriesContributedTo  # TODO
        # savedReplies  # TODO
        # socialAccounts  # TODO
        # sponsoring  # TODO
        # starredRepositories  # TODO
        # topRepositories  # TODO
        # watching  # TODO
        pass

    class UserData(
        OptionalUserData,
        ActorData,
        DiscussionAuthorData,
        NodeData,
        PackageOwnerData,
        ProfileOwnerData,
        # ProjectOwnerData,  # TODO (support-projects): GitHub Projects support
        RepositoryOwnerData,
        ResourceData,
        SponsorableData,
        TypeData,
    ):
        bio: str | None
        bioHTML: str | None
        company: str | None
        companyHTML: str | None
        createdAt: str
        databaseId: int
        followers: ConnectionData[UserData]
        following: ConnectionData[UserData]
        isBountyHunter: bool
        isCampusExpert: bool
        isDeveloperProgramMember: bool
        isEmployee: bool
        isFollowingViewer: bool
        isGitHubStar: bool
        isHireable: bool
        isSiteAdmin: bool
        isViewer: bool
        pronouns: str | None
        twitterUsername: str | None
        updatedAt: str
        viewerCanFollow: bool
        viewerIsFollowing: bool


class User(
    Actor,
    DiscussionAuthor,
    Node,
    PackageOwner,
    ProfileOwner,
    # ProjectOwner,  # TODO (support-projects): GitHub Projects support
    RepositoryOwner,
    Sponsorable,
    Type,
    Resource,
):
    """
    Represents a GitHub user.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: UserData

    _graphql_fields: dict[str, str] = {
        "bio": "bio",
        "bio_html": "bioHTML",
        "can_viewer_follow": "viewerCanFollow",
        "company": "company",
        "company_html": "companyHTML",
        "created_at": "createdAt",
        "database_id": "databaseId",
        "follower_count": "followers{totalCount}",
        "following_count": "following{totalCount}",
        # "is_administrator": "isSiteAdmin",
        "is_bounty_program_member": "isBountyHunter",
        "is_campus_program_member": "isCampusExpert",
        "is_developer_program_member": "isDeveloperProgramMember",
        "is_employee": "isEmployee",
        "is_following_viewer": "isFollowingViewer",
        "is_stars_program_member": "isGitHubStar",
        "is_hireable": "isHireable",
        "is_viewer": "isViewer",
        "is_viewer_following": "viewerIsFollowing",
        "pronouns": "pronouns",
        # "twitter_username": "twitterUsername",  # NOTE: see User.twitter_username
        "updated_at": "updatedAt",
    }

    _node_prefix: str = "U"

    if not TYPE_CHECKING:

        @classmethod
        def _from_data(cls, data, /, *, http=None):
            if isinstance(data, dict):
                if not data.get("isViewer", None):
                    return cls(data, http)
                else:
                    return AuthenticatedUser(data, http)
            else:
                return [cls._from_data(o, http=http) for o in data]

    @property
    def bio(
        self: Self,
        /,
    ) -> str | None:
        """
        The bio of the user.

        :type: Optional[:class:`str`]
        """

        return self._data["bio"]

    @property
    def bio_html(
        self: Self,
        /,
    ) -> str | None:
        """
        The bio of the user as HTML.

        This variant of :attr:`~github.User.bio` does the following:

        - Replaces ``:name:`` in the string with emoji.
        - Sanitizes the string such that it cannot contain HTML tags.
        - Wraps the string in ``<div>`` tags.

        :type: Optional[:class:`str`]
        """

        return self._data["bioHTML"]

    @property
    def can_viewer_follow(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can follow the user.

        :type: :class:`bool`
        """

        return self._data["viewerCanFollow"]

    @property
    def company(
        self: Self,
        /,
    ) -> str | None:
        """
        The company of the user.

        :type: Optional[:class:`str`]
        """

        return self._data["company"]

    @property
    def company_html(
        self: Self,
        /,
    ) -> str | None:
        """
        The company of the user as HTML.

        This variant of :attr:`~github.User.company` does the
        following:

        - Replaces ``:name:`` in the string with emoji.
        - Sanitizes the string such that it cannot contain HTML tags.
        - Wraps the string in ``<div>`` tags.

        :type: Optional[:class:`str`]
        """

        return self._data["companyHTML"]

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the user was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the user.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def follower_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of users following the user.

        :type: :class:`int`
        """

        return self._data["followers"]["totalCount"]

    @property
    def following_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of users the user is following.

        :type: :class:`int`
        """

        return self._data["following"]["totalCount"]

    @property
    def is_administrator(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is an administrator of this GitHub instance.

        .. note::

            This field is not requested by default. It will always be
            ``False`` on this branch. See TODO.

        :type: :class:`bool`
        """

        return self._data["isSiteAdmin"]

    @property
    def is_bounty_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is a member of GitHub's Bug Bounty Program.

        :type: :class:`bool`
        """

        return self._data["isBountyHunter"]

    @property
    def is_campus_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is a member of GitHub's Campus Experts Program.

        :type: :class:`bool`
        """

        return self._data["isCampusExpert"]

    @property
    def is_developer_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is a member of GitHub's Developer Program.

        :type: :class:`bool`
        """

        return self._data["isDeveloperProgramMember"]

    @property
    def is_employee(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is a GitHub employee.

        :type: :class:`bool`
        """

        return self._data["isEmployee"]

    @property
    def is_following_viewer(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is following the authenticated user.

        :type: :class:`bool`
        """

        return self._data["isFollowingViewer"]

    @property
    def is_hireable(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is a hireable.

        :type: :class:`bool`
        """

        return self._data["isHireable"]

    @property
    def is_stars_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is a member of GitHub's Stars Program.

        :type: :class:`bool`
        """

        return self._data["isGitHubStar"]

    @property
    def is_viewer(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the user is the authenticated user.

        .. seealso::

            :class:`~github.AuthenticatedUser`

        :type: :class:`bool`
        """

        return self._data["isViewer"]

    @property
    def is_viewer_following(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user is following the user.

        :type: :class:`bool`
        """

        return self._data["viewerIsFollowing"]

    @property
    def pronouns(
        self: Self,
        /,
    ) -> str | None:
        """
        The pronouns of the user.

        :type: Optional[:class:`str`]
        """

        return self._data["pronouns"]

    @property
    def twitter_username(
        self: Self,
        /,
    ) -> str | None:
        """
        The Twitter username of the user.

        .. note::

            This field is not requested by default. You should access
            this value via :meth:`~github.User.fetch_social_accounts`
            instead.

        :type: Optional[:class:`str`]
        """

        return self._data["twitterUsername"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the user was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_bio(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the bio of the user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("bio")  # type: ignore

    async def fetch_bio_html(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the bio of the user as HTML.

        This variant of :attr:`~github.User.bio` does the following:

        - Replaces ``:name:`` in the string with emoji.
        - Sanitizes the string such that it cannot contain HTML tags.
        - Wraps the string in ``<div>`` tags.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("bioHTML")  # type: ignore

    async def fetch_can_viewer_follow(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can follow the user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanFollow")  # type: ignore

    async def fetch_company(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the company of the user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("company")  # type: ignore

    async def fetch_company_html(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the company of the user as HTML.

        This variant of :attr:`~github.User.company` does the
        following:

        - Replaces ``:name:`` in the string with emoji.
        - Sanitizes the string such that it cannot contain HTML tags.
        - Wraps the string in ``<div>`` tags.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("companyHTML")  # type: ignore

    async def fetch_created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the user was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        value = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            value = cast(str, value)

        return github.utility.iso_to_datetime(value)

    async def fetch_database_id(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_is_administrator(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is an administrator of this GitHub
        instance.

        .. note::

            This field will always be ``False`` on this branch. See
            TODO.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isSiteAdmin")  # type: ignore

    async def fetch_is_bounty_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is a member of GitHub's Bug Bounty
        Program.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isBountyHunter")  # type: ignore

    async def fetch_is_campus_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is a member of GitHub's Campus Experts
        Program.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isCampusExpert")  # type: ignore

    async def fetch_is_developer_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is a member of GitHub's Developer
        Program.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isDeveloperProgramMember")  # type: ignore

    async def fetch_is_employee(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is a GitHub employee.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isEmployee")  # type: ignore

    async def fetch_is_following_viewer(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is following the authenticated user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isFollowingViewer")  # type: ignore

    async def fetch_is_stars_program_member(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is a member of the GitHub Stars
        Program.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isGitHubStar")  # type: ignore

    async def fetch_is_hireable(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is hireable.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isHireable")  # type: ignore

    async def fetch_is_viewer(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the user is the authenticated user.

        .. seealso::

            :class:`~github.AuthenticatedUser`


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isViewer")  # type: ignore

    async def fetch_is_viewer_following(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user is following the user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerIsFollowing")  # type: ignore

    async def fetch_pronouns(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the pronouns of the user.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("pronouns")  # type: ignore

    async def fetch_twitter_username(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the pronouns of the user.

        .. note::

            Consider using :meth:`~github.User.fetch_social_accounts`
            instead.


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

        Fetches the date and time at which the user was last updated.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        value = await self._fetch_field("updatedAt")

        if TYPE_CHECKING:
            value = cast(str, value)

        return github.utility.iso_to_datetime(value)

    async def fetch_status(
        self: Self,
        /,
        **kwargs,  # TODO
    ) -> UserStatus | None:
        """
        |coro|

        Fetches the user's status.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.UserStatus`
        """

        data = await self._http.fetch_user_status(self.id, **kwargs)

        if data is None:
            return None

        return github.UserStatus._from_data(data, http=self._http)


class AuthenticatedUser(User):
    """
    Represents the authenticated GitHub user.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    async def clear_status(
        self: Self,
        /,
    ) -> None:
        """
        |coro|

        Clears the authenticated user's status.

        .. note::

            This mutation requires the following token scopes:

            - ``user``
        """

        await self._http.mutate_user_update_status(None, None, None, None, None)

    async def update_status(
        self: Self,
        /,
        message: str | None = MISSING,
        *,
        busy: bool = MISSING,
        emoji: str | None = MISSING,
        expires_at: DateTime = MISSING,
        organization: Organization = MISSING,
    ) -> UserStatus | None:
        """
        |coro|

        Updates the authenticated user's status.

        .. note::

            This mutation requires the following token scopes:

            - ``user``


        Parameters
        ----------
        message: Optional[:class:`str`]
            The message to display on the status.
        busy: :class:`bool`
            Whether to mark the user as busy.
        emoji: Optional[:class:`str`]
            The emoji to display on the status. This can either be a
            unicode emoji or its name with colons.
        expires_at: :class:`~datetime.datetime`
            The date and time at which to expire the status in UTC.
        organization: :class:`~github.Organization`
            The organization whose members will be allowed to see the
            status.


        :rtype: Optional[:class:`~github.UserStatus`]
        """

        data = await self._http.mutate_user_update_status(
            busy if busy is not MISSING else False,
            emoji if emoji is not MISSING else None,
            github.utility.datetime_to_iso(expires_at) if expires_at is not MISSING else None,
            message if message is not MISSING else None,
            organization.id if organization is not MISSING else None,
        )

        if not data:
            return None

        return github.UserStatus._from_data(data, http=self._http)


__all__: list[str] = [
    "User",
    "AuthenticatedUser",
]
