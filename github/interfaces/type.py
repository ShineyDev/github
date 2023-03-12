from __future__ import annotations
from typing import TYPE_CHECKING, ClassVar, overload

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.client.http import HTTPClient
    from github.utilities.types import T_json_object

from github import utilities
from github.client.errors import ClientObjectMissingFieldError


if TYPE_CHECKING:
    from typing import TypedDict


    class TypeData(TypedDict):
        __typename: str


class Type:
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
        self._data = utilities.DataWrapper(data)  # type: ignore
        self._http: HTTPClient | None = http

    def __repr__(
        self: Self,
        /,
    ) -> str:
        d_fields = utilities.get_defined_repr_fields(self.__class__)

        f_fields = dict()
        for name in d_fields:
            try:
                value = getattr(self, name)
            except ClientObjectMissingFieldError:
                pass
            else:
                f_fields[name] = value

        if f_fields:
            m_fields = " ".join(f"{name}={value!r}" for (name, value) in f_fields.items())
            return f"<{self.__class__.__name__} {m_fields}>"
        else:
            return f"<{self.__class__.__name__}>"

    @overload
    @classmethod
    def _from_data(
        cls: type[Self],
        data: T_json_object,
        /,
        *,
        http: HTTPClient | None = None,
    ) -> Self:
        pass

    @overload
    @classmethod
    def _from_data(
        cls: type[Self],
        data: list[T_json_object],
        /,
        *,
        http: HTTPClient | None = None,
    ) -> list[Self]:
        pass

    @classmethod
    def _from_data(
        cls: type[Self],
        data: T_json_object | list[T_json_object],
        /,
        *,
        http: HTTPClient | None = None,
    ) -> Self | list[Self]:
        if isinstance(data, list):
            return [cls(o, http) for o in data]

        return cls(data, http)


__all__: list[str] = [
    "Type",
]
