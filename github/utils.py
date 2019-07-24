"""
/github/utils.py

    Copyright (c) 2019 ShineyDev
    
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

import datetime
import re
import typing


ISO_REGEX = r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})Z"


def get(iterable: typing.Iterable, **attributes):
    """
    A helper that returns the first element in the iterable that meets
    all the traits passed in ``attributes``.

    .. note::

        When multiple attributes are specified, they are checked using
        logical AND, not logical OR. Meaning they have to meet every
        attribute passed in and not one of them.

    If nothing is found that matches the attributes passed, then
    ``None`` is returned.

    Parameters
    ----------
    iterable
        An iterable to search through.
    \\*\\*attributes
        Keyword arguments that denote attributes to search with.
    """

    for (i) in iterable:
        for (k, v) in attributes.items():
            try:
                if getattr(i, k) == v:
                    return i
            except (AttributeError) as e:
                pass

def datetime_to_iso(dt: datetime.datetime) -> str:
    """
    Converts a datetime object to ISO-8601.

    Parameters
    ----------
    dt: :class:`datetime.datetime`
        A datetime object.

    Returns
    -------
    :class:`str`
        An ISO-8601 string.
    """
    
    iso_format = "%Y-%m-%dT%H:%M:%SZ"
    iso = dt.strftime(iso_format)
    return iso

def iso_to_datetime(iso: str) -> datetime.datetime:
    """
    Converts ISO-8601 to a datetime object.

    Parameters
    ----------
    iso: :class:`str`
        An ISO-8601 string.

    Returns
    -------
    :class:`datetime.datetime`
        A datetime object.
    """

    match = re.fullmatch(ISO_REGEX, iso)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hour = int(match.group(4))
        minute = int(match.group(5))
        second = int(match.group(6))

        return datetime.datetime(year, month, day, hour, minute, second)

def hex_to_rgb(hex: str) -> typing.Tuple[int, int, int]:
    ... # going to remove this in a very-soon future commit
