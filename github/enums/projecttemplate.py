"""
/github/enums/projecttemplate.py

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


class ProjectTemplate(Enum):
    """
    Represents a template used to create a :class:`~github.Project`.
    """

    #: A project with columns for "to do", "in progress", and "done".
    kanban = "BASIC_KANBAN"

    #: :attr:`.kanban` plus automation.
    kanban_automation = "AUTOMATED_KANBAN_V2"

    #: :attr:`.kanban_automation` plus pull request review automation.
    kanban_automation_reviews = "AUTOMATED_REVIEWS_KANBAN"

    #: A project with columns for "to do", "high priority",
    #: "low priority", and "closed".
    triage = "BUG_TRIAGE"
