from __future__ import annotations
from typing import TYPE_CHECKING

assert TYPE_CHECKING

from typing import Generic, List, Mapping, TypedDict, TypeVar, Union
from typing_extensions import TypeAlias

from datetime import date, datetime


_T = TypeVar("_T")


Date: TypeAlias = date
DateTime: TypeAlias = datetime

T_json_key: TypeAlias = str
T_json_value: TypeAlias = Union[None, bool, int, float, str, List["T_json_value"], Mapping[T_json_key, "T_json_value"]]
T_json_object: TypeAlias = Mapping[str, object]


class ConnectionData(TypedDict, Generic[_T]):
    edges: ConnectionEdgeData[_T]
    nodes: list[_T]
    pageInfo: ConnectionPageData
    totalCount: int


class ConnectionEdgeData(TypedDict, Generic[_T]):
    cursor: str
    node: _T


class ConnectionPageData(TypedDict):
    endCursor: str
    hasNextPage: bool
    hasPreviousPage: bool
    startCursor: str


__all__: list[str] = [
    "Date",
    "DateTime",
    "T_json_key",
    "T_json_value",
    "T_json_object",
]
