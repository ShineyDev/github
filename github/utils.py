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
import functools
import re


# https://developer.github.com/v4/scalar/datetime/
# https://developer.github.com/v4/scalar/precisedatetime/
ISO_8601_DATETIME_REGEX = r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(?:\.([0-9]{3}))?Z"


class _cached_property:
    """
    Similar to the :class:`property` decorator, with the addition of
    computing its value only once.

    Essentially :func:`functools.cached_property` without the
    version-lock, the property-to-attribute cache and thus its
    ``__dict__`` limitation.
    """

    class _sentinel: pass

    def __init__(self, func):
        functools.update_wrapper(self, func)

        self.func = func
        self.value = self._sentinel

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        if self.value is self._sentinel:
            self.value = self.func(instance)

        return self.value


def iso_to_datetime(iso):
    """
    Converts ISO-8601 to a datetime object.

    Parameters
    ----------
    iso: Optional[:class:`str`]
        An ISO-8601 string.

    Returns
    -------
    Optional[:class:`~datetime.datetime`]
        A datetime object.
    """

    if iso is None:
        return None

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
