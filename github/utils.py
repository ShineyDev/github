import base64
import datetime
import struct
import warnings

import github


def datetime_to_iso(dt):
    offset = dt.utcoffset()

    if offset is None:
        _warn_once(
            "using timezone-unaware datetime is not recommended, use aware datetime instead. "
            "for example, use datetime.now(timezone.utc) instead of datetime.utcnow(). "
            "assuming UTC.",
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
        minutes, _ = divmod(rest, datetime.timedelta(minutes=1))

        offset = f"{sign}{hours:>02}:{minutes:>02}"

    return dt.strftime(f"%Y-%m-%dT%H:%M:%S{offset}")


def iso_to_datetime(iso):
    return datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))


_empty_list = list()


def _get_fields(type):
    try:
        fields = list(type._fields)
    except AttributeError:
        return _empty_list

    for type in type.__bases__:
        fields.extend(_get_fields(type))

    return fields


def _cursor_to_database(cursor):
    cursor = base64.b64decode(cursor)
    name, version, msgpack = cursor.split(b":")
    return struct.unpack_from(">I", msgpack, 2)[0]


def _cursor_to_node(cursor, type):
    return _database_to_node(_cursor_to_database(cursor), type)


def _database_to_cursor(id):
    cursor = b"cursor:v2:\x91\xCE" + struct.pack(">I", id)
    return base64.b64encode(cursor).decode("utf-8")


def _database_to_node(id, type):
    return base64.b64encode(f"0{len(type)}:{type}{id}".encode("utf-8")).decode("utf-8")


def _node_to_cursor(id):
    return _database_to_cursor(_node_to_database(id))


_bad_types = frozenset({"CodeOfConduct", "Gist"})


def _node_to_database(id):
    id = base64.b64decode(id).decode("utf-8")[1:]
    length, id = id.split(":")
    length = int(length)
    type, id = id[:length], id[length:]

    if type in _bad_types:
        raise ValueError(f"node id of type '{type}' does not contain database id, got {id}")

    return int(id)


def _warn(message, cls, level=1):
    warnings.warn(message, cls, level + 1)


_warning_hashes = set()


def _warn_once(message, cls, level=1):
    h = hash((cls, message))

    if h not in _warning_hashes:
        _warn(message, cls, level + 1)
        _warning_hashes.add(h)


__all__ = []
