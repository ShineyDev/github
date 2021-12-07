from github.interfaces import Type


class LicenseRule(Type):
    """
    Represents a license rule.
    """

    __slots__ = ()

    _repr_fields = [
        "key",
    ]

    _graphql_type = "LicenseRule"

    _graphql_fields = [
        "description",
        "key",
        "label",
    ]

    @property
    def description(self):
        """
        A description of the license rule.

        :type: :class:`str`
        """

        return self._try_get("description")

    @property
    def key(self):
        """
        The machine-readable key of the license rule.

        :type: :class:`str`
        """

        return self._try_get("key")

    @property
    def label(self):
        """
        The human-readable label of the license rule.

        :type: :class:`str`
        """

        return self._try_get("label")


__all__ = [
    "LicenseRule",
]
