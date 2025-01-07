from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.connection import Connection, RepositoryOrder
    from github.core.http import HTTPClient
    from github.repository import Repository
    from github.repository.repository import RepositoryData

import github
from github.interfaces import Node, Starrable, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Literal

    from github.connection.connection import ConnectionData
    from github.interfaces.node import NodeData
    from github.interfaces.starrable import StarrableData
    from github.interfaces.type import TypeData
    from github.repository.repository import RepositoryData


    class TopicData(NodeData, StarrableData, TypeData):
        __typename: Literal["Topic"]

        name: str
        relatedTopics: list[TopicData]
        repositories: ConnectionData[RepositoryData]


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

    @staticmethod
    def _patch_data(
        data: TopicData,
        /,
    ) -> TopicData:
        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: TopicData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _repr_fields: list[str] = [
        "name",
    ]

    _graphql_fields: dict[str, str] = {
        "name": "name",
        "repository_count": "repositories{totalCount}",
    }

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

    @property
    def repository_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of repositories associated with the topic.

        :type: :class:`int`
        """

        return self._data["repositories"]["totalCount"]

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

    async def fetch_repository_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of repositories associated with the topic.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        connection = await self._fetch_field("repositories{totalCount}")

        if TYPE_CHECKING:
            connection = cast(ConnectionData, connection)

        return connection["totalCount"]

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
        return [Topic._from_data(d, http=self._http) for d in data]

    def fetch_repositories(
        self: Self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: RepositoryOrder = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[Repository]:
        """
        |aiter|

        Fetches repositories from the topic.


        Parameters
        ----------

        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        order_by: :class:`~github.RepositoryOrder`
            The field by which to order the elements.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.connection.Connection`[:class:`~github.Repository`]
        """

        def repositorydata_to_repository(repositorydata: RepositoryData, /) -> Repository:
            return github.Repository._from_data(repositorydata, http=self._http)

        return github.Connection(
            self._http.collect_topic_repositories,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=repositorydata_to_repository,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else None,
            **kwargs,
        )


__all__: list[str] = [
    "Topic",
]
