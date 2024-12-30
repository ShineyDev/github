from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.connection import Connection
    from github.interfaces import Node
    from github.user import User
    from github.user.user import UserData

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict

    from github.connection.connection import ConnectionData
    from github.user.user import UserData


    class AssignableData(TypedDict):
        assignees: ConnectionData[UserData]


class Assignable:
    """
    Represents an object that can have assignees.
    """

    __slots__ = ()

    _data: AssignableData

    _graphql_fields: list[str] = []

    def fetch_assignees(
        self: Self,
        /,
        *,
        cursor: str | None = MISSING,
        limit: int = MISSING,
        reverse: bool = MISSING,
        **kwargs,  # TODO
    ) -> Connection[User]:
        """
        |aiter|

        Fetches assignees from the assignable.


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


        :rtype: :class:`~github.connection.Connection`[:class:`github.User`]
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        def userdata_to_user(userdata: UserData, /) -> User:
            return github.User._from_data(userdata, http=self._http)

        return github.Connection(
            self._http.collect_assignable_assignees,
            self.id,
            data_map=userdata_to_user,
            cursor=cursor if cursor is not MISSING else None,
            limit=limit if limit is not MISSING else None,
            reverse=reverse if reverse is not MISSING else None,
            **kwargs,
        )


__all__ = [
    "Assignable",
]
