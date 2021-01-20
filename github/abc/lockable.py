"""
/github/abc/lockable.py

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

from github.enums import LockReason


class Lockable():
    """
    Represents an entity that can be locked.
    """

    __slots__ = ()

    @property
    def is_locked(self):
        """
        Whether the lockable is locked.

        :type: :class:`bool`
        """

        return self.data["locked"]

    @property
    def lock_reason(self):
        """
        The reason for the lockable being locked.

        :type: Optional[:class:`~github.enums.LockReason`]
        """

        lock_reason = self.data["activeLockReason"]
        return LockReason.try_value(lock_reason)
