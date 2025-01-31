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


    class SubscribeEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["SubscribedEvent"]

        subscribable: IssueData | PullData


class SubscribeEvent(Node, TimelineItem, Type):
    """
    Represents a subscribe event on an :class:`~github.Issue` or
    :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: SubscribeEventData

    _graphql_type = "SubscribedEvent"

    _node_prefix = "SE"


__all__ = [
    "SubscribeEvent",
]
