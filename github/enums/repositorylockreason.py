"""
/github/enums/repositorylockreason.py

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

class RepositoryLockReason():
    """
    Represents the reason for a given repository to be in a locked state.

    https://developer.github.com/v4/enum/repositorylockreason/
    """

    __slots__ = ("_lock_reason",)

    def __init__(self, lock_reason):
        self._lock_reason = lock_reason

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} '{0._lock_reason}'>".format(self)

    @classmethod
    def from_data(cls, lock_reason):
        return cls(lock_reason)

    @property
    def billing(self) -> bool:
        """
        The repository is locked for a billing-related reason.
        """

        return self._lock_reason == "BILLING"

    @property
    def migrating(self) -> bool:
        """
        The repository is locked due to a migration.
        """

        return self._lock_reason == "MIGRATING"

    @property
    def moving(self) -> bool:
        """
        The repository is locked due to a move.
        """

        return self._lock_reason == "MOVING"

    @property
    def rename(self) -> bool:
        """
        The repository is locked due to a rename.
        """

        return self._lock_reason == "RENAME"
