from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.connection import Connection, RepositoryOrder
    from github.interfaces import Node
    from github.repository import Repository
    from github.repository.repository import RepositoryData

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData
    # from github.repository.repository import RepositoryData  # TODO: [support-repository]


    class OptionalRepositoryOwnerData(TypedDict, total=False):
        # repositories: ConnectionData[RepositoryData]  # TODO: [support-repository]
        pass


    class RepositoryOwnerData(OptionalRepositoryOwnerData):
        # NOTE: avatarUrl: str (on ProfileOwner)
        # NOTE: id: str (on Node)
        # NOTE: login: str (on ProfileOwner)
        # NOTE: resourcePath: str (on Resource)
        # NOTE: url: str (on Resource)
        pass


class RepositoryOwner:
    """
    Represents an object that can own a Repository.

    ..                                  :class:`~github.Repository`
    """

    __slots__ = ()

    _data: RepositoryOwnerData

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


        :rtype: :class:`~github.connection.Connection`[:class:`~github.Repository`]
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        def repositorydata_to_repository(repositorydata: RepositoryData, /) -> Repository:
            return github.Repository._from_data(repositorydata, http=self._http)

        return github.Connection(
            self._http.collect_repositoryowner_repositories,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=repositorydata_to_repository,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else None,
            **kwargs,
        )

    async def fetch_repository(
        self: Self,
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


__all__: list[str] = [
    "RepositoryOwner",
]
