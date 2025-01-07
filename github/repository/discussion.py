from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.repository import DiscussionState

import github
from github.interfaces import Closable, Comment, Deletable, Labelable, Lockable, Node, Reactable, RepositoryNode, Resource, Subscribable, Type, Updatable, Votable


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.closable import ClosableData
    from github.interfaces.comment import CommentData
    from github.interfaces.deletable import DeletableData
    from github.interfaces.labelable import LabelableData
    from github.interfaces.lockable import LockableData
    from github.interfaces.node import NodeData
    from github.interfaces.reactable import ReactableData
    from github.interfaces.repositorynode import RepositoryNodeData
    from github.interfaces.resource import ResourceData
    from github.interfaces.subscribable import SubscribableData
    from github.interfaces.type import TypeData
    from github.interfaces.updatable import UpdatableData
    from github.interfaces.votable import VotableData
    from github.automation.bot import BotData
    from github.user.user import UserData


    class DiscussionData(
        ClosableData,
        CommentData,
        # CommentableData,  # TODO
        DeletableData,
        LabelableData,
        LockableData,
        NodeData,
        ReactableData,
        RepositoryNodeData,
        ResourceData,
        SubscribableData,
        TypeData,
        UpdatableData,
        VotableData,
    ):
        __typename: Literal["Discussion"]

        # answer  # TODO
        answerChosenAt: str
        answerChosenBy: BotData | UserData
        # category  # TODO
        databaseId: int
        isAnswered: bool
        number: int
        # poll  # TODO
        stateReason: Literal["DUPLICATE", "OUTDATED", "REOPENED", "RESOLVED"] | None
        title: str


class Discussion(
    Closable,
    Comment,
    Deletable,
    Labelable,
    Lockable,
    Node,
    Reactable,
    RepositoryNode,
    Resource,
    Subscribable,
    Type,
    Updatable,
    Votable,
):
    """
    Represents a discussion.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: DiscussionData

    @staticmethod
    def _patch_data(
        data: DiscussionData,
        /,
    ) -> DiscussionData:
        data = Comment._patch_data(data)

        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: DiscussionData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _repr_fields: list[str] = [
        "number",
    ]

    _graphql_fields: dict[str, str] = {
        # "": "answerChosenAt",  # TODO: name
        "database_id": "databaseId",
        "is_answered": "isAnswered",
        "number": "number",
        # "": "stateReason",  # TODO: type, name
        "title": "title",
    }

    _node_prefix: str = "D"

    @property
    def database_id(
        self: Self,
        /,
    ) -> int:
        """
        The database ID of the discussion.

        :type: :class:`int`
        """

        return self._data["databaseId"]

    @property
    def is_answered(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the discussion is answered.

        :type: :class:`bool`
        """

        return self._data["isAnswered"]

    @property
    def number(
        self: Self,
        /,
    ) -> int:
        """
        The number of the discussion.

        :type: :class:`int`
        """

        return self._data["number"]

    @property
    def state(
        self: Self,
        /,
    ) -> DiscussionState:
        """
        The state of the discussion.

        .. note::

            This is not an API field.

            Instead, this is calculated using
            :attr:`~github.Discussion.closed_reason`, and requires that
            field to be present.

        :type: :class:`~github.DiscussionState`
        """

        reason = self._data["stateReason"]

        if reason is not None and reason != "REOPENED":
            return github.DiscussionState.closed
        else:
            return github.DiscussionState.open

    @property
    def title(
        self: Self,
        /,
    ) -> str:
        """
        The title of the discussion.

        :type: :class:`str`
        """

        return self._data["title"]

    async def fetch_database_id(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the database ID of the discussion.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("databaseId")  # type: ignore

    async def fetch_is_answered(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the discussion is answered.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("isAnswered")  # type: ignore

    async def fetch_number(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of the discussion.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        return await self._fetch_field("number")  # type: ignore

    async def fetch_state(
        self: Self,
        /,
    ) -> DiscussionState:
        """
        |coro|

        Fetches the state of the discussion.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.DiscussionState`
        """

        reason = await self._fetch_field("stateReason")

        if reason is not None and reason != "REOPENED":
            return github.DiscussionState.closed
        else:
            return github.DiscussionState.open

    async def fetch_title(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the title of the discussion.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("title")  # type: ignore


__all__ = [
    "Discussion",
]
