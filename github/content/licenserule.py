from github.interfaces import Type


class LicenseRule(Type):
    """
    Represents a license rule.
    """

    __slots__ = ()

    _repr_fields = [
        "key",
    ]

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

        return self._get_field("description")

    @property
    def key(self):
        """
        The machine-readable key of the license rule.

        :type: :class:`str`
        """

        return self._get_field("key")

    @property
    def label(self):
        """
        The human-readable label of the license rule.

        :type: :class:`str`
        """

        return self._get_field("label")


__all__ = [
    "LicenseRule",
]
