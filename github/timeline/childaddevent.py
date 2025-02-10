from __future__ import annotations
from typing import TYPE_CHECKING

from github.interfaces import Node, TimelineItem, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.timelineitem import TimelineItemData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData


    class ChildAddEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["SubIssueAddedEvent"]

        parent: IssueData | None


class ChildAddEvent(Node, TimelineItem, Type):
    """
    Represents a child added event on an :class:`~github.Issue`
    timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: ChildAddEventData

    _graphql_type = "SubIssueAddedEvent"

    _node_prefix = "SIAE"


__all__ = [
    "ChildAddEvent",
]
