from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.repository import Issue, Label, Pull

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

    async def fetch_label(
        self,
        /,
        **kwargs,  # TODO
    ) -> Label:
        """
        |coro|

        Fetches the label removed.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Label`
        """

        data = await self._http.fetch_labelremoveevent_label(self.id, **kwargs)
        return github.Label._from_data(data, http=self._http)

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

        data = await self._http.fetch_labelremoveevent_subject(self.id, **kwargs)

        # TODO[type-from-data]

        if data["__typename"] == "Issue":
            return github.Issue._from_data(data, http=self._http)
        elif data["__typename"] == "PullRequest":
            return github.Pull._from_data(data, http=self._http)
        else:
            raise RuntimeError(f"unsupported type {data['__typename']} for UnlabeledEvent.assignable")


__all__ = [
    "LabelRemoveEvent",
]
