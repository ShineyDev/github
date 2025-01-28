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
    from github.repository.pull import PullData


    class ReopenEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["ReopenedEvent"]

        closable: IssueData | PullData


class ReopenEvent(Node, TimelineItem, Type):
    """
    Represents a reopen event on an :class:`~github.Issue` or
    :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: ReopenEventData

    _graphql_type = "ReopenedEvent"

    _node_prefix = "REE"


__all__ = [
    "ReopenEvent",
]
