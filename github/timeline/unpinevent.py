from __future__ import annotations
from typing import TYPE_CHECKING

import github
from github.interfaces import Node, TimelineItem, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.timelineitem import TimelineItemData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData


    class UnpinEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["UnpinnedEvent"]

        issue: IssueData


class UnpinEvent(Node, TimelineItem, Type):
    """
    Represents a unpin event on an :class:`~github.Issue` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: UnpinEventData

    _graphql_type = "UnpinnedEvent"

    _node_prefix = "UNPE"


__all__ = [
    "UnpinEvent",
]
