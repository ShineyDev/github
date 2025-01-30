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
    from github.repository.label import LabelData
    from github.repository.pull import PullData


    class LabelRemoveEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["UnlabeledEvent"]

        label: LabelData
        labelable: IssueData | PullData


class LabelRemoveEvent(Node, TimelineItem, Type):
    """
    Represents a label remove event on an :class:`~github.Issue` or
    :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: LabelRemoveEventData

    _graphql_type = "UnlabeledEvent"

    _node_prefix = "UNLE"


__all__ = [
    "LabelRemoveEvent",
]
