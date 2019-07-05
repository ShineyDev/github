"""
/github/objects/ratelimit.py

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

from github import utils


class RateLimit():
    """

    """

    def __init__(self, data):
        self.data = data

    @classmethod
    def from_data(cls, data):
        return cls(data["rateLimit"])

    @property
    def cost(self) -> int:
        """

        """

        return self.data.get("cost")

    @property
    def limit(self) -> int:
        """

        """

        return self.data.get("limit")

    @property
    def remaining(self) -> int:
        """

        """

        return self.data.get("remaining")

    @property
    def reset_at(self) -> datetime.datetime:
        """

        """

        return utils.iso_to_datetime(self.data.get("resetAt"))