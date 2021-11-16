import re

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


__all__ = [
    "CodeOfConduct",
]
