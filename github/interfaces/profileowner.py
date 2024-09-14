from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict

    # from github.gist.gist import GistData  # TODO: [support-gist]
    # from github.repository.repository import RepositoryData  # TODO: [support-repository]
    from github.utility.types import ConnectionData


    class _OptionalProfileOwnerShowcaseData(TypedDict, total=False):
        pass
        # items: ConnectionData[GistData | RepositoryData]  # TODO: [support-gist] [support-repository]


    class _ProfileOwnerShowcaseData(_OptionalProfileOwnerShowcaseData):
        hasPinnedItems: bool


    class OptionalProfileOwnerData(TypedDict, total=False):
        pass
        # pinnableItems: ConnectionData[GistData | RepositoryData]  # TODO: [support-gist] [support-repository]
        # pinnedItems: ConnectionData[GistData | RepositoryData]  # TODO: [support-gist] [support-repository]


    class ProfileOwnerData(OptionalProfileOwnerData):
        anyPinnableItems: bool
        email: str
        # NOTE: id: str (on Node)
        itemShowcase: _ProfileOwnerShowcaseData
        location: str | None
        # NOTE: login: str (on Actor)
        name: str | None
        pinnedItemsRemaining: int
        viewerCanChangePinnedItems: bool
        websiteUrl: str | None


class ProfileOwner:
    """
    Represents an object that can own a profile.
    """

    __slots__ = ()

    _data: ProfileOwnerData

    _graphql_fields: dict[str, str] = {
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
        self: Self,
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
        self: Self,
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
        self: Self,
        /,
    ) -> bool:
        """
        Whether the profile owner has any pinnable items.

        :type: :class:`bool`
        """

        return self._data["anyPinnableItems"]

    @property
    def has_pinned_items(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the profile owner has any pinned items.

        :type: :class:`bool`
        """

        return self._data["itemShowcase"]["hasPinnedItems"]

    @property
    def location(
        self: Self,
        /,
    ) -> str | None:
        """
        The location of the profile owner.

        :type: Optional[:class:`str`]
        """

        return self._data["location"]

    @property
    def name(
        self: Self,
        /,
    ) -> str | None:
        """
        The name of the profile owner.

        :type: Optional[:class:`str`]
        """

        return self._data["name"]

    @property
    def showcase_slots_remaining(
        self: Self,
        /,
    ) -> int:
        """
        The number of slots remaining in the showcase of the profile owner.

        :type: :class:`int`
        """

        return self._data["pinnedItemsRemaining"]

    @property
    def website(
        self: Self,
        /,
    ) -> str | None:
        """
        The website of the profile owner.

        :type: Optional[:class:`str`]
        """

        return self._data["websiteUrl"]

    async def fetch_email(
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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


__all__: list[str] = [
    "ProfileOwner",
]
