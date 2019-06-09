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

class RateLimit(DataStore):
    def __repr__(self):
        return "<{0} limit={1} remaining={2} reset={3}>".format(
            self.__class__.__name__, self.limit, self.remaining, self.reset.timestamp())
    
    @classmethod
    def from_data(cls, data: dict):
        if (data is None):
            return None

        data_ = {
            "_data"    : data,
            "limit"    : data.get("limit"),
            "remaining": data.get("remaining"),
            "reset"    : utils.snowflake_to_datetime(data.get("limit")),
        }

        return cls(**data_)