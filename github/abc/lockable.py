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

from github.enums import LockReason


class Lockable():
    """
    Represents an object which can be locked.

    https://developer.github.com/v4/interface/lockable/

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def is_locked(self) -> bool:
        """
        Whether or not the lockable is locked.
        """

        return self.data["locked"]

    @property
    def lock_reason(self) -> typing.Optional[LockReason]:
        """
        The reason for the lockable being locked.
        """

        reason = self.data["activeLockReason"]
        if reason:
            return LockReason.from_data(reason)

    async def lock(self, *, reason: str=None):
        """
        |coro|

        Locks the lockable.

        Parameters
        ----------
        reason: Optional[:class:`str`]
            The reason for locking the lockable. Can be one of
            ``"OFF_TOPIC"``, ``"RESOLVED"``, ``"SPAM"``,
            ``"TOO_HEATED"``.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to lock the lockable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The lockable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        await self.http.lock(self.id, reason)

    async def unlock(self):
        """
        |coro|

        Unlocks the lockable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to unlock the lockable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The lockable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        await self.http.unlock(self.id)

