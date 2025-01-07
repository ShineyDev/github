from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import ClassVar, Iterable, cast, overload
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.utility.types import T_json_object

import abc

import github
from github import utility


if TYPE_CHECKING:
    from typing import TypedDict


    class TypeData(TypedDict):
        __typename: str


class Type(abc.ABC):
    __slots__ = ("_data", "_http")

    _data: TypeData

    _repr_fields: ClassVar[list[str]]

    _graphql_fields: ClassVar[dict[str, str] | list[str]] = [
        "__typename",
    ]

    _graphql_type: ClassVar[str]

    def __init__(
        self: Self,
        data: T_json_object,
        http: HTTPClient | None = None,
        /,
    ) -> None:
        self._data = utility.DataWrapper(data)  # type: ignore
        self._http: HTTPClient | None = http

    def __repr__(
        self: Self,
        /,
    ) -> str:
        d_fields = utility.get_defined_repr_fields(self.__class__)

        f_fields = dict()
        for name in d_fields:
            try:
                value = getattr(self, name)
            except github.ClientObjectMissingFieldError:
                pass
            else:
                f_fields[name] = value

        if f_fields:
            m_fields = " ".join(f"{name}={value!r}" for (name, value) in f_fields.items())
            return f"<{self.__class__.__name__} {m_fields}>"
        else:
            return f"<{self.__class__.__name__}>"

    @staticmethod
    @abc.abstractmethod
    def _patch_data(
        data: T_json_object,
        /,
    ) -> T_json_object:
        raise NotImplementedError

    @classmethod
    @abc.abstractmethod
    def _from_data(
        cls: type[Self],
        data: T_json_object,
        /,
        *,
        http: HTTPClient | None = None,
    ) -> Self:
        raise NotImplementedError


__all__: list[str] = [
    "Type",
]
