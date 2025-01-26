from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.connection import Connection, StargazerOrder
    from github.interfaces import Node
    from github.user import User
    from github.user.user import UserData

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData
    from github.user.user import UserData


    class StarrableData(TypedDict):
        # id: str  # NOTE: on Node
        stargazerCount: int
        stargazers: ConnectionData[UserData]
        viewerHasStarred: bool


class Starrable:
    """
    Represents an object that can be starred.
    """

    __slots__ = ()

    _data: StarrableData

    _graphql_fields = {
        "has_viewer_starred": "viewerHasStarred",
        "stargazer_count": "stargazerCount",
    }

    @property
    def has_viewer_starred(
        self,
        /,
    ) -> bool:
        """
        Whether the viewer has starred the starrable.

        :type: :class:`bool`
        """

        return self._data["viewerHasStarred"]

    @property
    def stargazer_count(
        self,
        /,
    ) -> int:
        """
        The number of stars on the starrable.

        :type: :class:`int`
        """

        return self._data["stargazerCount"]

    async def fetch_has_viewer_starred(
        self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the viewer has starred the starrable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerHasStarred")  # type: ignore

    async def fetch_stargazer_count(
        self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of stars on the starrable.

        :rtype: :class:`int`
        """

        return await self._fetch_field("stargazerCount")  # type: ignore

    def fetch_stargazers(
        self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        order_by: StargazerOrder = MISSING,
        reverse: bool = MISSING,
    ) -> Connection[User]:
        """
        |aiter|

        Fetches stargazers from the starrable.


        Parameters
        ----------
        cursor: :class:`str`
            The cursor to start at.
        limit: :class:`int`
            The maximum number of elements to yield.
        reverse: :class:`bool`
            Whether to yield the elements in reverse order.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`~github.connection.Connection`[:class:`~github.User`]
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        return github.Connection(
            self._http.collect_starrable_stargazers,
            self.id,
            order_by.value if order_by is not MISSING else None,
            data_map=lambda d: github.User._from_data(d, http=self._http),
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
        )

    async def star(
        self,
        /,
    ) -> None:
        """
        |coro|

        Stars the starrable.

        Use of this mutation will also update the following fields:

        - :attr:`~.viewer_has_starred`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.mutate_starrable_star(self.id, fields=["viewerHasStarred"])

        self._data["viewerHasStarred"] = data["viewerHasStarred"]

    async def unstar(
        self,
        /,
    ) -> None:
        """
        |coro|

        Unstars the starrable.

        Use of this mutation will also update the following fields:

        - :attr:`~.viewer_has_starred`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.mutate_starrable_unstar(self.id, fields=["viewerHasStarred"])

        self._data["viewerHasStarred"] = data["viewerHasStarred"]


__all__ = [
    "Starrable",
]
