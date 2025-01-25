from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.connection import Connection, IssueOrder, PullOrder
    from github.core.http import HTTPClient
    from github.repository import Issue, Pull
    from github.utility.types import DateTime

import github
from github.interfaces import Node, RepositoryNode, Resource, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData
    from github.repository.pull import PullData


    class LabelData(NodeData, RepositoryNodeData, ResourceData, TypeData):
        __typename: Literal["Label"]

        color: str
        createdAt: str
        description: str | None
        isDefault: bool
        issues: ConnectionData[IssueData]
        name: str
        pullRequests: ConnectionData[PullData]
        updatedAt: str


class Label(Node, RepositoryNode, Resource, Type):
    """
    Represents a label.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: LabelData

    @staticmethod
    def _patch_data(
        data: LabelData,
        /,
    ) -> LabelData:
        if data.get("description", False) == "":
            data["description"] = None

        return data

    @classmethod
    def _from_data(
        cls,
        data: LabelData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _repr_fields = [
        "name",
    ]

    _graphql_fields = {
        "color": "color",
        "created_at": "createdAt",
        "description": "description",
        "is_default": "isDefault",
        "name": "name",
        "updated_at": "updatedAt",
    }

    _node_prefix = "LA"

    @property
    def color(
        self,
        /,
    ) -> int:
        """
        The color of the label.

        :type: :class:`int`
        """

        return int(self._data["color"], 16)

    @property
    def created_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the label was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def description(
        self,
        /,
    ) -> str | None:
        """
        The description of the label, if any.

        :type: :class:`str`
        """

        return self._data["description"]

    @property
    def is_default(
        self,
        /,
    ) -> bool:
        """
        Whether the label is a default label.

        .. tip::

            Specifically, this checks whether the name is one of the
            following:

            - bug
            - documentation
            - duplicate
            - enhancement
            - good first issue
            - help wanted
            - invalid
            - question
            - wontfix

        :type: :class:`bool`
        """

        return self._data["isDefault"]

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The name of the label.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def updated_at(
        self,
        /,
    ) -> DateTime:
        """
        The date and time at which the label was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_color(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the color of the label.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return int(await self._fetch_field("color"), 16)  # type: ignore

    async def fetch_created_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the label was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        created_at = await self._fetch_field("createdAt")

        if TYPE_CHECKING:
            created_at = cast(str, created_at)

        return github.utility.iso_to_datetime(created_at)

    async def fetch_description(
        self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the description of the label, if any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_is_default(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the label is a default label.

        .. seealso::

            :attr:`Label.is_default <github.Label.is_default>`


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isDefault")  # type: ignore

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the label.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_updated_at(
        self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the label was last updated.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        updated_at = await self._fetch_field("updatedAt")

        if TYPE_CHECKING:
            updated_at = cast(str, updated_at)

        return github.utility.iso_to_datetime(updated_at)

    def fetch_issues(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: IssueOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Issue]:
        """
        |aiter|

        Fetches issues associated with the label.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.IssueOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Issue`]
        """

        return github.Connection(
            self._http.collect_label_issues,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Issue._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )

    def fetch_pulls(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: PullOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Pull]:
        """
        |aiter|

        Fetches pull requests associated with the label.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.PullOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Connection`[:class:`~github.Pull`]
        """

        return github.Connection(
            self._http.collect_label_pulls,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Pull._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
            **kwargs,
        )


__all__ = [
    "Label",
]
