from __future__ import annotations
from typing import TYPE_CHECKING

assert TYPE_CHECKING

from typing import List, Mapping, TypeVar, Union
from typing_extensions import TypeAlias

from datetime import date, datetime


_T = TypeVar("_T")


Date: TypeAlias = date
DateTime: TypeAlias = datetime

T_json_key: TypeAlias = str
T_json_value: TypeAlias = Union[None, bool, int, float, str, List["T_json_value"], Mapping[T_json_key, "T_json_value"]]
T_json_object: TypeAlias = Mapping[str, object]


__all__: list[str] = [
    "Date",
    "DateTime",
    "T_json_key",
    "T_json_value",
    "T_json_object",
]
