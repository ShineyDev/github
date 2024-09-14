from __future__ import annotations
from typing import TYPE_CHECKING, Dict, TypeVar

if TYPE_CHECKING:
    from typing import Any
    from typing_extensions import Self

from github.core.errors import ClientObjectMissingFieldError


if TYPE_CHECKING:
    from github.utility.types import T_json_key, T_json_value

    _K = TypeVar("_K", bound=T_json_key)
    _V = TypeVar("_V", bound=T_json_value)
else:
    _K = TypeVar("_K")
    _V = TypeVar("_V")


def wrap(
    wrapped: Any,  # TODO
) -> Any:  # TODO
    def decorator(wrapper):
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__name__ = wrapped.__name__
        wrapper.__qualname__ = wrapped.__qualname__

        return wrapper

    return decorator


class DataWrapper(Dict[_K, _V]):
    def __getitem__(
        self: Self,
        key: _K,
        /,
    ) -> _V:
        try:
            return super().__getitem__(key)
        except KeyError:
            raise ClientObjectMissingFieldError(key) from None


__all__: list[str] = [
    "wrap",
    "DataWrapper",
]
