from __future__ import annotations
from typing import Generic, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, AsyncIterator, Awaitable, Callable, Final, type_check_only
    from typing_extensions import Self

    _T = TypeVar("_T")

from github.core.http import DEFAULT_MAXIMUM_NODES, DEFAULT_MINIMUM_NODES
from github import utility
from github.utility import MISSING


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


_Tci = TypeVar("_Tci")

if not TYPE_CHECKING:
    AsyncIterator = Generic


class Connection(AsyncIterator[_Tci]):
    """
    An |aiter_link|_ implementation used for GraphQL connections.

    .. container:: operations

        .. describe:: async for item in iterator

            Iterates over items in iterator.
    """

    __slots__ = (
        "_collector",
        "_cursor",
        "_limit",
        "_args",
        "_kwargs",
        "_data_filter",
        "_data_map",
        "_stages",
        "_buffer",
        "_done",
        "_locked",
        "_paginating",
    )

    def __init__(
        self: Self,
        collector: Callable[..., Awaitable[ConnectionData[Any]]],
        /,
        *args: Any,
        data_filter: Callable[[Any], bool | Awaitable[bool]] | None = MISSING,
        data_map: Callable[[Any], _Tci | Awaitable[_Tci]] | None = MISSING,
        limit: int | None = MISSING,
        **kwargs: Any,
    ) -> None:
        self._collector: Callable[..., Awaitable[ConnectionData[Any]]] = collector
        self._limit: int | None = limit if limit is not MISSING else None

        self._args: tuple[Any, ...] = args
        self._kwargs: dict[str, Any] = kwargs
        self._kwargs.setdefault("cursor", None)
        self._kwargs.setdefault("length", None)
        self._kwargs.setdefault("reverse", False)

        # NOTE: the initial stages (see below for the user
        #       implementation) used mostly to get from data to object
        self._data_filter: Callable[[Any], bool | Awaitable[bool]] | None = data_filter if data_filter is not MISSING else None
        self._data_map: Callable[[Any], _Tci | Awaitable[_Tci]] | None = data_map if data_map is not MISSING else None

        # NOTE: collects manipulation steps ("stages") for subsequent
        #       calling on each item in the graph response, properly
        #       supporting i.map(a_to_b).filter(b_with_x).map(b_to_c)
        # TODO: the current implementation is a little jank; i'd prefer
        #       tuple[ManipulationType, Callable] but with only filter
        #       and map i probably won't bother
        self._stages: list[tuple[str, Callable[..., Any]]] = list()

        self._buffer: list[_Tci] = list()
        self._done: bool = False
        self._locked: bool = False
        self._paginating: bool = False

    def __aiter__(
        self: Self,
        /,
    ) -> Self:
        return self

    async def __anext__(
        self: Self,
        /,
    ) -> _Tci:
        self._locked = True

        if self._limit is not None:
            if self._limit <= 0:
                # NOTE: we have already yielded the number of elements
                #       the user requested
                raise StopAsyncIteration

        if self._buffer:
            if self._limit is not None:
                self._limit -= 1

            return self._buffer.pop(0)

        if self._done:
            # NOTE: the connection contains no more elements
            raise StopAsyncIteration

        if self._limit is not None:
            self._kwargs["length"] = max(DEFAULT_MINIMUM_NODES, min(self._limit, self._kwargs["length"] or DEFAULT_MAXIMUM_NODES))

        staged_nodes = list()

        cursor_name = "startCursor" if self._kwargs["reverse"] else "endCursor"
        page_name = "hasPreviousPage" if self._kwargs["reverse"] else "hasNextPage"

        while not staged_nodes and not self._done:
            data = await self._collector(*self._args, **self._kwargs)

            nodes, next_cursor, has_next_page = data["nodes"], data["pageInfo"][cursor_name], data["pageInfo"][page_name]

            self._kwargs["cursor"] = next_cursor
            self._done = not has_next_page

            for node in nodes:
                if self._data_filter is not None:
                    if not await utility.call_maybe_coroutine(self._data_filter, node):
                        continue

                if self._data_map is not None:
                    staged_node = await utility.call_maybe_coroutine(self._data_map, node)
                else:
                    staged_node = node

                filter = False

                for stage_type, stage in self._stages:
                    if stage_type == "filter":
                        if not await utility.call_maybe_coroutine(stage, staged_node):
                            filter = True
                    elif stage_type == "map":
                        staged_node = await utility.call_maybe_coroutine(stage, staged_node)
                    else:
                        raise RuntimeError("invalid stage type; this shouldn't happen")

                if filter:
                    continue

                staged_nodes.append(staged_node)

        if not staged_nodes and self._done:
            # NOTE: the connection contains no more elements and we
            #       filtered away the current page, or the connection
            #       was empty
            raise StopAsyncIteration

        if self._paginating:
            if self._limit is not None:
                self._limit -= len(staged_nodes)

            return staged_nodes[:self._limit]  # type: ignore  # NOTE: this is magic, see Connection.paginate

        self._buffer = staged_nodes

        if self._limit is not None:
            self._limit -= 1

        return self._buffer.pop(0)

    def filter(
        self: Self,
        function: Callable[[_Tci], bool | Awaitable[bool]],
        /,
    ) -> Self:
        """
        This is similar to the built-in :func:`filter <py:filter>`
        function.


        Parameters
        ----------
        function
            The filter predicate.


        :rtype: TODO
        """

        if self._locked:
            raise RuntimeError("cannot update while iterating")

        self._stages.append(("filter", function))

        return self

    async def flatten(
        self: Self,
        /,
    ) -> list[_Tci]:
        """
        |coro|

        Flattens the iterator into a list of its items.


        :rtype: List[T]
        """

        return [e async for e in self]

    def map(
        self: Self,
        function: Callable[[_Tci], _T | Awaitable[_T]],
        /,
    ) -> Connection[_T]:
        """
        This is similar to the built-in :func:`map <py:map>` function.


        Parameters
        ----------
        function
            The mapping function.


        :rtype: TODO
        """

        if self._locked:
            raise RuntimeError("cannot update while iterating")

        self._stages.append(("map", function))

        return self  # type: ignore  # NOTE: this is magic, see note on ConnectionIterator._stages above

    def paginate(
        self: Self,
        /,
        length: int = MISSING,
    ) -> PaginatedConnection[list[_Tci]]:
        """

        """

        if self._locked:
            raise RuntimeError("cannot update while iterating")

        self._kwargs["length"] = length if length is not MISSING else None
        self._paginating = True

        return self  # type: ignore  # NOTE: this is magic, see note on PaginatedConnectionIterator below


if TYPE_CHECKING:

    # NOTE: this type exists as an implementation detail for
    #       ConnectionIterator.paginate to prevent further pagination

    @type_check_only
    class PaginatedConnection(AsyncIterator[_Tci]):
        def filter(self: Self, function: Callable[[_Tci], bool | Awaitable[bool]], /) -> Self: ...
        async def flatten(self: Self, /) -> list[_Tci]: ...
        def map(self: Self, function: Callable[[_Tci], _T | Awaitable[_T]], /) -> PaginatedConnection[_T]: ...


__all__: Final[list[str]] = [
    "Connection",
]
