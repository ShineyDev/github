from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

from github.interfaces import Node, Starrable, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connections.connection import ConnectionData
    from github.interfaces.node import NodeData
    from github.interfaces.starrable import StarrableData
    from github.interfaces.type import TypeData
    # from github.repository.repository import RepositoryData  # TODO: [support-repository]


    class OptionalTopicData(TypedDict, total=False):
        relatedTopics: list[TopicData]
        # repositories: ConnectionData[RepositoryData]  # TODO: [support-repository]


    class TopicData(OptionalTopicData, NodeData, StarrableData, TypeData):
        name: str


class Topic(Node, Starrable, Type):
    """
    Represents a repository topic.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: TopicData

    _repr_fields: list[str] = [
        "name",
    ]

    _graphql_fields: list[str] = [
        "name",
    ]

    _node_prefix: str = "TO"

    @property
    def name(
        self: Self,
        /,
    ) -> str:
        """
        The name of the topic.

        :type: :class:`str`
        """

        return self._data["name"]

    async def fetch_name(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the topic.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_related_topics(
        self: Self,
        /,
        *,
        limit: int = MISSING,
        **kwargs,  # TODO
    ) -> list[Topic]:
        """
        |coro|

        Fetches topics related to the topic.


        Parameters
        ----------

        limit: :class:`int`
            The number of related topics to fetch. Defaults to 3.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: List[:class:`~github.Topic`]
        """

        data = await self._http.fetch_topic_related_topics(self.id, limit if limit is not MISSING else None, **kwargs)
        return Topic._from_data(data)

    async def fetch_repositories(
        self: Self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches repositories from the topic.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Repository]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Repository`]
        """

        raise NotImplementedError  # TODO: Topic.repositories


__all__: list[str] = [
    "Topic",
]
