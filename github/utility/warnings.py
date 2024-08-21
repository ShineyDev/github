from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any

import warnings

import github


def changing(
    callable: Any | None = None,  # TODO
    /,
    *,
    what: str | None = None,
    when: str | None = None,
    where: str | None = None,
    who: type[Warning] | None = None,
    why: str | None = None,
) -> Any:  # TODO
    if when:
        who = who or github.ServerDeprecationWarning
        when = f"on {when}"
    else:
        who = who or github.ClientDeprecationWarning
        when = "in the next prime version"

    def decorator(callable):
        message = f"{what or callable.__qualname__} will change {when}"

        if where:
            message += f", use {where} instead."
        else:
            message += "."

        if why:
            message += f" {why}."

        @github.utility.wrap(callable)
        def wrapper(*args, **kwargs):
            warn_once(message, who, 2)
            return callable(*args, **kwargs)

        return wrapper

    if callable:
        return decorator(callable)
    else:
        return decorator


def deprecated(
    callable: Any | None = None,  # TODO
    *,
    what: str | None = None,
    when: str | None = None,
    where: str | None = None,
    who: type[Warning] | None = None,
    why: str | None = None,
) -> Any:  # TODO
    if when:
        who = who or github.ServerDeprecationWarning
        when = f"on {when}"
    else:
        who = who or github.ClientDeprecationWarning
        when = "in the next prime version"

    def decorator(callable):
        message = f"{what or callable.__qualname__} will be removed {when}"

        if where:
            message += f", use {where} instead."
        else:
            message += "."

        if why:
            message += f" {why}."

        @github.utility.wrap(callable)
        def wrapper(*args, **kwargs):
            warn_once(message, who, 2)
            return callable(*args, **kwargs)

        return wrapper

    if callable:
        return decorator(callable)
    else:
        return decorator


def warn(
    message: str,
    /,
    cls: type[Warning],
    level: int = 1,
) -> None:
    warnings.warn(message, cls, level + 1)


_warning_hashes: set[int] = set()


def warn_once(
    message: str,
    /,
    cls: type[Warning],
    level: int = 1
) -> None:
    h = hash((cls, message))

    if h not in _warning_hashes:
        warn(message, cls, level + 1)
        _warning_hashes.add(h)


__all__: list[str] = [
    "changing",
    "deprecated",
    "warn",
    "warn_once",
]
