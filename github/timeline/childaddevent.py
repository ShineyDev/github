from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.repository import Issue

import github
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

    async def fetch_child(
        self,
        /,
        **kwargs,  # TODO
    ) -> Issue:
        """
        |coro|

        Fetches the child.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Issue`
        """

        data = await self._http.fetch_childaddevent_parent(self.id, **kwargs)
        return github.Issue._from_data(data, http=self._http)


__all__ = [
    "ChildAddEvent",
]
