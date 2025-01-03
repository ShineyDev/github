from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict


    class VotableData(TypedDict):
        upvoteCount: int
        viewerCanUpvote: bool
        viewerHasUpvoted: bool


class Votable:
    """
    Represents an object that can be upvoted.
    """

    __slots__ = ()

    _data: VotableData

    _graphql_fields: dict[str, str] = {
        "upvote_count": "upvoteCount",
        "viewer_can_upvote": "viewerCanUpvote",
        "viewer_has_upvoted": "viewerHasUpvoted",
    }

    @property
    def upvote_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of upvotes on the votable.

        :type: :class:`int`
        """

        return self._data["upvoteCount"]

    @property
    def viewer_can_upvote(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can upvote the votable.

        :type: :class:`bool`
        """

        return self._data["viewerCanUpvote"]

    @property
    def viewer_has_upvoted(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user has upvoted the votable.

        :type: :class:`bool`
        """

        return self._data["viewerHasUpvoted"]

    async def fetch_upvote_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of upvotes on the votable

        :rtype: :class:`int`
        """

        return await self._fetch_field("upvoteCount")  # type: ignore

    async def fetch_viewer_can_upvote(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can upvote the votable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanUpvote")  # type: ignore

    async def fetch_viewer_has_upvoted(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user has upvoted the votable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerHasUpvoted")  # type: ignore


__all__ = [
    "Votable",
]
