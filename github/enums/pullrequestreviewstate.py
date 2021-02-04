"""
/github/enums/pullrequestreviewstate.py

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


class PullRequestReviewState(Enum):
    """
    Represents the state of a :class:`~github.PullRequestReview`.
    """

    #: The review allows merging the pull request.
    approved = "APPROVED"

    #: The review disallows merging the pull request.
    changes_requested = "CHANGES_REQUESTED"

    #: The review does not explicitly allow or disallow merging the
    #: pull request.
    comment = "COMMENTED"

    #: The review has been dismissed.
    dismissed = "DISMISSED"

    #: The review is pending.
    pending = "PENDING"
