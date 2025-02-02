from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypeVar, TypedDict

    from github.connection.connection import ConnectionData
    from github.content.gist import GistData
    from github.repository.repository import RepositoryData


    class _ProfileOwnerShowcaseData(TypedDict):
        hasPinnedItems: bool
        items: ConnectionData[GistData | RepositoryData]


    class ProfileOwnerData(TypedDict):
        anyPinnableItems: bool
        email: str | None
        # id: str  # NOTE: on Node
        itemShowcase: _ProfileOwnerShowcaseData
        location: str | None
        # login: str  # NOTE: on Actor
        name: str | None
        pinnableItems: ConnectionData[GistData | RepositoryData]
        pinnedItems: ConnectionData[GistData | RepositoryData]
        pinnedItemsRemaining: int
        viewerCanChangePinnedItems: bool
        websiteUrl: str | None


    _ProfileOwnerData_T_co = TypeVar("_ProfileOwnerData_T_co", bound=ProfileOwnerData, covariant=True)


class ProfileOwner:
    """
    Represents an object that can own a profile.
    """

    __slots__ = ()

    _data: ProfileOwnerData

    @staticmethod
    def _patch_data(
        data: _ProfileOwnerData_T_co,
        /,
    ) -> _ProfileOwnerData_T_co:
        if data.get("email", False) == "":
            data["email"] = None

        return data

    _graphql_fields = {
        "can_viewer_update_showcase": "viewerCanChangePinnedItems",
        # "email": "email",  # NOTE: see ProfileOwner.email
        "has_pinnable_items": "anyPinnableItems",
        "has_pinned_items": "itemShowcase{hasPinnedItems}",
        "location": "location",
        "name": "name",
        "showcase_slots_remaining": "pinnedItemsRemaining",
        "website": "websiteUrl",
    }

    @property
    def can_viewer_update_showcase(
        self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can update the showcase of the
        profile owner.

        :type: :class:`bool`
        """

        return self._data["viewerCanChangePinnedItems"]

    @property
    def email(
        self,
        /,
    ) -> str | None:
        """
        The email of the profile owner.

        .. note::

            This field is not requested by default. It requires the
            following token scopes:

            - ``read:org`` for :attr:`Organization.email`.
            - ``read:user`` OR ``user:email`` for :attr:`User.email`.

        :type: Optional[:class:`str`]
        """

        return self._data["email"]

    @property
    def has_pinnable_items(
        self,
        /,
    ) -> bool:
        """
        Whether the profile owner has any pinnable items.

        :type: :class:`bool`
        """

        return self._data["anyPinnableItems"]

    @property
    def has_pinned_items(
        self,
        /,
    ) -> bool:
        """
        Whether the profile owner has any pinned items.

        :type: :class:`bool`
        """

        return self._data["itemShowcase"]["hasPinnedItems"]

    @property
    def location(
        self,
        /,
    ) -> str | None:
        """
        The location of the profile owner.

        :type: Optional[:class:`str`]
        """

        return self._data["location"]

    @property
    def name(
        self,
        /,
    ) -> str | None:
        """
        The name of the profile owner.

        :type: Optional[:class:`str`]
        """

        return self._data["name"]

    @property
    def showcase_slots_remaining(
        self,
        /,
    ) -> int:
        """
        The number of slots remaining in the showcase of the profile owner.

        :type: :class:`int`
        """

        return self._data["pinnedItemsRemaining"]

    @property
    def website(
        self,
        /,
    ) -> str | None:
        """
        The website of the profile owner.

        :type: Optional[:class:`str`]
        """

        return self._data["websiteUrl"]

    async def fetch_email(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the email of the profile owner.

        .. note::

            This field requires the following token scopes:

            - ``read:org`` for :attr:`Organization.email`.
            - ``read:user`` OR ``user:email`` for :attr:`User.email`.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.
        ~github.core.errors.ClientResponseGraphQLInsufficientScopesError
            The token used by the client does not have the required scopes.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("email")  # type: ignore

    async def fetch_pinnable_items(
        self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches pinnable items from the profile author.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Gist | Repository]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Gist` | :class:`~github.Repository`]
        """

        raise NotImplementedError  # TODO: ProfileOwner.pinnableItems

    async def fetch_pinned_items(
        self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches pinned items from the profile author.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Gist | Repository]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Gist` | :class:`~github.Repository`]
        """

        raise NotImplementedError  # TODO: ProfileOwner.pinnedItems

    async def fetch_showcase_items(
        self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches showcase items from the profile author.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Gist | Repository]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Gist` | :class:`~github.Repository`]
        """

        raise NotImplementedError  # TODO: ProfileOwner.itemShowcase.items


__all__ = [
    "ProfileOwner",
]
