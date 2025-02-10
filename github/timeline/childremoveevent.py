from __future__ import annotations
from typing import TYPE_CHECKING

from github.interfaces import Node, TimelineItem, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.timelineitem import TimelineItemData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData


    class ChildRemoveEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["SubIssueRemovedEvent"]

        subIssue: IssueData | None


class ChildRemoveEvent(Node, TimelineItem, Type):
    """
    Represents a child removed event on an :class:`~github.Issue`
    timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: ChildRemoveEventData

    _graphql_type = "SubIssueRemovedEvent"

    _node_prefix = "SIRE"


__all__ = [
    "ChildRemoveEvent",
]
