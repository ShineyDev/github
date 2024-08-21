from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import TypeVar
    from typing_extensions import ParamSpec

    _P = ParamSpec("_P")
    _T = TypeVar("_T")


def wrap(
    wrapped: Callable[_P, _T],
    /,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    """
    TODO
    """

    def decorator(
        wrapper: Callable[_P, _T],
        /,
    ) -> Callable[_P, _T]:
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__name__ = wrapped.__name__
        wrapper.__qualname__ = wrapped.__qualname__
        wrapper.__wrapped__ = wrapped

        return wrapper

    return decorator


def wrap_fallback(
    wrapped: Callable[_P, _T],
    /,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    """
    TODO
    """

    def decorator(
        wrapper: Callable[_P, _T],
        /,
    ) -> Callable[_P, _T]:
        wrapper = wrap(wrapped)(wrapper)

        @wrap(wrapper)
        def inner(
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _T:
            try:
                return wrapper(*args, **kwargs)
            except Exception:
                return wrapped(*args, **kwargs)

        return inner

    return decorator


__all__ = [
    "wrap",
    "wrap_fallback",
]
