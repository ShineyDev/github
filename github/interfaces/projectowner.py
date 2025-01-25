from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.interfaces import Node


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData


    class ProjectOwnerData(TypedDict):
        # id: str  # NOTE: on Node
        # projectV2  # TODO
        projectsV2: ConnectionData[object]  # TODO


class ProjectOwner:
    """
    Represents an object that can own a :class:`~github.Project`.
    """

    __slots__ = ()

    _data: ProjectOwnerData

    _graphql_fields = {
        "project_count": "projectsV2{totalCount}",
    }

    @property
    def project_count(
        self,
        /,
    ) -> int:
        """
        The number of projects on the project owner.

        :type: :class:`int`
        """

        return self._data["projectsV2"]["totalCount"]

    async def fetch_project_count(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of projects on the project owner.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return await self._fetch_field("projectsV2{totalCount}")  # type: ignore


__all__: list[str] = [
    "ProjectOwner",
]
