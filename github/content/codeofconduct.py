from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.utilities.types import T_json_key, T_json_value

from github.client.errors import ClientObjectMissingFieldError
from github.interfaces import Node, Type, UniformResourceLocatable


if TYPE_CHECKING:
    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData
    from github.interfaces.uniformresourcelocatable import UniformResourceLocatableData


    class CodeOfConductData(NodeData, TypeData, UniformResourceLocatableData):
        body: str
        key: str
        name: str


class CodeOfConduct(Node, Type, UniformResourceLocatable):
    """
    Represents a code of conduct.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: CodeOfConductData

    _repr_fields: list[str] = [
        "key",
    ]

    _graphql_fields: list[str] = [
        "body",
        "key",
        "name",
    ]

    _node_prefix: str = "COC"

    @property
    def body(
        self: Self,
        /,
    ) -> str:
        """
        The body of the code of conduct.

        :type: :class:`str`
        """

        return self._data["body"]

    @property
    def key(
        self: Self,
        /,
    ) -> str:
        """
        The machine-readable key of the code of conduct.

        :type: :class:`str`
        """

        return self._data["key"]

    @property
    def name(
        self: Self,
        /,
    ) -> str:
        """
        The human-readable name of the code of conduct.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def resource_path(
        self: Self,
        /,
    ) -> str | None:
        """
        An HTTP path to the resource.

        :type: Optional[:class:`str`]
        """

        return super().resource_path

    @property
    def url(
        self: Self,
        /,
    ) -> str | None:
        """
        An HTTP URL to the resource.

        :type: Optional[:class:`str`]
        """

        return super().url

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

        try:
            key = self.key
        except ClientObjectMissingFieldError:
            key = False

        try:
            url = self.url
        except ClientObjectMissingFieldError:
            url = False

        if id is False and key is False and url is False:
            raise ClientObjectMissingFieldError("id", "key", "url") from None

        if id is not False:
            data = await self._http.fetch_query_node(self.__class__, id, fields=(field,))
        elif key and key != "other" and not url:
            data = await self._http.fetch_query_code_of_conduct(key, fields=(field,))
        elif url:
            raise NotImplementedError  # TODO: custom code of conduct
        elif not url:
            raise ClientObjectMissingFieldError("id", "url") from None
        elif not key:
            raise ClientObjectMissingFieldError("id", "key") from None

        value = data[field]

        if save:
            self._data[field] = value

        return value

    async def fetch_body(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the body of the code of conduct.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("body")  # type: ignore

    async def fetch_id(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the ID of the node.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.


        :rtype: :class:`str`
        """

        return await super().fetch_id()  # type: ignore

    async def fetch_key(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the machine-readable key of the code of conduct.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("key")  # type: ignore

    async def fetch_name(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the human-readable name of the code of conduct.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_resource_path(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches an HTTP path to the resource.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.


        :rtype: Optional[:class:`str`]
        """

        return await super().fetch_resource_path()  # type: ignore

    async def fetch_url(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches an HTTP URL to the resource.


        Raises
        ------

        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.


        :rtype: Optional[:class:`str`]
        """

        return await super().fetch_url()  # type: ignore


__all__: list[str] = [
    "CodeOfConduct",
]
