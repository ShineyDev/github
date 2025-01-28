from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.automation import Mannequin
    from github.repository import Issue, Pull
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


    class AssigneeAddEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["AssignedEvent"]

        assignable: IssueData | PullData
        assignee: MannequinData | UserData | None
        user: UserData | None


class AssigneeAddEvent(Node, TimelineItem, Type):
    """
    Represents an assignee added event on an :class:`~github.Issue` or
    :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: AssigneeAddEventData

    _graphql_type = "AssignedEvent"

    _node_prefix = "AE"

    async def fetch_assignee(
        self,
        /,
        **kwargs,  # TODO
    ) -> Mannequin | User:
        """
        |coro|

        Fetches the assignee added.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Mannequin` | :class:`~github.User`
        """

        data = await self._http.fetch_assigneeaddevent_assignee(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Mannequin":
            return github.Mannequin._from_data(data, http=self._http)
        elif data["__typename"] == "User":
            return github.User._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {data['__typename']} for AssignedEvent.assignee")

    async def fetch_subject(
        self,
        /,
        **kwargs,  # TODO
    ) -> Issue | Pull:
        """
        |coro|

        Fetches the subject of the timeline item.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Issue` | :class:`~github.Pull`
        """

        data = await self._http.fetch_assigneeaddevent_subject(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Issue":
            return github.Issue._from_data(data, http=self._http)
        elif data["__typename"] == "PullRequest":
            return github.Pull._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {data['__typename']} for AssignedEvent.assignable")


__all__ = [
    "AssigneeAddEvent",
]
