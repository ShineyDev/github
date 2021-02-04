"""
/github/enums/pullrequestorderfield.py

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


class PullRequestOrderField(Enum):
    """
    Represents fields by which you can order :class:`~github.PullRequest`s.
    """

    #: :attr:`PullRequest.created_at <github.PullRequest.created_at>`
    created_at = "CREATED_AT"

    #: :attr:`PullRequest.updated_at <github.PullRequest.updated_at>`
    updated_at = "UPDATED_AT"
