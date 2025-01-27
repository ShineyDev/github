from __future__ import annotations
from typing import TYPE_CHECKING

from github.interfaces import Node, Resource, TimelineItem, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.timelineitem import TimelineItemData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData
    from github.repository.issueclosereason import IssueCloseReasonData
    from github.repository.pull import PullData


    class CloseEventData(NodeData, ResourceData, TimelineItemData, TypeData):
        __typename: Literal["ClosedEvent"]

        closable: IssueData | PullData
        # closer  # TODO
        stateReason: IssueCloseReasonData


class CloseEvent(Node, Resource, TimelineItem, Type):
    """
    Represents a close event on an :class:`~github.Issue` or
    :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: CloseEventData

    _node_prefix = "CE"


__all__ = [
    "CloseEvent",
]
