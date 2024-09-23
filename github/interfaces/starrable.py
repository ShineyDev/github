from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.connections import Connection
    from github.interfaces import Node
    from github.user import User
    from github.user.user import UserData

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connections.connection import ConnectionData
    # from github.user.user import UserData  # TODO: [support-user]


    class OptionalStarrableData(TypedDict, total=False):
        # stargazers: ConnectionData[UserData]  # TODO: [support-user]
        pass


    class StarrableData(OptionalStarrableData):
        # NOTE: id: str (on Node)
        stargazerCount: int
        viewerHasStarred: bool


class Starrable:
    """
    Represents an object that can be starred.
    """

    __slots__ = ()

    _data: StarrableData
    _http: HTTPClient

    _graphql_fields: dict[str, str] = {
        "has_viewer_starred": "viewerHasStarred",
        "stargazer_count": "stargazerCount",
    }

    @property
    def has_viewer_starred(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the viewer has starred the starrable.

        :type: :class:`bool`
        """

        return self._data["viewerHasStarred"]

    @property
    def stargazer_count(
        self: Self,
        /,
    ) -> int:
        """
        The number of stars on the starrable.

        :type: :class:`int`
        """

        return self._data["stargazerCount"]

    async def fetch_has_viewer_starred(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the viewer has starred the starrable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerHasStarred")  # type: ignore

    async def fetch_stargazer_count(
        self: Self,
        /,
    ) -> int:
        """
        |coro|

        Fetches the number of stars on the starrable.

        :rtype: :class:`int`
        """

        return await self._fetch_field("stargazerCount")  # type: ignore

    def fetch_stargazers(
        self: Self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        # order_by: StargazerOrder = MISSING,  # NOTE (stargazerorder): StargazerOrder has only one attribute
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


        :rtype: :class:`~github.connections.Connection`[:class:`~github.User`]
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_starrable_stargazers,
            self.id,
            None,  # order_by.value if order_by is not MISSING else None  # NOTE (stargazerorder): StargazerOrder has only one attribute
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else False,
        )

    async def star(
        self: Self,
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
        self: Self,
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


__all__: list[str] = [
    "Starrable",
]
