import warnings

import github


def changing(callable=None, *, what=None, when=None, where=None, who=None, why=None):
    if when:
        who = who or github.errors.ServerDeprecationWarning
        when = f"on {when}"
    else:
        who = who or github.errors.ClientDeprecationWarning
        when = "in the next prime version"

    def decorator(callable):
        message = f"{what or callable.__qualname__} will change {when}"

        if where:
            message += f", use {where} instead."
        else:
            message += "."

        if why:
            message += f" {why}."

        @github.utilities.wrap(callable)
        def wrapper(*args, **kwargs):
            warn_once(message, who, 2)
            return callable(*args, **kwargs)

        return wrapper

    if callable:
        return decorator(callable)
    else:
        return decorator


def deprecated(callable=None, *, what=None, when=None, where=None, who=None, why=None):
    if when:
        who = who or github.errors.ServerDeprecationWarning
        when = f"on {when}"
    else:
        who = who or github.errors.ClientDeprecationWarning
        when = "in the next prime version"

    def decorator(callable):
        message = f"{what or callable.__qualname__} will be removed {when}"

        if where:
            message += f", use {where} instead."
        else:
            message += "."

        if why:
            message += f" {why}."

        @github.utilities.wrap(callable)
        def wrapper(*args, **kwargs):
            warn_once(message, who, 2)
            return callable(*args, **kwargs)

        return wrapper

    if callable:
        return decorator(callable)
    else:
        return decorator


def warn(message, cls, level=1):
    warnings.warn(message, cls, level + 1)


_warning_hashes = set()


def warn_once(message, cls, level=1):
    h = hash((cls, message))

    if h not in _warning_hashes:
        warn(message, cls, level + 1)
        _warning_hashes.add(h)


__all__ = [
    "changing",
    "deprecated",
    "warn",
    "warn_once",
]
