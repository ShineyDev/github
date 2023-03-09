from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self


if TYPE_CHECKING:
    from typing import TypedDict


    class ActorData(TypedDict):
        avatarUrl: str
        login: str


class Actor:
    """
    Represents an object that can take action.
    """

    __slots__ = ()

    _data: ActorData

    _repr_fields: list[str] = [
        "login",
    ]

    _graphql_fields: dict[str, str] = {
        "avatar_url": "avatarUrl",
        "login": "login",
    }

    @property
    def avatar_url(
        self: Self,
        /,
    ) -> str:
        """
        A URL to the avatar of the actor.

        :type: :class:`str`
        """

        return self._data["avatarUrl"]

    @property
    def login(
        self: Self,
        /,
    ) -> str:
        """
        The login of the actor.

        :type: :class:`str`
        """

        return self._data["login"]

    async def fetch_avatar_url(
        self: Self,
        /,
        *,
        size: int | None = None,
    ) -> str:
        """
        |coro|

        Fetches a URL to the avatar of the actor.

        Parameters
        ----------
        size: :class:`int`
            The width of the square image in pixels.


        :rtype: :class:`str`
        """

        if size is not None:
            field = f"avatarUrl(size:{size})"
            save = False
        else:
            field = "avatarUrl"
            save = True

        return await self._fetch_field(field, save=save)  # type: ignore

    async def fetch_login(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the login of the actor.

        :rtype: :class:`str`
        """

        return await self._fetch_field("login")  # type: ignore


__all__: list[str] = [
    "Actor",
]
