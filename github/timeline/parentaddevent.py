from __future__ import annotations
from typing import TYPE_CHECKING

from github.interfaces import Node, TimelineItem, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.timelineitem import TimelineItemData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData


    class ParentAddEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["ParentIssueAddedEvent"]

        parent: IssueData | None


class ParentAddEvent(Node, TimelineItem, Type):
    """
    Represents a parent added event on an :class:`~github.Issue`
    timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: ParentAddEventData

    _graphql_type = "ParentIssueAddedEvent"

    _node_prefix = "PIAE"


__all__ = [
    "ParentAddEvent",
]
