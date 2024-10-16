from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.interfaces.type import Type
    from github.utility.types import T_json_key, T_json_value

from github.core.errors import ClientObjectMissingFieldError
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import TypedDict


    class ResourceData(TypedDict):
        resourcePath: str
        url: str


class Resource:
    """
    Represents an object with a URL.
    """

    __slots__ = ()

    _data: ResourceData
    _http: HTTPClient

    _graphql_fields: dict[str, str] = {
        "resource_path": "resourcePath",
        "url": "url",
    }

    @property
    def resource_path(
        self: Self,
        /,
    ) -> str:
        """
        An HTTP path to the resource.

        :type: :class:`str`
        """

        return self._data["resourcePath"]

    @property
    def url(
        self: Self,
        /,
    ) -> str:
        """
        An HTTP URL to the resource.

        :type: :class:`str`
        """

        return self._data["url"]

    async def _fetch_field(
        self: Self,
        field: T_json_key,
        /,
        *,
        save: bool = MISSING,
    ) -> T_json_value:
        save = save if save is not MISSING else True

        try:
            url = self.url
        except ClientObjectMissingFieldError:
            url = False

        if url is False:
            raise ClientObjectMissingFieldError("url") from None

        cls = self.__class__

        if TYPE_CHECKING:
            cls = cast(type[Type], cls)

        data = await self._http.fetch_query_resource(cls, url, fields=(field,))

        value = data[field]

        if save:
            self._data[field] = value

        return value

    async def fetch_resource_path(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches an HTTP path to the resource.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`url` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("resourcePath")  # type: ignore

    async def fetch_url(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches an HTTP URL to the resource.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`url` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("url")  # type: ignore


__all__: list[str] = [
    "Resource",
]
