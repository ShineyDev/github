from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.repository import LockReason

import github
from github.interfaces import Node, Resource, TimelineItem, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.timelineitem import TimelineItemData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData
    from github.repository.lockreason import LockReasonData
    from github.repository.pull import PullData


    class LockEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["ClosedEvent"]

        lockable: IssueData | PullData
        lockReason: LockReasonData


class LockEvent(Node, Resource, TimelineItem, Type):
    """
    Represents a lock event on an :class:`~github.Issue` or
    :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: LockEventData

    _graphql_fields = {
        "reason": "lockReason",
    }

    _graphql_type = "LockedEvent"

    _node_prefix = "LOE"

    @property
    def reason(
        self,
        /,
    ) -> LockReason:
        """
        The reason the subject was locked.

        :type: :class:`~github.LockReason`
        """

        return github.LockReason(self._data["lockReason"])

    async def fetch_reason(
        self,
        /,
    ) -> LockReason:
        """
        |coro|

        Fetches the reason the subject was locked.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.LockReason` | None
        """

        return github.LockReason(await self._fetch_field("lockReason"))


__all__ = [
    "LockEvent",
]
