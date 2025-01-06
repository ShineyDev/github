from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.utility.types import DateTime

import github
from github.interfaces import Node, Subscribable, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.interfaces.node import NodeData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.type import TypeData
    from github.organization.organization import OrganizationData
    from github.repository.repository import RepositoryData
    from github.user.user import UserData


    class TeamData(
        # MemberStatusableData,  # TODO
        NodeData,
        # ProjectOwnerData,  # TODO
        SubscribableData,
        TypeData,
    ):
        ancestors: ConnectionData[TeamData]
        avatarUrl: str
        childTeams: ConnectionData[TeamData]
        combinedSlug: str
        createdAt: str
        databaseId: int
        description: str | None
        # discussion  # TODO
        # discussions  # TODO
        discussionsResourcePath: str
        discussionsUrl: str
        editTeamResourcePath: str
        editTeamUrl: str
        # invitations  # TODO
        members: ConnectionData[UserData]
        membersResourcePath: str
        membersUrl: str
        name: str
        newTeamResourcePath: str
        newTeamUrl: str
        notificationSetting: Literal["NOTIFICATIONS_DISABLED", "NOTIFICATIONS_ENABLED"]
        organization: OrganizationData
        parentTeam: TeamData | None
        privacy: Literal["SECRET", "VISIBLE"]
        repositories: ConnectionData[RepositoryData]
        repositoriesResourcePath: str
        repositoriesUrl: str
        reviewRequestDelegationAlgorithm: Literal["LOAD_BALANCE", "ROUND_ROBIN"] | None
        reviewRequestDelegationEnabled: bool
        reviewRequestDelegationMemberCount: int | None
        reviewRequestDelegationNotifyTeam: bool
        slug: str
        teamsResourcePath: str
        teamsUrl: str
        updatedAt: str
        viewerCanAdminister: bool


class Team(
    # MemberStatusable,  # TODO
    Node,
    # ProjectOwner,  # TODO
    Subscribable,
    Type,
):
    """
    Represents a team.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: TeamData

    _graphql_fields: dict[str, str] = {
        "avatar_url": "avatarUrl",
        # "": "combinedSlug",  # TODO: name
        "created_at": "createdAt",
        "database_id": "databaseId",
        "description": "description",
        # "": "discussionsResourcePath",  # TODO: name
        # "": "discussionsUrl",  # TODO: name
        # "": "editTeamResourcePath",  # TODO: name
        # "": "editTeamUrl",  # TODO: name
        # "": "membersResourcePath",  # TODO: name
        # "": "membersUrl",  # TODO: name
        "name": "name",
        # "": "newTeamResourcePath",  # TODO: name
        # "": "newTeamUrl",  # TODO: name
        # "": "notificationSetting",  # TODO: name, type
        # "privacy": "privacy",  # TODO: type
        # "": "repositoriesResourcePath",  # TODO: name
        # "": "repositoriesUrl",  # TODO: name
        # "": "reviewRequestDelegationAlgorithm",  # TODO: name, type
        # "": "reviewRequestDelegationEnabled",  # TODO: name
        # "": "reviewRequestDelegationMemberCount",  # TODO: name
        # "": "reviewRequestDelegationNotifyTeam",  # TODO: name
        "slug": "slug",
        # "": "teamsResourcePath",  # TODO: name
        # "": "teamsUrl",  # TODO: name
        "updated_at": "updatedAt",
        "viewer_can_administer": "viewerCanAdminister",
    }

    _node_prefix: str = "T"

    @property
    def avatar_url(
        self: Self,
        /,
    ) -> str:
        """
        A URL to the avatar of the team.

        :type: :class:`str`
        """

        return self._data["avatarUrl"]

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the team was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the team.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def description(
        self: Self,
        /,
    ) -> str | None:
        """
        The description of the team.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def name(
        self: Self,
        /,
    ) -> str:
        """
        The name of the team.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def slug(
        self: Self,
        /,
    ) -> str:
        """
        The slug of the team.

        :type: :class:`str`
        """

        return self._data["slug"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the team was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    @property
    def viewer_can_administer(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can administer the team.

        :type: :class:`bool`
        """

        return self._data["viewerCanAdminister"]

    async def fetch_avatar_url(
        self: Self,
        /,
        *,
        size: int = MISSING,
    ) -> str:
        """
        |coro|

        Fetches a URL to the avatar of the team.


        Parameters
        ----------

        size: :class:`int`
            The width of the square image in pixels.


        :rtype: :class:`str`
        """

        if size is MISSING:
            field = f"avatarUrl(size:{size})"
            save = False
        else:
            field = "avatarUrl"
            save = True

        return await self._fetch_field(field, save=save)  # type: ignore

    async def fetch_created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the team was created.


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

        Fetches the database ID of the team.


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

        Fetches the description of the team.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_name(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the team.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_slug(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the slug of the team.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("slug")  # type: ignore

    async def fetch_updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the team was last updated.


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

    async def fetch_viewer_can_administer(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can administer the team.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanAdminister")  # type: ignore


__all__ = [
    "Team",
]
