from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict

    # from github.repository.repository import RepositoryData  # TODO: [support-repository]
    from github.utility.types import ConnectionData


    class OptionalRepositoryOwnerData(TypedDict, total=False):
        # repositories: ConnectionData[RepositoryData]  # TODO: [support-repository]
        pass


    class RepositoryOwnerData(OptionalRepositoryOwnerData):
        # NOTE: avatarUrl: str (on ProfileOwner)
        # NOTE: id: str (on Node)
        # NOTE: login: str (on ProfileOwner)
        # NOTE: resourcePath: str (on UniformResourceLocatable)
        # NOTE: url: str (on UniformResourceLocatable)
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

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: ConnectionIterator[Repository]

        ..      :class:`~github.utility.ConnectionIterator`[:class:`~github.Repository`]
        """

        raise NotImplementedError  # TODO: RepositoryOwner.repositories

    async def fetch_repository(
        self: Self,
        /,
    ) -> None:
        """
        |coro|

        Fetches a repository from the repository owner.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: Repository

        ..      :class:`~github.Repository`
        """

        raise NotImplementedError  # TODO: RepositoryOwner.repository


__all__: list[str] = [
    "RepositoryOwner",
]
