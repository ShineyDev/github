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


    class PinEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["PinnedEvent"]

        issue: IssueData


class PinEvent(Node, TimelineItem, Type):
    """
    Represents a pin event on an :class:`~github.Issue` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: PinEventData

    _graphql_type = "PinnedEvent"

    _node_prefix = "PE"

    async def fetch_subject(
        self,
        /,
        **kwargs,  # TODO
    ) -> Issue:
        """
        |coro|

        Fetches the subject of the timeline item.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Issue`
        """

        data = await self._http.fetch_pinevent_subject(self.id, **kwargs)
        return github.Issue._from_data(data, http=self._http)


__all__ = [
    "PinEvent",
]
