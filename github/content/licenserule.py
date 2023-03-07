from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

from github.interfaces import Type


if TYPE_CHECKING:
    from github.interfaces.type import TypeData


    class LicenseRuleData(TypeData):
        description: str
        key: str
        label: str


class LicenseRule(Type):
    """
    Represents a license rule.
    """

    __slots__ = ()

    _data: LicenseRuleData

    _repr_fields: list[str] = [
        "key",
    ]

    _graphql_fields: list[str] = [
        "description",
        "key",
        "label",
    ]

    @property
    def description(
        self: Self,
        /,
    ) -> str:
        """
        A description of the license rule.

        :type: :class:`str`
        """

        return self._get_field("description")  # type: ignore

    @property
    def key(
        self: Self,
        /,
    ) -> str:
        """
        The machine-readable key of the license rule.

        :type: :class:`str`
        """

        return self._get_field("key")  # type: ignore

    @property
    def label(
        self: Self,
        /,
    ) -> str:
        """
        The human-readable label of the license rule.

        :type: :class:`str`
        """

        return self._get_field("label")  # type: ignore


__all__: list[str] = [
    "LicenseRule",
]
