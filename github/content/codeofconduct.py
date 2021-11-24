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

    async def fetch_body(self):
        """
        |coro|

        Fetches the body of the code of conduct.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`key` and :attr:`url` attributes are both
            missing. OR; (on an instance-level code of conduct) The
            :attr:`key` attribute is missing. OR; (on a
            repository-level code of conduct) The :attr:`url` attribute
            is missing.

        Returns
        -------
        :class:`str`
            The body of the code of conduct.
        """

        try:
            key = self._try_get("key")
        except ClientObjectMissingFieldError:
            key = False

        try:
            url = self._try_get("url")
        except ClientObjectMissingFieldError:
            url = False

        if key is False and url is False:
            raise ClientObjectMissingFieldError("key", "url") from None

        if key is not False and (url is None or key != "other"):
            data = await self._http.fetch_query_code_of_conduct(key, fields=("body",))
            return data["body"]
        elif key is False:
            raise ClientObjectMissingFieldError("key") from None
        elif url is False:
            raise ClientObjectMissingFieldError("url") from None
        else:
            raise NotImplementedError  # TODO: custom code of conduct


__all__ = [
    "CodeOfConduct",
]
