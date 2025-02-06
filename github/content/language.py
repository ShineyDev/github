from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.core.http import HTTPClient

from github.interfaces import Node, Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData


    class LanguageData(NodeData, TypeData):
        __typename: Literal["Language"]

        color: str | None
        name: str


class Language(Node, Type):
    """
    Represents a language.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: LanguageData

    @staticmethod
    def _patch_data(
        data: LanguageData,
        /,
    ) -> LanguageData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: LanguageData,
        /,
        *,
        http: HTTPClient,
    ):
        return cls(cls._patch_data(data), http)

    _graphql_fields = [
        "color",
        "name",
    ]

    _node_prefix = "LAN"

    _repr_fields = [
        "name",
    ]

    @property
    def color(
        self,
        /,
    ) -> int | None:
        """
        The color of the language, if it has one.

        :type: :class:`int` | None
        """

        color = self._data["color"]

        if color is None:
            return None

        return int(color[1:])

    @property
    def name(
        self,
        /,
    ) -> str:
        """
        The name of the language.

        :type: :class:`str`
        """

        return self._data["name"]

    async def fetch_color(
        self,
        /,
    ) -> int | None:
        """
        |coro|

        Fetches the color of the language, if it has one.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`int` | None
        """

        color = await self._fetch_field("color")

        if color is None:
            return None

        return int(color[1:])  # type: ignore

    async def fetch_name(
        self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the name of the language.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore


__all__ = [
    "Language",
]
