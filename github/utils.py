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

import datetime
import re
import typing


ISO_8601_DATETIME_REGEX = r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(?:\.([0-9]{3}))?Z"


def find(iterable: typing.Iterable, predicate: typing.Callable) -> typing.Optional[typing.Any]:
    """
    A helper that returns the first element in the iterable that meets
    the predicate.

    If nothing is found that meets the predicate, then ``None`` is
    returned.

    Parameters
    ----------
    iterable
        An iterable to search through.
    predicate
        A callable which takes one parameter and returns a boolean.

    Returns
    -------
    Optional[Any]
        The element that met the predicate.
    """

    l = find_all(iterable, predicate)
    return l[0] if l else None

def find_all(iterable: typing.Iterable, predicate: typing.Callable) -> typing.List[typing.Any]:
    """
    A helper that returns all elements in the iterable that meet the
    predicate.

    If nothing is found that meets the predicate, then an empty list is
    returned.

    Parameters
    ----------
    iterable
        An iterable to search through.
    predicate
        A callable which takes one parameter and returns a boolean.

    Returns
    -------
    List[Any]
        The elements that met the predicate.
    """

    l = list()

    for (i) in iterable:
        if predicate(i):
            l.append(i)

    return l

def get(iterable: typing.Iterable, **attributes) -> typing.Optional[typing.Any]:
    """
    A helper that returns the first element in the iterable that meets
    all of the traits passed in ``attributes``.

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

    Returns
    -------
    Optional[Any]
        The element that met all traits passed in ``attributes``.
    """

    l = get_all(iterable, **attributes)
    return l[0] if l else None

def get_all(iterable: typing.Iterable, **attributes) -> typing.List[typing.Any]:
    """
    A helper that returns all elements in the iterable that meet all
    of the traits passed in ``attributes``.

    .. note::

        When multiple attributes are specified, they are checked using
        logical AND, not logical OR. Meaning they have to meet every
        attribute passed in and not one of them.

    If nothing is found that matches the attributes passed, then an 
    empty list is returned.

    Parameters
    ----------
    iterable
        An iterable to search through.
    \\*\\*attributes
        Keyword arguments that denote attributes to search with.

    Returns
    -------
    List[Any]
        The elements that met all traits passed in ``attributes``.
    """

    l = list()

    for (i) in iterable:
        try:
            if all([getattr(i, k) == v for (k, v) in attributes.items()]):
                l.append(i)
        except (AttributeError) as e:
            pass

    return l

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

    # https://developer.github.com/v4/scalar/datetime/
    # https://developer.github.com/v4/scalar/precisedatetime/
    match = re.fullmatch(ISO_8601_DATETIME_REGEX, iso)
    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        day = int(match.group(3))
        hour = int(match.group(4))
        minute = int(match.group(5))
        second = int(match.group(6))
        microsecond = int(match.group(7) or 0) * 1000

        return datetime.datetime(year, month, day, hour, minute, second, microsecond)
