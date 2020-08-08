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


# https://docs.github.com/en/graphql/reference/scalars#datetime
# https://docs.github.com/en/graphql/reference/scalars#precisedatetime
ISO_8601_DATETIME_FMT = "{0:>04}-{1:>02}-{2:>02}T{3:>02}:{4:>02}:{5:>02}.{6:>03}Z"
ISO_8601_DATETIME_REGEX = r"([0-9]{4})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(?:\.([0-9]{3}))?Z"


def datetime_to_iso(dt):
    """
    Converts a datetime object to ISO-8601.

    Parameters
    ----------
    dt: :class:`~datetime.datetime`
        A datetime. object.

    Returns
    -------
    :class:`str`
        An ISO-8601 string.
    """

    return ISO_8601_DATETIME_FMT.format(dt.year, dt.month, dt.day,
                                        dt.hour, dt.minute, dt.second,
                                        dt.microsecond // 1000)

def iso_to_datetime(iso):
    """
    Converts ISO-8601 to a datetime object.

    Parameters
    ----------
    iso: :class:`str`
        An ISO-8601 string.

    Returns
    -------
    :class:`~datetime.datetime`
        A datetime object.
    """

    if iso is None:
        # internal helper
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

        return datetime.datetime(year, month, day,
                                 hour, minute, second,
                                 microsecond)
