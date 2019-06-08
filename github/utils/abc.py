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

import datetime

from . import (
    utils,
)


class RateLimitABC():
    def __init__(self, *, limit: int, remaining: int, reset: datetime.datetime):
        self.limit = limit
        self.remaining = remaining
        self.reset = reset

    def __repr__(self):
        return "<{0} limit={1} remaining={2} reset={3}>".format(
            self.__class__.__name__, self.limit, self.remaining, self.reset.timestamp())
    
    @classmethod
    def from_data(cls, data: dict):
        limit = data["limit"]
        remaining = data["remaining"]
        reset = utils.snowflake_time(data["reset"])

        return cls(limit=limit, remaining=remaining, reset=reset)