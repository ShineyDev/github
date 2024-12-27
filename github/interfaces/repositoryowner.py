from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.interfaces import Node
    from github.repository import Repository

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connections.connection import ConnectionData
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

    async def fetch_repositories(
        self: Self,
        /,
    ) -> None:
        """
        |aiter|

        Fetches repositories from the repository owner.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Repository]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Repository`]
        """

        raise NotImplementedError  # TODO: RepositoryOwner.repositories

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
