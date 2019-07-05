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
    for (i) in iterable:
        for (k, v) in attributes.items():
            try:
                if (getattr(i, k) == v):
                    return i
            except (AttributeError) as e:
                pass

def iso_to_datetime(iso: str) -> datetime.datetime:
    match = re.fullmatch(ISO_REGEX, iso)
    if (match):
        year = match.group(0)
        month = match.group(1)
        day = match.group(2)
        hour = match.group(3)
        minute = match.group(4)
        second = match.group(5)

        return datetime.datetime(year, month, day, hour, minute, second)