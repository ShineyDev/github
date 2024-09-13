from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, cast
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.interfaces.type import Type
    from github.utility.types import T_json_key, T_json_value

from github.core.errors import ClientObjectMissingFieldError


if TYPE_CHECKING:
    from typing import TypedDict


    class NodeData(TypedDict):
        id: str


class Node:
    """
    Represents an object with an ID.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: NodeData
    _http: HTTPClient

    _repr_fields: list[str] = [
        "id",
    ]

    _graphql_fields: list[str] = [
        "id",
    ]

    def __hash__(
        self: Self,
        /,
    ) -> int:
        return hash(self.id)

    def __eq__(
        self: Self,
        other: Any,
        /,
    ) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.id == other.id

    @property
    def id(
        self: Self,
        /,
    ) -> str:
        """
        The ID of the node.

        :type: :class:`str`
        """

        return self._data["id"]

    async def _fetch_field(
        self: Self,
        field: T_json_key,
        /,
        *,
        save: bool = True,
    ) -> T_json_value:
        try:
            id = self.id
        except ClientObjectMissingFieldError:
            id = False

        if id is False:
            raise ClientObjectMissingFieldError("id") from None

        cls = self.__class__

        if TYPE_CHECKING:
            cls = cast(type[Type], cls)

        data = await self._http.fetch_query_node(cls, id, fields=(field,))

        value = data[field]

        if save:
            self._data[field] = value

        return value

    async def fetch_id(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the ID of the node.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("id")  # type: ignore


__all__: list[str] = [
    "Node",
]
