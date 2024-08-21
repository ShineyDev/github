from __future__ import annotations
from typing import Generic, TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections import OrderedDict
    from collections.abc import Callable, Generator
    from typing import Any, overload
    from typing_extensions import TypeAlias, ParamSpec, Self

    _P = ParamSpec("_P")
    _T = TypeVar("_T")
    _U = TypeVar("_U")

    _Generator: TypeAlias = Generator[_T, None, Any]
    _GeneratorFunc: TypeAlias = Callable[_P, Generator[_T, None, Any]]

import collections

from .typing import MISSING


def _make_key(
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
) -> int:
    return hash((args, frozenset(kwargs.items())))


if TYPE_CHECKING:

    @overload
    def cache_generator(
        wrapped: _GeneratorFunc[_P, _T],
        /,
    ) -> _GeneratorFunc[_P, _T]: ...

    @overload
    def cache_generator(
        *,
        max_size: int | None = ...,
    ) -> Callable[[_GeneratorFunc[_P, _T]], _GeneratorFunc[_P, _T]]: ...

    @overload
    def cache_generator(
        *,
        max_size: int | None = ...,
        wrapper: Callable[[_Generator[_T]], _U],
    ) -> Callable[[_GeneratorFunc[_P, _T]], Callable[_P, _U]]: ...


def cache_generator(
    wrapped: _GeneratorFunc[_P, _T] = MISSING,
    /,
    *,
    max_size: int | None = MISSING,
    wrapper: Callable[[_Generator[_T]], _U] = MISSING,
) -> _GeneratorFunc[_P, _T] | Callable[[_GeneratorFunc[_P, _T]], _GeneratorFunc[_P, _T]] | Callable[[_GeneratorFunc[_P, _T]], Callable[_P, _U]]:
    max_size = max_size if max_size is not MISSING else 1024

    if isinstance(max_size, int):
        if max_size < -1 or max_size == 0:
            raise ValueError("max_size must be None, -1, or a positive integer")

    if wrapper is not MISSING:

        def decorator_wrapper(
            wrapped: _GeneratorFunc[_P, _T],
            /,
        ) -> Callable[_P, _U]:
            cache: Cache[int, _U] | None

            if max_size == -1 or max_size is None:
                cache = Cache()
            else:
                cache = LRUCache(max_size=max_size)

            def inner(
                *args: _P.args,
                **kwargs: _P.kwargs,
            ) -> _U:
                key = _make_key(args, kwargs)

                if key not in cache:
                    cache[key] = wrapper(wrapped(*args, **kwargs))

                return cache[key]

            inner.__utility_cache__ = cache

            return inner

        return decorator_wrapper

    else:

        def decorator(
            wrapped: _GeneratorFunc[_P, _T],
            /,
        ) -> _GeneratorFunc[_P, _T]:
            cache: Cache[int, tuple[Generator[_T, None, Any], list[_T], bool]]

            if max_size == -1 or max_size is None:
                cache = Cache()
            else:
                cache = LRUCache(max_size=max_size)

            def inner(
                *args: _P.args,
                **kwargs: _P.kwargs,
            ) -> Generator[_T, None, Any]:
                key = _make_key(args, kwargs)

                if key not in cache:
                    generator = wrapped(*args, **kwargs)
                    cache[key] = (generator, list(), False)

                generator, items, done = cache[key]

                i = 0  # NOTE: this garbage is all required to support multiple entries before exit
                while i < len(items):
                    yield items[i]
                    i += 1

                if not done:
                    i = 0
                    for item in generator:
                        items.append(item)
                        yield item
                        i += 1

                        if cache[key][2]:
                            yield from items[i:]
                            return

                    cache[key] = (MISSING, items, True)

            inner.__utility_cache__ = cache

            return inner

        if wrapped is MISSING:
            return decorator

        return decorator(wrapped)


_K = TypeVar("_K")
_V = TypeVar("_V")


class Cache(Generic[_K, _V]):
    """
    TODO
    """

    __slots__ = ("_cache", "hits", "misses")

    def __init__(
        self: Self,
        /,
    ) -> None:
        self._cache: dict[_K, _V] = dict()

        self.hits: int = 0
        self.misses: int = 0

    def __contains__(
        self: Self,
        key: _K,
    ) -> bool:
        return key in self._cache

    def __delitem__(
        self: Self,
        key: _K,
        /,
    ) -> None:
        try:
            del self._cache[key]
        except KeyError:
            raise

    def __getitem__(
        self: Self,
        key: _K,
        /,
    ) -> _V:
        try:
            value = self._cache[key]
        except KeyError:
            self.misses += 1
            raise
        else:
            self.hits += 1
            return value

    def __setitem__(
        self: Self,
        key: _K,
        value: _V,
        /,
    ) -> None:
        self._cache[key] = value

    def __len__(
        self: Self,
        /,
    ) -> int:
        return len(self._cache)

    @property
    def size(
        self: Self,
        /,
    ) -> int:
        return len(self)

    def clear(
        self: Self,
        /,
    ) -> None:
        """
        Clears the cache.
        """

        self._cache.clear()

    def reset(
        self: Self,
        /,
    ) -> None:
        """
        Resets the cache.
        """

        self.clear()

        self.hits = 0
        self.misses = 0


class SizedCache(Cache[_K, _V]):
    """
    TODO
    """

    __slots__ = ("_max_size",)

    def __init__(
        self: Self,
        /,
        *,
        max_size: int,
    ) -> None:
        self._max_size: int = MISSING

        self.max_size = max_size

    @property
    def max_size(
        self: Self,
        /,
    ) -> int:
        return self._max_size

    @max_size.setter
    def max_size(
        self: Self,
        value: int,
        /,
    ) -> None:
        if value < 0:
            raise ValueError("max_size must be 0 or a positive integer")

        self._max_size = value


class LRUCache(SizedCache[_K, _V]):
    """
    TODO
    """

    __slots__ = ()

    def __init__(
        self: Self,
        /,
        *,
        max_size: int,
    ) -> None:
        super().__init__(max_size=max_size)

        self._cache: OrderedDict[_K, _V] = collections.OrderedDict()

    def __getitem__(self, key: _K) -> _V:
        try:
            value = super().__getitem__(key)
        except KeyError:
            raise
        else:
            self._cache.move_to_end(key)
            return value

    def __setitem__(self, key: _K, value: _V) -> None:
        if key in self._cache.keys():
            self._cache.move_to_end(key)

        super().__setitem__(key, value)

        while len(self._cache) > self.max_size:
            self._cache.popitem(last=False)


__all__ = [
    "cache_generator",
    "Cache",
    "SizedCache",
    "LRUCache",
]
