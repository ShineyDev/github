from __future__ import annotations
from asyncio import iscoroutine
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Awaitable, Callable, Coroutine, TypeVar
    from typing_extensions import ParamSpec

    _P = ParamSpec("_P")
    _T = TypeVar("_T")

import inspect


async def call_maybe_coroutine(
    callable: Callable[_P, _T | Awaitable[_T]],
    *args: _P.args,
    **kwargs: _P.kwargs,
) -> _T:
    object = callable(*args, **kwargs)

    if inspect.isawaitable(object):
        object = await object

    return object


__all__ = [
    "call_maybe_coroutine",
]
