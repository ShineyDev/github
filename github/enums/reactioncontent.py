"""
/github/enums/reactioncontent.py

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


class ReactionContent(Enum):
    """
    Represents the content of a :class:`~github.Reaction`.
    """

    #: The ``:confused:`` emoji.
    confused = "CONFUSED"

    #: The ``:eyes:`` emoji.
    eyes = "EYES"

    #: The ``:heart:`` emoji.
    heart = "HEART"

    #: The ``:hooray:`` emoji.
    hooray = "HOORAY"

    #: The ``:laugh:`` emoji.
    laugh = "LAUGH"

    #: The ``:rocket:`` emoji.
    rocket = "ROCKET"

    #: The ``:-1:`` emoji.
    thumbs_down = "THUMBS_DOWN"

    #: The ``:+1:`` emoji.
    thumbs_up = "THUMBS_UP"
