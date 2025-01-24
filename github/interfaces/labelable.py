from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.connection import Connection, LabelOrder
    from github.interfaces import Node
    from github.repository import Label

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData
    from github.repository.label import LabelData


    class LabelableData(TypedDict):
        labels: ConnectionData[LabelData]
        viewerCanLabel: bool


class Labelable:
    """
    Represents an object that can have :class:`labels <github.Label>`
    applied to it.
    """

    __slots__ = ()

    _data: LabelableData

    _graphql_fields = {
        "label_count": "labels{totalCount}",
        "viewer_can_label": "viewerCanLabel",
    }

    @property
    def label_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of labels on the labelable.

        :type: :class:`int`
        """

        return self._data["labels"]["totalCount"]

    @property
    def viewer_can_label(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can update labels on the
        labelable.

        :type: :class:`bool`
        """

        return self._data["viewerCanLabel"]

    async def fetch_label_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of labels on the labelable.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return await self._fetch_field("labels{totalCount}")  # type: ignore

    async def fetch_viewer_can_label(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can update labels on the
        labelable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanLabel")  # type: ignore

    def fetch_labels(
        self: Self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: LabelOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Label]:
        """
        |aiter|

        Fetches labels from the labelable.


        Parameters
        ----------

        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.LabelOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Label`]
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        def labeldata_to_label(labeldata: LabelData, /) -> Label:
            return github.Label._from_data(labeldata, http=self._http)

        return github.Connection(
            self._http.collect_labelable_labels,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=labeldata_to_label,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    async def add_labels(
        self: Self,
        /,
        *labels: Label,
    ) -> None:
        """
        |coro|

        Adds labels to the labelable.


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.label_count`


        Parameters
        ----------

        *labels: :class:`github.Label`
            The labels to add.
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.mutate_labelable_add_labels(self.id, [l.id for l in labels], fields=("labels{totalCount}",))

        if "labels" not in self._data.keys():
            self._data["labels"] = dict()  # type: ignore

        self._data["labels"]["totalCount"] = data["labels"]["totalCount"]

    async def remove_labels(
        self: Self,
        /,
        *labels: Label,
    ) -> None:
        """
        |coro|

        Removes labels from the labelable.


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.label_count`


        Parameters
        ----------

        *labels: :class:`github.Label`
            The labels to remove.
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.mutate_labelable_remove_labels(self.id, [l.id for l in labels], fields=("labels{totalCount}",))

        if "labels" not in self._data.keys():
            self._data["labels"] = dict()  # type: ignore

        self._data["labels"]["totalCount"] = data["labels"]["totalCount"]


__all__ = [
    "Labelable",
]
