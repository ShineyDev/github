"""
/github/enums/lockreason.py

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


class LockReason(Enum):
    """
    Represents a reason for locking a
    :class:`~github.interfaces.Lockable`.
    """

    #: The conversation is off-topic.
    off_topic = "OFF_TOPIC"

    #: The conversation is resolved.
    resolved = "RESOLVED"

    #: The conversation is spam.
    spam = "SPAM"

    #: The conversation is too heated.
    too_heated = "TOO_HEATED"
