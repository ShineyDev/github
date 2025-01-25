from __future__ import annotations
from typing import TYPE_CHECKING

from github.interfaces import Type


if TYPE_CHECKING:
    from typing import Literal

    from github.interfaces.type import TypeData


    class LicenseRuleData(TypeData):
        __typename: Literal["LicenseRule"]

        description: str
        key: str
        label: str


class LicenseRule(Type):
    """
    Represents a license rule.
    """

    __slots__ = ()

    _data: LicenseRuleData

    @staticmethod
    def _patch_data(
        data: LicenseRuleData,
        /,
    ) -> LicenseRuleData:
        return data

    @classmethod
    def _from_data(
        cls,
        data: LicenseRuleData,
        /,
    ):
        return cls(cls._patch_data(data))

    _repr_fields = [
        "key",
    ]

    _graphql_fields = [
        "description",
        "key",
        "label",
    ]

    @property
    def description(
        self,
        /,
    ) -> str:
        """
        A description of the license rule.

        :type: :class:`str`
        """

        return self._data["description"]

    @property
    def key(
        self,
        /,
    ) -> str:
        """
        The machine-readable key of the license rule.

        :type: :class:`str`
        """

        return self._data["key"]

    @property
    def label(
        self,
        /,
    ) -> str:
        """
        The human-readable label of the license rule.

        :type: :class:`str`
        """

        return self._data["label"]


__all__ = [
    "LicenseRule",
]
