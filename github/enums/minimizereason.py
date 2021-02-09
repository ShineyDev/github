"""
/github/enums/minimizereason.py

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


class MinimizeReason(Enum):
    """
    Represents a reason for minimizing a :class:`~github.abc.Minimizable`.
    """

    #: The content is abusive or harassive.
    abuse = "ABUSE"

    #: The content is a duplicate.
    duplicate = "DUPLICATE"

    #: The content is off-topic.
    off_topic = "OFF_TOPIC"

    #: The content is outdated.
    outdated = "OUTDATED"

    #: The content is resolved.
    resolved = "RESOLVED"

    #: The content is spam.
    spam = "SPAM"
