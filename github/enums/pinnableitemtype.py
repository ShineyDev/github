"""
/github/enums/pinnableitemtype.py

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


class PinnableItemType(Enum):
    """
    Represents a pinnable item type.
    """

    #: A :class:`~github.Gist`.
    gist = "GIST"

    #: An :class:`~github.Issue`.
    issue = "ISSUE"

    #: An :class:`~github.Organization`.
    organization = "ORGANIZATION"

    #: A :class:`~github.Project`.
    project = "PROJECT"

    #: A :class:`~github.PullRequest`.
    pull_request = "PULL_REQUEST"

    #: A :class:`~github.Repository`.
    repository = "REPOSITORY"

    #: A :class:`~github.Team`.
    team = "TEAM"

    #: A :class:`~github.User`.
    user = "USER"
