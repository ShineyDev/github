from __future__ import annotations
from typing import TYPE_CHECKING

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


__all__ = [
    "AssigneeRemoveEvent",
]
