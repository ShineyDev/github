import re

from github.errors import ClientObjectMissingFieldError
from github.interfaces import Node, Type, UniformResourceLocatable


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

    _repr_fields = [
        "key",
    ]

    _graphql_type = "CodeOfConduct"

    _graphql_fields = [
        "body",
        "key",
        "name",
    ]

    @property
    def body(self):
        """
        The body of the code of conduct.

        :type: :class:`str`
        """

        return self._try_get("body")

    @property
    def key(self):
        """
        The machine-readable key of the code of conduct.

        :type: :class:`str`
        """

        return self._try_get("key")

    @property
    def name(self):
        """
        The human-readable name of the code of conduct.

        :type: :class:`str`
        """

        return self._try_get("name")

    @property
    def resource_path(self):
        return super().resource_path

    resource_path.__doc__ = re.sub(
        ":type: [^\n]+\n",
        ":type: Optional[:class:`str`]",
        UniformResourceLocatable.resource_path.__doc__,
    )

    @property
    def url(self):
        return super().url

    url.__doc__ = re.sub(
        ":type: [^\n]+\n",
        ":type: Optional[:class:`str`]",
        UniformResourceLocatable.url.__doc__,
    )

    async def _fetch_field(self, field):
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
            data = await self._http.fetch_node(self.__class__, id, fields=(field,))
        elif key is not False and (url is None or key != "other"):
            data = await self._http.fetch_query_code_of_conduct(key, fields=(field,))
        elif key is False:
            raise ClientObjectMissingFieldError("id", "key") from None
        elif url is False:
            raise ClientObjectMissingFieldError("id", "url") from None
        else:
            raise NotImplementedError  # TODO: custom code of conduct

        value = data[field]

        self._data[field] = value
        return value

    async def fetch_body(self):
        """
        |coro|

        Fetches the body of the code of conduct.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.

        Returns
        -------
        :class:`str`
            The body of the code of conduct.
        """

        return await self._fetch_field("body")

    fetch_id = Node.fetch_id
    fetch_id.__doc__ = """
        |coro|

        Fetches the ID of the node.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.

        Returns
        -------
        :class:`str`
            The ID of the node.
    """

    async def fetch_key(self):
        """
        |coro|

        Fetches the machine-readable key of the code of conduct.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.

        Returns
        -------
        :class:`str`
            The machine-readable key of the code of conduct.
        """

        return await self._fetch_field("key")

    async def fetch_name(self):
        """
        |coro|

        Fetches the human-readable name of the code of conduct.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.

        Returns
        -------
        :class:`str`
            The human-readable name of the code of conduct.
        """

        return await self._fetch_field("name")

    async def fetch_resource_path(self):
        """
        |coro|

        Fetches an HTTP path to the resource.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.

        Returns
        -------
        Optional[:class:`str`]
            An HTTP path to the resource.
        """

        return await self._fetch_field("resourcePath")

    async def fetch_url(self):
        """
        |coro|

        Fetches an HTTP URL to the resource.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id`, :attr:`key`, and :attr:`url` attributes are
            all missing. OR; (on an instance-level code of conduct) The
            :attr:`id` and :attr:`key` attributes are missing. OR; (on
            a repository-level code of conduct) The :attr:`id` and
            :attr:`url` attributes are missing.

        Returns
        -------
        Optional[:class:`str`]
            An HTTP URL to the resource.
        """

        return await self._fetch_field("url")


__all__ = [
    "CodeOfConduct",
]
