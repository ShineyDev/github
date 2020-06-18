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
from github.enums import RepositoryLockReason


class Lockable():
    """
    Represents an object which can be locked.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    * :class:`~github.Repository`
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

    @property
    def lock_reason(self):
        """
        The reason for the lockable being locked.

        :type: Union[:class:`~github.enums.LockReason`,
                     :class:`~github.enums.RepositoryLockReason`]
        """

        map = {
            "Issue": ("activeLockReason", LockReason),
            "PullRequest": ("activeLockReason", LockReason),
            "Repository": ("lockReason", RepositoryLockReason),
        }

        key, type = map[self.data["__typename"]]
        return type.try_value(self.data[key])

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

        # https://developer.github.com/v4/mutation/locklockable/

        if reason is not None:
            reason = reason.value

        await self.http.mutate_lockable_lock(self.id, reason)

    async def unlock(self):
        """
        |coro|

        Unlocks the lockable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to unlock the lockable.
        """

        # https://developer.github.com/v4/mutation/unlocklockable/

        await self.http.mutate_lockable_unlock(self.id)

