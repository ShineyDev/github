import base64
import datetime
import functools
import operator
import struct
import warnings

import github


def date_to_iso(d):
    return d.strftime(f"%Y-%m-%d")


def datetime_to_iso(dt):
    offset = dt.utcoffset()

    if offset is None:
        _warn_once(
            "using timezone-unaware datetime is not recommended, use aware datetime instead. for example, use datetime.now(timezone.utc) instead of "
            "datetime.utcnow(). assuming UTC for now.",
            github.errors.ClientDeprecationWarning,
            2,
        )

    if not offset:
        offset = "Z"
    else:
        if offset < datetime.timedelta(0):
            sign = "-"
            offset = -offset
        else:
            sign = "+"

        hours, rest = divmod(offset, datetime.timedelta(hours=1))
        minutes, rest = divmod(rest, datetime.timedelta(minutes=1))

        if rest:
            _warn_once(
                "using timezone with second or millisecond offset is not allowed. truncating to hours and minutes.",
                github.errors.ClientDeprecationWarning,
                2,
            )

        offset = f"{sign}{hours:>02}:{minutes:>02}"

    return dt.strftime(f"%Y-%m-%dT%H:%M:%S{offset}")


def iso_to_datetime(iso):
    return datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))


def iso_to_date(iso):
    return datetime.date.fromisoformat(iso)


# TODO: use next ids


def _cursor_to_database(cursor):
    cursor = base64.b64decode(cursor)
    name, version, msgpack = cursor.split(b":")
    return struct.unpack_from(">I", msgpack, 2)[0]


# def _cursor_to_node(cursor, type):
#     return _database_to_node(_cursor_to_database(cursor), type)


def _database_to_cursor(id):
    cursor = b"cursor:v2:\x91\xCE" + struct.pack(">I", id)
    return base64.b64encode(cursor).decode("utf-8")


# def _database_to_node(id, type):
#     return base64.b64encode(f"0{len(type)}:{type}{id}".encode("utf-8")).decode("utf-8")
#
#
# def _node_to_cursor(id):
#     return _database_to_cursor(_node_to_database(id))
#
#
# _bad_types = frozenset({"CodeOfConduct", "Gist"})
#
#
# def _node_to_database(id):
#     id = base64.b64decode(id).decode("utf-8")[1:]
#     length, id = id.split(":")
#     length = int(length)
#     type, id = id[:length], id[length:]
#
#     if type in _bad_types:
#         raise ValueError(f"node id of type '{type}' does not contain database id, got {id}")
#
#     return int(id)


_empty_dict = dict()


def _get_defined_graphql_fields(type):
    try:
        d_fields = type._graphql_fields
    except AttributeError:
        d_fields = _empty_dict
    else:
        if isinstance(d_fields, dict):
            d_fields = d_fields.copy()
        else:
            d_fields = {f: f for f in d_fields}

    for type in type.__bases__:
        for (key, value) in _get_defined_graphql_fields(type).items():
            if key not in d_fields.keys():
                d_fields[key] = value

    return d_fields


def _get_merged_graphql_fields(type, r_fields=None):
    d_fields = _get_defined_graphql_fields(type)

    if r_fields is None:
        return list(d_fields.values())

    if "__typename" not in r_fields:
        r_fields += ("__typename",)

    r_fields = list(r_fields)
    for (i, r_field) in enumerate(r_fields):
        try:
            r_field = d_fields[r_field]
        except KeyError:
            pass
        else:
            r_fields[i] = r_field

    return r_fields


_empty_list = list()


def _get_defined_repr_fields(type):
    try:
        d_fields = type._repr_fields.copy()
    except AttributeError:
        d_fields = _empty_list

    for type in type.__bases__:
        for element in _get_defined_repr_fields(type):
            if element not in d_fields:
                d_fields.append(element)

    return sorted(d_fields)


def _changing(callable=None, *, what=None, when=None, where=None, who=None, why=None):
    if when:
        who = who or github.errors.ServerDeprecationWarning
        when = f"on {when}"
    else:
        who = who or github.errors.ClientDeprecationWarning
        when = "in the next prime version"

    def decorator(callable):
        what_ = what or callable.__qualname__

        message = f"{what_} will change {when}"

        if where:
            message += f", use {where} instead."
        else:
            message += "."

        if why:
            message += f" {why}."

        @_wrap(callable)
        def wrapper(*args, **kwargs):
            _warn_once(message, who, 2)
            return callable(*args, **kwargs)

        return wrapper

    if callable:
        return decorator(callable)
    else:
        return decorator


def _deprecated(callable=None, *, what=None, when=None, where=None, who=None, why=None):
    if when:
        who = who or ServerDeprecationWarning
        when = f"on {when}"
    else:
        who = who or ClientDeprecationWarning
        when = "in the next prime version"

    def decorator(callable):
        what_ = what or callable.__qualname__

        message = f"{what_} will be removed {when}"

        if where:
            message += f", use {where} instead."
        else:
            message += "."

        if why:
            message += f" {why}."

        @_wrap(callable)
        def wrapper(*args, **kwargs):
            _warn_once(message, who, 2)
            return callable(*args, **kwargs)

        return wrapper

    if callable:
        return decorator(callable)
    else:
        return decorator


def _warn(message, cls, level=1):
    warnings.warn(message, cls, level + 1)


_warning_hashes = set()


def _warn_once(message, cls, level=1):
    h = hash((cls, message))

    if h not in _warning_hashes:
        _warn(message, cls, level + 1)
        _warning_hashes.add(h)


def _wrap(wrapped):
    def decorator(wrapper):
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__name__ = wrapped.__name__
        wrapper.__qualname__ = wrapped.__qualname__

        return wrapper

    return decorator


def _follow(data, path):
    return functools.reduce(operator.getitem, path, data)


__all__ = []
