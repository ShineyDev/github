from __future__ import annotations
from typing import TYPE_CHECKING


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


__all__: list[str] = [
    "RepositoryOwner",
]
