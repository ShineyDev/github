"""
/utils/utils.py

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
import typing


def get(iterable: typing.Iterable, **attributes):
    for (i) in iterable:
        for (k, v) in attributes.items():
            try:
                if (getattr(i, k) == v):
                    return i
            except (AttributeError) as e:
                pass

def iso_to_datetime(iso: str) -> datetime.datetime:
    ...

def snowflake_to_datetime(timestamp: int) -> datetime.datetime:
    return datetime.datetime.utcfromtimestamp(timestamp)