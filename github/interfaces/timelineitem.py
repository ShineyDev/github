from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.interfaces import Node
    from github.utility.types import DateTime

import github


if TYPE_CHECKING:
    from typing import TypedDict

    from github.automation.bot import BotData
    from github.automation.mannequin import MannequinData
    from github.organization.organization import OrganizationData
    from github.user.user import UserData


    class TimelineItemData(TypedDict):
        actor: BotData | MannequinData | OrganizationData | UserData | None
        createdAt: str


class TimelineItem:
    """
    Represents an item in an issue or pull request timeline.
    """

    __slots__ = ()

    _data: TimelineItemData

    _graphql_fields = {
        "created_at": "createdAt",
    }

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the timeline item was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the timeline item was
        created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        created_at = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            created_at = cast(str, created_at)

        return github.utility.iso_to_datetime(created_at)


__all__ = [
    "TimelineItem",
]
