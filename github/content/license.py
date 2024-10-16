from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.utility.types import T_json_key, T_json_value

from github import utility
from github.core.errors import ClientObjectMissingFieldError
from github.content.licenserule import LicenseRule
from github.interfaces import Node, Type
from github.utility import MISSING


if TYPE_CHECKING:
    from github.content.licenserule import LicenseRuleData
    from github.interfaces.node import NodeData
    from github.interfaces.type import TypeData


    class LicenseData(NodeData, TypeData):
        body: str
        conditions: list[LicenseRuleData]
        description: str | None
        featured: bool
        hidden: bool
        implementation: str
        key: str
        limitations: list[LicenseRuleData]
        name: str
        nickname: str | None
        permissions: list[LicenseRuleData]
        pseudoLicense: bool
        spdxId: str | None
        url: str | None


class License(Node, Type):
    """
    Represents a license.


    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _data: LicenseData

    _repr_fields: list[str] = [
        "key",
    ]

    _graphql_fields: dict[str, str] = {
        "body": "body",
        "choosealicense_url": "url",
        "conditions": "conditions{%s}" % ",".join(utility.get_defined_graphql_fields(LicenseRule)),
        "description": "description",
        "implementation": "implementation",
        "is_featured": "featured",
        "is_hidden": "hidden",
        "is_pseudo": "pseudoLicense",
        "key": "key",
        "limitations": "limitations{%s}" % ",".join(utility.get_defined_graphql_fields(LicenseRule)),
        "name": "name",
        "nickname": "nickname",
        "permissions": "permissions{%s}" % ",".join(utility.get_defined_graphql_fields(LicenseRule)),
        "spdx_id": "spdxId",
    }

    _node_prefix: str = "L"

    @property
    def body(
        self: Self,
        /,
    ) -> str:
        """
        The body of the license.

        :type: :class:`str`
        """

        return self._data["body"]

    @property
    def choosealicense_url(
        self: Self,
        /,
    ) -> str | None:
        """
        A URL to the license on |choosealicense|.

        :type: Optional[:class:`str`]
        """

        return self._data["url"]

    @property
    def conditions(
        self: Self,
        /,
    ) -> list[LicenseRule]:
        """
        The conditions of the license.

        :type: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule._from_data(self._data["conditions"])

    @property
    def description(
        self: Self,
        /,
    ) -> str | None:
        """
        A description of the license.

        :type: Optional[:class:`str`]
        """

        return self._data["description"]

    @property
    def implementation(
        self: Self,
        /,
    ) -> str | None:
        """
        A guide to implementing the license.

        :type: Optional[:class:`str`]
        """

        return self._data["implementation"]

    @property
    def is_featured(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the license is featured.

        :type: :class:`bool`
        """

        return self._data["featured"]

    @property
    def is_hidden(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the license is hidden.

        :type: :class:`bool`
        """

        return self._data["hidden"]

    @property
    def is_pseudo(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the license is pseudo.

        :type: :class:`bool`
        """

        return self._data["pseudoLicense"]

    @property
    def key(
        self: Self,
        /,
    ) -> str:
        """
        The machine-readable key of the license.

        :type: :class:`str`
        """

        return self._data["key"]

    @property
    def limitations(
        self: Self,
        /,
    ) -> list[LicenseRule]:
        """
        The limitations of the license.

        :type: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule._from_data(self._data["limitations"])

    @property
    def name(
        self: Self,
        /,
    ) -> str:
        """
        The human-readable name of the license.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def nickname(
        self: Self,
        /,
    ) -> str | None:
        """
        The human-readable nickname of the license.

        :type: Optional[:class:`str`]
        """

        return self._data["nickname"]

    @property
    def permissions(
        self: Self,
        /,
    ) -> list[LicenseRule]:
        """
        The permissions of the license.

        :type: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule._from_data(self._data["permissions"])

    @property
    def spdx_id(
        self: Self,
        /,
    ) -> str | None:
        """
        The ID of the license on |spdx|.

        :type: Optional[:class:`str`]
        """

        return self._data["spdxId"]

    async def _fetch_field(
        self: Self,
        field: T_json_key,
        /,
        *,
        save: bool = MISSING,
    ) -> T_json_value:
        save = save if save is not MISSING else True

        try:
            id = self.id
        except ClientObjectMissingFieldError:
            id = False

        try:
            key = self.key
        except ClientObjectMissingFieldError:
            key = False

        if id is False and key is False:
            raise ClientObjectMissingFieldError("id", "key") from None

        if id is not False:
            data = await self._http.fetch_query_node(self.__class__, id, fields=(field,))
        elif key and key != "other":
            data = await self._http.fetch_query_license(key, fields=(field,))
        elif key is False:
            raise ClientObjectMissingFieldError("key") from None
        else:
            raise ClientObjectMissingFieldError("id") from None

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

        Fetches the body of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("body")  # type: ignore

    async def fetch_choosealicense_url(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches a URL to the license on |choosealicense|.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("url")  # type: ignore

    async def fetch_conditions(
        self: Self,
        /,
    ) -> list[LicenseRule]:
        """
        |coro|

        Fetches the conditions of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule._from_data(await self._fetch_field("conditions"))  # type: ignore

    async def fetch_description(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches a description of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("description")  # type: ignore

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
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await super().fetch_id()  # type: ignore

    async def fetch_implementation(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches a guide to implementing the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("implementation")  # type: ignore

    async def fetch_is_featured(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the license is featured.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("featured")  # type: ignore

    async def fetch_is_hidden(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the license is hidden.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("hidden")  # type: ignore

    async def fetch_is_pseudo(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the license is pseudo.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: :class:`bool`
        """

        return await self._fetch_field("pseudoLicense")  # type: ignore

    async def fetch_key(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the machine-readable key of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("key")  # type: ignore

    async def fetch_limitations(
        self: Self,
        /,
    ) -> list[LicenseRule]:
        """
        |coro|

        Fetches the limitations of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule._from_data(await self._fetch_field("limitations"))  # type: ignore

    async def fetch_name(
        self: Self,
        /,
    ) -> str:
        """
        |coro|

        Fetches the human-readable name of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")  # type: ignore

    async def fetch_nickname(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the human-readable nickname of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("nickname")  # type: ignore

    async def fetch_permissions(
        self: Self,
        /,
    ) -> list[LicenseRule]:
        """
        |coro|

        Fetches the permissions of the license.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule._from_data(await self._fetch_field("permissions"))  # type: ignore

    async def fetch_spdx_id(
        self: Self,
        /,
    ) -> str | None:
        """
        |coro|

        Fetches the ID of the license on |spdx|.


        Raises
        ------

        ~github.core.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.


        :rtype: Optional[:class:`str`]
        """

        return await self._fetch_field("spdxId")  # type: ignore


__all__: list[str] = [
    "License",
]
