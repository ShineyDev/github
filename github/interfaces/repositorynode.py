from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.interfaces import Node
    from github.repository import Repository

import github


if TYPE_CHECKING:
    from typing import TypedDict

    from github.repository.repository import RepositoryData


    class RepositoryNodeData(TypedDict):
        repository: RepositoryData


class RepositoryNode:
    """
    Represents an object associated with a repository.
    """

    __slots__ = ()

    _data: RepositoryNodeData

    async def fetch_repository(
        self: Self,
        /,
        **kwargs,  # TODO
    ) -> Repository:
        """
        |coro|

        Fetches the repository of the repository node.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.Repository`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.fetch_repositorynode_repository(self.id, **kwargs)
        return github.Repository._from_data(data, http=self._http)


__all__: list[str] = [
    "RepositoryNode",
]
