"""
/github/utils.py

    Copyright (c) 2019-2020 ShineyDev

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import base64
import datetime
import inspect
import struct


def cursor_to_database(cursor):
    cursor = base64.b64decode(cursor)
    name, version, msgpack = cursor.split(b":")
    return struct.unpack_from(">I", msgpack, 2)[0]

def database_to_cursor(id):
    msgpack = b"\x91\xCE" + struct.pack(">I", id)
    cursor = b"cursor:v2:" + msgpack
    return base64.b64encode(cursor)

def datetime_to_iso(dt):
    offset = dt.utcoffset()
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
    if iso is None:
        return None

    return datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))

def iso_to_date(iso):
    if iso is None:
        return None

    return datetime.date.fromisoformat(iso)

async def maybe_coro(callable, *args, **kwargs):
    result = callable(*args, **kwargs)

    if inspect.iscoroutine(result):
        result = await result

    return result
