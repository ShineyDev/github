from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.core.http import HTTPClient


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connections.connection import ConnectionData
    # from github.user.user import UserData  # TODO: [support-user]


    class OptionalSponsorableData(TypedDict, total=False):
        pass


    class SponsorableData(OptionalSponsorableData):
        hasSponsorsListing: bool
        isSponsoringViewer: bool
        viewerCanSponsor: bool
        viewerIsSponsoring: bool


class Sponsorable:
    """
    Represents an object that can give or receive a GitHub Sponsors
    sponsorship.
    """

    __slots__ = ()

    _data: SponsorableData
    _http: HTTPClient

    _graphql_fields: dict[str, str] = {
        "can_viewer_sponsor": "viewerCanSponsor",
        "has_sponsors_listing": "hasSponsorsListing",
        "is_sponsoring_viewer": "isSponsoringViewer",
        "is_viewer_sponsoring": "viewerIsSponsoring",
    }

    @property
    def can_viewer_sponsor(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can sponsor the sponsorable.

        :type: :class:`bool`
        """

        return self._data["viewerCanSponsor"]

    @property
    def has_sponsors_listing(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the sponsorable has a GitHub Sponsors listing.

        :type: :class:`bool`
        """

        return self._data["hasSponsorsListing"]

    @property
    def is_sponsoring_viewer(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the sponsorable is sponsoring the authenticated user.

        :type: :class:`bool`
        """

        return self._data["isSponsoringViewer"]

    @property
    def is_viewer_sponsoring(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user is sponsoring the sponsorable.

        :type: :class:`bool`
        """

        return self._data["viewerIsSponsoring"]

    async def fetch_can_viewer_sponsor(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can sponsor the
        sponsorable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanSponsor")  # type: ignore

    async def fetch_has_sponsors_listing(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the sponsorable has a GitHub Sponsors listing.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("hasSponsorsListing")  # type: ignore

    async def fetch_is_sponsoring_viewer(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether sponsorable is sponsoring the authenticated
        user.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("isSponsoringViewer")  # type: ignore

    async def fetch_is_viewer_sponsoring(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user is sponsoring the
        sponsorable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerIsSponsoring")  # type: ignore


__all__: list[str] = [
    "Sponsorable",
]
