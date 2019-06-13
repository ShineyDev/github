"""
/utils/abc.py

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

from . import (
    utils,
)


class DataStore():
    def __init__(self, **data):
        self._data = data
        for (key, value) in self._data.items():
            setattr(self, key, value)

    @classmethod
    def _from_data(cls, data: dict, *, current: dict=None,
                      overwrites: dict=None, defaults: dict=None,
                      converters: dict=None):

        current = current or dict()
        overwrites = overwrites or dict()
        defaults = defaults or dict()
        converters = converters or dict()

        current["_data"] = data

        for (key, value) in data.items():
            if (key in converters.keys()):
                converter = converters[key]
                if (isinstance(converter, tuple)):
                    converter, args, kwargs = converter
                    value = converter(value, *args, **kwargs)
                else:
                    value = converter(value)

            if (key in defaults.keys()):
                if (value is None):
                    value = defaults[key]

            if (key in overwrites.keys()):
                key = overwrites[key]

            current[key] = value

        for (key, value) in defaults.items():
            if (key not in current.keys()):
                current[key] = value

        return cls(**current)

class RateLimit(DataStore):
    def __repr__(self):
        return "<{0} limit={1} remaining={2} reset={3}>".format(
            self.__class__.__name__, self.limit, self.remaining, self.reset.timestamp())
    
    @classmethod
    def from_data(cls, data: dict):
        if (data is None):
            return None

        converters = {
            "reset": utils.snowflake_to_datetime,
        }

        return cls._from_data(data, converters=converters)