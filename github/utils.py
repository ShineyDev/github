import base64
import struct


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


def _database_to_cursor(id):
    cursor = b"cursor:v2:\x91\xCE" + struct.pack(">I", id)
    return base64.b64encode(cursor).decode("utf-8")


__all__ = []
