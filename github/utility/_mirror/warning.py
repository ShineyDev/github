from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Callable, TypeVar, overload
    from typing_extensions import ParamSpec

    from datetime import date

    _P = ParamSpec("_P")
    _T = TypeVar("_T")

import datetime
import pathlib
import warnings

from .typing import MISSING
from .version import SUPPORTS_WARNINGSKIPS
from .wrapper import wrap


if TYPE_CHECKING:

    @overload
    def deprecated(
        wrapped: Callable[_P, _T],
        /,
    ) -> Callable[_P, _T]: ...

    @overload
    def deprecated(
        *,
        condition: Callable[[tuple[Any], dict[str, Any]], bool] = MISSING,
        what: str = MISSING,
        when: date | str = MISSING,
        where: str = MISSING,
        who: type[Warning] = MISSING,
        why: str = MISSING,
    ) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]: ...


def deprecated(
    wrapped: Callable[_P, _T] = MISSING,
    /,
    *,
    condition: Callable[[tuple[Any, ...], dict[str, Any]], bool] = MISSING,
    what: str = MISSING,
    when: date | str = MISSING,
    where: str = MISSING,
    who: type[Warning] = MISSING,
    why: str = MISSING,
) -> Callable[_P, _T] | Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    """
    |decorator_dynamic|

    Marks a callable as deprecated, causing it to issue a warning when
    called.


    Parameters
    ----------
    condition: Callable[[tuple[Any, ...], dict[:class:`str`, Any]], :class:`bool`]
        A condition callable given `(args, kwargs)` that should return
        a boolean as to whether to issue the warning. Typically used to
        issue warnings only to users who use a deprecated parameter.
        Defaults to `(_, _) -> True`
    what: :class:`str`
        The name of the thing that is deprecated. Defaults to the name
        of the callable.
    when: :class:`~datetime.date` | :class:`str`
        The date on which the thing will be changed or removed.
        Defaults to the next major version.
    where: :class:`str`
        The name of a thing to use instead of the deprecated thing.
        Defaults to nothing.
    who: type[:class:`Warning`]
        The category of warning to issue.
    why: :class:`str`
        An arbitrary sentence to place at the end of the warning
        message. Typically the reason for the deprecation. Defaults to
        nothing.


    Examples
    --------

    Issue a deprecation warning for a renamed callable
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: python
        :emphasize-lines: 1

        @utility.deprecated(where="bar")
        def foo(*, a: str, b: int):
            ...


    Issue a deprecation warning for a renamed parameter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    .. code-block:: python
        :emphasize-lines: 1-5

        @utility.deprecated(
            condition=lambda args,kwargs: "a" in kwargs.keys(),
            what="foo(a=...)"
            where="foo(b=...)",
        )
        def foo(*, a: str = MISSING, b: int):
            ...
    """

    who = who if who is not MISSING else DeprecationWarning

    if when is not MISSING:
        if isinstance(when, datetime.date):
            when = when.strftime("%Y-%m-%d")

        when = f"on {when}"
    else:
        when = "in the next major version"

    def decorator(
        wrapped: Callable[_P, _T],
        /,
    ) -> Callable[_P, _T]:
        what_ = what if what is not MISSING else wrapped.__qualname__

        message = f"{what_} will be removed {when}"

        if where:
            message += f", use {where} instead."
        else:
            message += "."

        if why:
            message += f" {why}."

        @wrap(wrapped)
        def wrapper(
            *args: _P.args,
            **kwargs: _P.kwargs,
        ) -> _T:
            if condition is MISSING or condition(args, kwargs):
                warn_once(message, cls=who, level=2)

            return wrapped(*args, **kwargs)

        return wrapper

    if wrapped is not MISSING:
        return decorator(wrapped)
    else:
        return decorator


_warning_skips = (str(pathlib.Path(__file__).parent.parent),)


def warn(
    message: str,
    /,
    *,
    cls: type[Warning],
    level: int = 1,
) -> None:
    """
    TODO
    """

    if SUPPORTS_WARNINGSKIPS:
        warnings.warn(message, cls, 0, skip_file_prefixes=_warning_skips)  # type: ignore  # skip_file_prefixes does exist
    else:
        warnings.warn(message, cls, level + 1)


_warning_hashes: set[int] = set()


def warn_once(
    message: str,
    /,
    *,
    cls: type[Warning],
    level: int = 1,
) -> None:
    """
    TODO
    """

    warning_hash = hash((cls, message))

    if warning_hash not in _warning_hashes:
        _warning_hashes.add(warning_hash)
        warn(message, cls=cls, level=level + 1)


__all__ = [
    "deprecated",
    "warn",
    "warn_once",
]
