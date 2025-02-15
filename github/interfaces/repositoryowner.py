from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.connection import Connection, RepositoryOrder
    from github.interfaces import Node
    from github.repository import Repository, RepositoryVisibility

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData
    from github.repository.repository import RepositoryData


    class RepositoryOwnerData(TypedDict):
        # avatarUrl: str  # NOTE: on Actor
        # id: str  # NOTE: on Node
        # login: str  # NOTE: on Actor
        repositories: ConnectionData[RepositoryData]
        repository: RepositoryData
        # resourcePath: str  # NOTE: on Resource
        # url: str  # NOTE: on Resource


class RepositoryOwner:
    """
    Represents an object that can own a :class:`~github.Repository`.
    """

    __slots__ = ()

    _data: RepositoryOwnerData

    _graphql_fields = {
        "repository_count": "repositories{totalCount}",
    }

    @property
    def repository_count(
        self,
        /,
    ) -> int:
        """
        The number of repositories on the repository owner.

        :type: :class:`int`
        """

        return self._data["repositories"]["totalCount"]

    async def fetch_repository_count(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of repositories on the repository owner.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return await self._fetch_field("repositories{totalCount}")  # type: ignore

    async def fetch_repository(
        self,
        name: str,
        /,
        *,
        follow_renames: bool = MISSING,
        **kwargs,  # TODO
    ) -> Repository:
        """
        |coro|

        Fetches a repository from the repository owner.


        Parameters
        ----------

        name: :class:`str`
            The name of the repository.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.
        ~github.core.errors.ClientResponseGraphQLNotFoundError
            A repository with the provided name does not exist.


        :rtype: :class:`~github.Repository`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.fetch_repositoryowner_repository(
            self.id,
            name,
            follow_renames if follow_renames is not MISSING else None,
            **kwargs,
        )

        return github.Repository._from_data(data, http=self._http)

    def fetch_repositories(
        self,
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

        Fetches repositories from the repository owner.


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


        :rtype: :class:`~github.Connection` of :class:`~github.Repository`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return github.Connection(
            self._http.collect_repositoryowner_repositories,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.Repository._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else None,
            **kwargs,
        )

    async def create_repository(
        self,
        /,
        name: str,
        *,
        description: str = MISSING,
        fields = MISSING,  # TODO
        visibility: RepositoryVisibility = MISSING,
    ) -> Repository:
        """
        |coro|

        Creates a repository on the repository owner.


        .. note::

            Use of this mutation will also update the following fields:

            - :attr:`~.repository_count`


        Parameters
        ----------
        name: :class:`str`
            The name of the repository.
        description: :class:`str`
            The description of the repository.
        visibility: :class:`~github.RepositoryVisibility`
            The visibility of the repository.


        :rtype: :class:`~github.Repository`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        repositoryowner_data, repository_data = await self._http.mutate_repositoryowner_create_repository(
            self.id,
            description if description is not MISSING else None,
            name,
            visibility.value if visibility is not MISSING else github.RepositoryVisibility.public.value,
            repository_fields=fields,
            repositoryowner_fields=("repositories{totalCount}",),
        )

        if "repositories" not in self._data.keys():
            self._data["repositories"] = dict()  # type: ignore

        self._data["repositories"]["totalCount"] = repositoryowner_data["repositories"]["totalCount"]

        return github.Repository._from_data(repository_data, http=self._http)


__all__ = [
    "RepositoryOwner",
]
