from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict

    # TODO: from github.???.gist import GistData
    # TODO: from github.???.repository import RepositoryData
    # TODO: from github.utilities.types import ConnectionData


    class _OptionalProfileOwnerShowcaseData(TypedDict, total=False):
        pass
        # TODO: items: ConnectionData[GistData | RepositoryData]


    class _ProfileOwnerShowcaseData(_OptionalProfileOwnerShowcaseData):
        hasPinnedItems: bool


    class OptionalProfileOwnerData(TypedDict, total=False):
        pass
        # TODO: pinnableItems: ConnectionData[GistData | RepositoryData]
        # TODO: pinnedItems: ConnectionData[GistData | RepositoryData]


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
        "email": "email",
        "has_pinnable_items": "anyPinnableItems",
        "has_pinned_items": "itemShowcase{hasPinnedItems}",
        "location": "location",
        "name": "name",
        "showcase_slots_remaining": "pinnedItemsRemaining",
        "viewer_can_change_pinned_items": "viewerCanChangePinnedItems",
        "website": "websiteUrl",
    }

    @property
    def email(
        self: Self,
        /,
    ) -> str | None:
        """
        The email of the profile owner.

        :type: Optional[:class:`str`]
        """

        return self._data["email"] or None

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
    def viewer_can_update_showcase(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can update the showcase of the profile owner.

        :type: :class:`bool`
        """

        return self._data["viewerCanChangePinnedItems"]

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


__all__: list[str] = [
    "ProfileOwner",
]
