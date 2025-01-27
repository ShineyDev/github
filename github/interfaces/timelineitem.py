from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.automation import Bot, Mannequin
    from github.interfaces import Node
    from github.organization import Organization
    from github.user import User
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

    async def fetch_actor(
        self,
        /,
        **kwargs,  # TODO
    ) -> Bot | Mannequin | Organization | User:
        """
        |coro|

        Fetches the actor of the timeline item.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Bot` | :class:`~github.Mannequin` | :class:`~github.Organization` | :class:`~github.User`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.fetch_timelineitem_actor(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Bot":
            return github.Bot._from_data(data, http=self._http)
        elif data["__typename"] == "Mannequin":
            return github.Mannequin._from_data(data, http=self._http)
        elif data["__typename"] == "Organization":
            return github.Organization._from_data(data, http=self._http)
        elif data["__typename"] == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {data['__typename']} for TimelineItem.actor")


__all__ = [
    "TimelineItem",
]
