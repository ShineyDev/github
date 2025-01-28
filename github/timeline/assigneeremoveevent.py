from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.automation import Mannequin
    from github.user import User

import github
from github.interfaces import Node, TimelineItem, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.automation.mannequin import MannequinData
    from github.interfaces.node import NodeData
    from github.interfaces.timelineitem import TimelineItemData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData
    from github.repository.pull import PullData
    from github.user.user import UserData


    class AssigneeRemoveEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["UnassignedEvent"]

        assignable: IssueData | PullData
        assignee: MannequinData | UserData | None
        user: UserData | None


class AssigneeRemoveEvent(Node, TimelineItem, Type):
    """
    Represents an assignee removed event on an :class:`~github.Issue`
    or :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: AssigneeRemoveEventData

    _graphql_type = "UnassignedEvent"

    _node_prefix = "UNE"

    async def fetch_assignee(
        self,
        /,
        **kwargs,  # TODO
    ) -> Mannequin | User:
        """
        |coro|

        Fetches the assignee removed.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Mannequin` | :class:`~github.User`
        """

        data = await self._http.fetch_assigneeremoveevent_assignee(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Mannequin":
            return github.Mannequin._from_data(data, http=self._http)
        elif data["__typename"] == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {data['__typename']} for UnassignedEvent.assignee")


__all__ = [
    "AssigneeRemoveEvent",
]
