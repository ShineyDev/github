"""
/github/objects/ratelimit.py

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

from github import utils
from github.abc import Type


class RateLimit(Type):
    """
    Represents the viewer's rate limit.

    https://developer.github.com/v4/object/ratelimit/

    Implements:

    * :class:`~github.abc.Type`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} limit={0.limit} remaining={0.remaining}>".format(self)

    @classmethod
    def from_data(cls, data):
        return cls(data)

    @property
    def limit(self) -> int:
        """
        The maximum number of points the viewer is permitted to consume in a rate limit window.
        """

        return self.data["limit"]

    @property
    def remaining(self) -> int:
        """
        The number of points remaining in the current rate limit window.
        """

        return self.data["remaining"]

    @property
    def reset_at(self) -> datetime.datetime:
        """
        The date and time at which the current rate limit window resets in UTC.
        """

        reset_at = self.data["resetAt"]
        return utils.iso_to_datetime(reset_at)
