"""
/github/enums/cannotupdatereason.py

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


class CannotUpdateReason():
    """
    Represents a reason the authenticated user cannot update a comment.

    https://developer.github.com/v4/enum/commentcannotupdatereason/
    """

    __slots__ = ("data",)

    def __init__(self, reason):
        self._reason = reason

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} '{0._reason}'>".format(self)

    @classmethod
    def from_data(cls, data):
        reasons = list()

        for (reason) in data:
            reasons.append(cls(reason))

        return reasons

    @property
    def archived(self) -> bool:
        """
        You cannot update this comment because the repository is archived.
        """

        return self._reason == "ARCHIVED"

    @property
    def denied(self) -> bool:
        """
        You cannot update this comment.
        """

        return self._reason == "DENIED"

    @property
    def insufficient_access(self) -> bool:
        """
        You must be the author or have write access to update this comment.
        """

        return self._reason == "INSUFFICIENT_ACCESS"

    @property
    def locked(self) -> bool:
        """
        You cannot update this comment because the issue is locked.
        """

        return self._reason == "LOCKED"

    @property
    def maintenance(self) -> bool:
        """
        You cannot update this comment because the repository is under maintenance.
        """

        return self._reason == "MAINTENANCE"

    @property
    def login_required(self) -> bool:
        """
        You must be logged in to update this comment.
        """

        return self._reason == "LOGIN_REQUIRED"

    @property
    def verified_email_required(self) -> bool:
        """
        At least one email address must be verified to update this comment.
        """

        return self._reason == "VERIFIED_EMAIL_REQUIRED"
    