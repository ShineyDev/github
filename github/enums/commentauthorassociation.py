"""
/github/enums/commentauthorassociation.py

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


class CommentAuthorAssociation(Enum):
    """
    Represents an author's association with a subject of a
    :class:`.github.interfaces.Comment`.
    """

    #: The author is a collaborator on the subject
    #: :class:`~github.Repository`.
    collaborator = "COLLABORATOR"

    #: The author has previously contributed to the subject
    #: :class:`~github.Repository`.
    contributor = "CONTRIBUTOR"

    #: The author has not previously contributed to the subject
    #: :class:`~github.Repository`.
    first_time_contributor = "FIRST_TIME_CONTRIBUTOR"

    #: The author has not previously contributed to any GitHub
    #: repository.
    first_timer = "FIRST_TIMER"

    #: The author is a :class:`~github.Mannequin`.
    mannequin = "MANNEQUIN"

    #: The author is a member of the :class:`~github.Organization` that
    #: owns the subject :class:`~github.Repository`.
    member = "MEMBER"

    #: The author has no association with the subject
    #: :class:`~github.Repository`.
    none = "NONE"

    #: The author owns the subject :class:`~github.Repository`.
    owner = "OWNER"
