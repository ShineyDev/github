"""
/github/enums/milestoneorderfield.py

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


class MilestoneOrderField(Enum):
    """
    Represents fields by which you can order :class:`~github.Milestone`s.
    """

    #: :attr:`Milestone.created_at <github.Milestone.created_at>`
    created_at = "CREATED_AT"

    #: :attr:`Milestone.due_at <github.Milestone.due_at>`
    due_at = "DUE_DATE"

    #: :attr:`Milestone.number <github.Milestone.number>`
    number = "NUMBER"

    #: :attr:`Milestone.updated_at <github.Milestone.updated_at>`
    updated_at = "UPDATED_AT"
