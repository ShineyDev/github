from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import ClassVar, Iterable, cast, overload
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.utility.types import T_json_object

from github import utility
from github.core.errors import ClientObjectMissingFieldError


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
            except ClientObjectMissingFieldError:
                pass
            else:
                f_fields[name] = value

        if f_fields:
            m_fields = " ".join(f"{name}={value!r}" for (name, value) in f_fields.items())
            return f"<{self.__class__.__name__} {m_fields}>"
        else:
            return f"<{self.__class__.__name__}>"

    if TYPE_CHECKING:

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
            data: Iterable[T_json_object],
            /,
            *,
            http: HTTPClient | None = None,
        ) -> list[Self]:
            pass

    @classmethod
    def _from_data(
        cls: type[Self],
        data: T_json_object | Iterable[T_json_object],
        /,
        *,
        http: HTTPClient | None = None,
    ) -> Self | list[Self]:
        if isinstance(data, dict):
            if TYPE_CHECKING:
                data = cast(T_json_object, data)

            return cls(data, http)
        else:
            if TYPE_CHECKING:
                data = cast(Iterable[T_json_object], data)

            return [cls(o, http) for o in data]


__all__: list[str] = [
    "Type",
]
