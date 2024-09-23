from __future__ import annotations
from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final

    _T = TypeVar("_T")


if TYPE_CHECKING:
    from typing import TypedDict


    class ConnectionData(TypedDict, Generic[_T]):
        edges: list[ConnectionEdgeData[_T]]
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


__all__: Final[list[str]] = [
    
]
