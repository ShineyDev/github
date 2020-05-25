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

import typing

from github import utils
from github.enums import LockReason


class Lockable():
    """
    Represents an object which can be locked.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    # https://developer.github.com/v4/interface/lockable/

    __slots__ = ()

    @property
    def is_locked(self) -> bool:
        """
        Whether the lockable is locked.

        :type: :class:`bool`
        """

        return self.data["locked"]

    @utils._cached_property
    def lock_reason(self) -> typing.Optional[LockReason]:
        """
        The reason for the lockable being locked.

        :type: Optional[:class:`~github.enums.LockReason`]
        """

        reason = self.data["activeLockReason"]
        return LockReason.try_value(reason)

    async def lock(self, *, reason: LockReason=None):
        """
        |coro|

        Locks the lockable.

        Parameters
        ----------
        reason: Optional[:class:`~github.enums.Lockreason`]
            The reason for locking the lockable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to lock the lockable.
        """

        if reason is not None:
            reason = reason.value

        await self.http.lock(self.id, reason)

    async def unlock(self):
        """
        |coro|

        Unlocks the lockable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to unlock the lockable.
        """

        await self.http.unlock(self.id)

