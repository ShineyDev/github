from github import utils
from github.errors import ClientObjectMissingFieldError
from github.interfaces import Node, Type
from .licenserule import LicenseRule


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

    _repr_fields = [
        "key",
    ]

    _graphql_type = "License"

    _graphql_fields = {
        "body": "body",
        "choosealicense_url": "url",
        "conditions": "conditions{%s}" % ",".join(utils._get_defined_graphql_fields(LicenseRule)),
        "description": "description",
        "implementation": "implementation",
        "is_featured": "featured",
        "is_hidden": "hidden",
        "is_pseudo": "pseudoLicense",
        "key": "key",
        "limitations": "limitations{%s}" % ",".join(utils._get_defined_graphql_fields(LicenseRule)),
        "name": "name",
        "nickname": "nickname",
        "permissions": "permissions{%s}" % ",".join(utils._get_defined_graphql_fields(LicenseRule)),
        "spdx_id": "spdxId",
    }

    @property
    def body(self):
        """
        The body of the license.

        :type: :class:`str`
        """

        return self._try_get("body")

    @property
    def choosealicense_url(self):
        """
        A URL to the license on |choosealicense|.

        :type: Optional[:class:`str`]
        """

        return self._try_get("url")

    @property
    def conditions(self):
        """
        The conditions of the license.

        :type: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule(self._try_get("conditions"))

    @property
    def description(self):
        """
        A description of the license.

        :type: Optional[:class:`str`]
        """

        return self._try_get("description")

    @property
    def implementation(self):
        """
        A guide to implementing the license.

        :type: Optional[:class:`str`]
        """

        return self._try_get("implementation")

    @property
    def is_featured(self):
        """
        Whether the license is featured.

        :type: :class:`bool`
        """

        return self._try_get("featured")

    @property
    def is_hidden(self):
        """
        Whether the license is hidden.

        :type: :class:`bool`
        """

        return self._try_get("hidden")

    @property
    def is_pseudo(self):
        """
        Whether the license is pseudo.

        :type: :class:`bool`
        """

        return self._try_get("pseudoLicense")

    @property
    def key(self):
        """
        The machine-readable key of the license.

        :type: :class:`str`
        """

        return self._try_get("key")

    @property
    def limitations(self):
        """
        The limitations of the license.

        :type: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule(self._try_get("limitations"))

    @property
    def name(self):
        """
        The human-readable name of the license.

        :type: :class:`str`
        """

        return self._try_get("name")

    @property
    def nickname(self):
        """
        The human-readable nickname of the license.

        :type: Optional[:class:`str`]
        """

        return self._try_get("nickname")

    @property
    def permissions(self):
        """
        The permissions of the license.

        :type: List[:class:`~github.LicenseRule`]
        """

        return LicenseRule(self._try_get("permissions"))

    @property
    def spdx_id(self):
        """
        The ID of the license on |spdx|.

        :type: Optional[:class:`str`]
        """

        return self._try_get("spdxId")

    async def _fetch_field(self, field):
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

        self._data[field] = value
        return value

    async def fetch_body(self):
        """
        |coro|

        Fetches the body of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        :class:`str`
            The body of the license.
        """

        return await self._fetch_field("body")

    async def fetch_choosealicense_url(self):
        """
        |coro|

        Fetches a URL to the license on |choosealicense|.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        Optional[:class:`str`]
            A URL to the license on |choosealicense|.
        """

        return await self._fetch_field("url")

    async def fetch_conditions(self):
        """
        |coro|

        Fetches the conditions of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        List[:class:`~github.LicenseRule`]
            The conditions of the license.
        """

        return LicenseRule(await self._fetch_field("conditions"))

    async def fetch_description(self):
        """
        |coro|

        Fetches a description of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        Optional[:class:`str`]
            A description of the license.
        """

        return await self._fetch_field("description")

    async def fetch_id(self):
        """
        |coro|

        Fetches the ID of the node.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        :class:`str`
            The ID of the node.
        """

        return await super().fetch_id()

    async def fetch_implementation(self):
        """
        |coro|

        Fetches a guide to implementing the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        Optional[:class:`str`]
            A guide to implementing the license.
        """

        return await self._fetch_field("implementation")

    async def fetch_is_featured(self):
        """
        |coro|

        Fetches whether the license is featured.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        :class:`bool`
            Whether the license is featured.
        """

        return await self._fetch_field("featured")

    async def fetch_is_hidden(self):
        """
        |coro|

        Fetches whether the license is hidden.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        :class:`bool`
            Whether the license is hidden.
        """

        return await self._fetch_field("hidden")

    async def fetch_is_pseudo(self):
        """
        |coro|

        Fetches whether the license is pseudo.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        :class:`bool`
            Whether the license is pseudo.
        """

        return await self._fetch_field("pseudoLicense")

    async def fetch_key(self):
        """
        |coro|

        Fetches the machine-readable key of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        :class:`str`
            The machine-readable key of the license.
        """

        return await self._fetch_field("key")

    async def fetch_limitations(self):
        """
        |coro|

        Fetches the limitations of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        List[:class:`~github.LicenseRule`]
            The limitations of the license.
        """

        return LicenseRule(await self._fetch_field("limitations"))

    async def fetch_name(self):
        """
        |coro|

        Fetches the human-readable name of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        :class:`str`
            The human-readable name of the license.
        """

        return await self._fetch_field("name")

    async def fetch_nickname(self):
        """
        |coro|

        Fetches the human-readable nickname of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        Optional[:class:`str`]
            The human-readable nickname of the license.
        """

        return await self._fetch_field("nickname")

    async def fetch_permissions(self):
        """
        |coro|

        Fetches the permissions of the license.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        List[:class:`~github.LicenseRule`]
            The permissions of the license.
        """

        return LicenseRule(await self._fetch_field("permissions"))

    async def fetch_spdx_id(self):
        """
        |coro|

        Fetches the ID of the license on |spdx|.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`.id` and :attr:`.key` attributes are both
            missing. OR; (on an instance-level license) The :attr:`key`
            attribute is missing. OR; (on a repository-level license)
            The :attr:`id` attribute is missing.

        Returns
        -------
        Optional[:class:`str`]
            The ID of the license on |spdx|.
        """

        return await self._fetch_field("spdxId")


__all__ = [
    "License",
]