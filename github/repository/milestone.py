from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.utility.types import DateTime

import github
from github.interfaces import Closable, Node, RepositoryNode, Resource, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.automation.bot import BotData
    from github.connection.connection import ConnectionData
    from github.interfaces.closable import ClosableData
    from github.interfaces.node import NodeData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.type import TypeData
    from github.repository.issue import IssueData
    from github.repository.milestonestate import MilestoneStateData
    from github.repository.pull import PullData
    from github.user.user import UserData


    class MilestoneData(
        ClosableData,
        NodeData,
        RepositoryNodeData,
        ResourceData,
        TypeData,
    ):
        __typename: Literal["Milestone"]

        createdAt: str
        creator: BotData | UserData
        description: str | None
        dueOn: str | None
        issues: ConnectionData[IssueData]
        number: int
        progressPercentage: float
        pullRequests: ConnectionData[PullData]
        state: MilestoneStateData
        title: str
        updatedAt: str


class Milestone(Closable, Node, RepositoryNode, Resource, Type):
    """
    Represents a milestone.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: MilestoneData

    @staticmethod
    def _patch_data(
        data: MilestoneData,
        /,
    ) -> MilestoneData:
        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: MilestoneData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _repr_fields: list[str] = [
        "number",
    ]

    _graphql_fields: dict[str, str] = {
        "created_at": "createdAt",
        "description": "description",
        "due_at": "dueOn",
        "number": "number",
        "progress": "progressPercentage",
        # "state": "state",  # TODO: type
        "title": "title",
        "updated_at": "updatedAt",
    }

    _node_prefix: str = "MI"

    @property
    def created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the milestone was created.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["createdAt"])

    @property
    def description(
        self: Self,
        /,
    ) -> str | None:
        """
        The description of the milestone.

        :type: :class:`str` | None
        """

        return self._data["description"]

    @property
    def due_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        The date and time at which the milestone is due, if any.

        :type: :class:`~datetime.datetime` | None
        """

        due_at = self._data["dueOn"]

        if due_at is None:
            return None

        return github.utility.iso_to_datetime(due_at)

    @property
    def number(
        self: Self,
        /,
    ) -> int:
        """
        The number of the milestone.

        :type: :class:`int`
        """

        return self._data["number"]

    @property
    def progress(
        self: Self,
        /,
    ) -> float:
        """
        The progress of the milestone, as a float between 0 and 100.

        :type: :class:`float`
        """

        return self._data["progressPercentage"]

    @property
    def title(
        self: Self,
        /,
    ) -> str:
        """
        The title of the milestone.

        :type: :class:`str`
        """

        return self._data["title"]

    @property
    def updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        The date and time at which the milestone was last updated.

        :type: :class:`~datetime.datetime`
        """

        return github.utility.iso_to_datetime(self._data["updatedAt"])

    async def fetch_created_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the milestone was created.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

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

        Fetches the description of the milestone.

        :rtype: :class:`str` | None
        """

        return await self._fetch_field("description")  # type: ignore

    async def fetch_due_at(
        self: Self,
        /,
    ) -> DateTime | None:
        """
        |coro|

        Fetches the date and time at which the milestone is due, if
        any.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~datetime.datetime` | None
        """

        due_at = await self._fetch_field("dueOn")

        if due_at is None:
            return None

        if TYPE_CHECKING:
            due_at = cast(str, due_at)

        return github.utility.iso_to_datetime(due_at)

    async def fetch_number(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of the milestone.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("number")  # type: ignore

    async def fetch_progress(
        self: Self,
        /,
    ) -> float:
        """
        |coro|

        Fetches the progress of the milestone, as a float between 0 and
        100.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`float`
        """

        return await self._fetch_field("progressPercentage")  # type: ignore

    async def fetch_title(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the title of the milestone.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("title")  # type: ignore

    async def fetch_updated_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        |coro|

        Fetches the date and time at which the milestone was last
        updated.


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
    "Milestone",
]
