from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.utility.types import DateTime

import github
from github.interfaces import Node, RepositoryNode, Resource, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.type import TypeData


    class LabelData(NodeData, RepositoryNodeData, ResourceData, TypeData):
        __typename: Literal["Label"]

        color: str
        createdAt: str
        description: str | None
        isDefault: bool
        # issues: ConnectionData[IssueData]  # TODO
        name: str
        # pullRequests: ConnectionData[PullRequestData]  # TODO
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

    _repr_fields: list[str] = [
        "name",
    ]

    _graphql_fields: dict[str, str] = {
        "color": "color",
        "created_at": "createdAt",
        "description": "description",
        "is_default": "isDefault",
        "name": "name",
        "updated_at": "updatedAt",
    }

    _node_prefix: str = "LA"

    @property
    def color(
        self: Self,
        /,
    ) -> int:
        """
        The color of the label.

        :type: :class:`int`
        """

        return int(self._data["color"], 16)

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the label was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def description(
        self: Self,
        /,
    ) -> str | None:
        """
        The description of the label, if any.

        :type: :class:`str`
        """

        return self._data["description"]

    @property
    def is_default(
        self: Self,
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
        self: Self,
        /,
    ) -> str:
        """
        The name of the label.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the label was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_color(
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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
        self: Self,
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


__all__ = [
    "Label",
]
