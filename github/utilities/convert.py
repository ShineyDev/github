from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from github.utilities.typing import Date, DateTime

import base64
import datetime
import struct

import github


def date_to_iso(
    obj: Date,
    /,
) -> str:
    return obj.strftime("%Y-%m-%d")


def datetime_to_iso(
    obj: DateTime,
    /,
) -> str:
    offset = obj.utcoffset()

    if offset is None:
        github.utilities.warn_once(
            "using timezone-unaware datetime is not recommended, use aware datetime instead. for example, use datetime.now(timezone.utc) instead of "
            "datetime.utcnow(). assuming UTC for now.",
            github.ClientDeprecationWarning,
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
            github.utilities.warn_once(
                "using timezone with second or millisecond offset is not allowed. truncating to hours and minutes.",
                github.ClientDeprecationWarning,
                2,
            )

        offset = f"{sign}{hours:>02}:{minutes:>02}"

    return obj.strftime(f"%Y-%m-%dT%H:%M:%S{offset}")


def iso_to_date(
    iso: str,
    /,
) -> Date:
    return datetime.date.fromisoformat(iso)


def iso_to_datetime(
    iso: str,
    /,
) -> DateTime:
    return datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))


def cursor_to_database(
    cursor: str,
    /,
) -> int:
    _, _, msgpack = base64.b64decode(cursor).split(b":")
    return struct.unpack_from(">I", msgpack, 2)[0]


def cursor_to_node(
    cursor: str,
    type: str,
    /,
) -> str:
    return database_to_node(cursor_to_database(cursor), type)


def database_to_cursor(
    id: int,
    /,
) -> str:
    cursor = b"cursor:v2:\x91\xCE" + struct.pack(">I", id)
    return base64.b64encode(cursor).decode("utf-8")


def database_to_node(
    id: int,
    type: str,
    /,
) -> str:
    return base64.b64encode(f"0{len(type)}:{type}{id}".encode("utf-8")).decode("utf-8")


def node_to_cursor(
    id: str,
    /,
) -> str:
    return database_to_cursor(node_to_database(id))


_bad_node_types: frozenset[str] = frozenset({"CodeOfConduct", "Gist"})


def node_to_database(
    id: str,
    /,
) -> int:
    id = base64.b64decode(id).decode("utf-8")[1:]
    length, id = id.split(":")
    length = int(length)
    type, id = id[:length], id[length:]

    if type in _bad_node_types:
        raise ValueError(f"node id of type '{type}' does not contain database id, got {id}")

    return int(id)


__all__: list[str] = [
    "date_to_iso",
    "datetime_to_iso",
    "iso_to_date",
    "iso_to_datetime",
    "cursor_to_database",
    "cursor_to_node",
    "database_to_cursor",
    "database_to_node",
    "node_to_cursor",
    "node_to_database",
]
