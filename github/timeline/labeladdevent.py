from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.repository import Issue, Pull

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


    class LabelAddEventData(NodeData, TimelineItemData, TypeData):
        __typename: Literal["LabeledEvent"]

        label: LabelData
        labelable: IssueData | PullData


class LabelAddEvent(Node, TimelineItem, Type):
    """
    Represents a label added event on an :class:`~github.Issue` or
    :class:`~github.Pull` timeline.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: LabelAddEventData

    _graphql_type = "LabeledEvent"

    _node_prefix = "LE"

    async def fetch_subject(
        self,
        /,
        **kwargs,  # TODO
    ) -> Issue | Pull:
        """
        |coro|

        Fetches the subject of the timeline item.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Issue` | :class:`~github.Pull`
        """

        data = await self._http.fetch_labeladdevent_subject(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Issue":
            return github.Issue._from_data(data, http=self._http)
        elif data["__typename"] == "PullRequest":
            return github.Pull._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {data['__typename']} for LabeledEvent.assignable")


__all__ = [
    "LabelAddEvent",
]
