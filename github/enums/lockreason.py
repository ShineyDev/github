"""
/github/enums/lockreason.py

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

class LockReason():
    """
    Represents the reason for a lockable to be in a locked state.

    https://developer.github.com/v4/enum/lockreason/
    """

    __slots__ = ("_reason",)

    def __init__(self, reason):
        self._reason = reason

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} '{0._reason}'>".format(self)

    @classmethod
    def from_data(cls, reason):
        return cls(reason)

    @property
    def off_topic(self) -> bool:
        """
        The lockable is locked because the conversation was off-topic.
        """

        return self._reason == "OFF_TOPIC"

    @property
    def resolved(self) -> bool:
        """
        The lockable is locked because the conversation was resolved.
        """

        return self._reason == "RESOLVED"

    @property
    def spam(self) -> bool:
        """
        The lockable is locked because the conversation was spam.
        """

        return self._reason == "SPAM"

    @property
    def too_heated(self) -> bool:
        """
        The lockable is locked because the conversation was too heated.
        """

        return self._reason == "TOO_HEATED"
