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

from enum import Enum


class CannotUpdateReason(Enum):
    """
    Represents a reason for the authenticated user being unable to
    update an :class:`~github.interfaces.Updatable`.
    """

    #: The subject :class:`~github.Repository` is archived.
    archived = "ARCHIVED"

    #: The authenticated user cannot update the updatable.
    denied = "DENIED"

    #: The authenticated user does not have permission to update the
    #: updatable.
    insufficient_access = "INSUFFICIENT_ACCESS"

    #: The subject :class:`~github.Issue` or
    #: :class:`~github.PullRequest` is locked.
    locked = "LOCKED"

    #: There is no authenticated user.
    login_required = "LOGIN_REQUIRED"

    #: The subject :class:`~github.Repository` is under maintenance.
    maintenance = "MAINTENANCE"

    #: The authenticated user does not have a verified email.
    verified_email_required = "VERIFIED_EMAIL_REQUIRED"
