"""
/github/abc/minimizable.py

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

from github.enums import MinimizeReason


class Minimizable():
    """
    Represents an entity that can be minimized.
    """

    __slots__ = ()

    @property
    def is_minimized(self):
        """
        Whether the minimizable is minimized.

        :type: :class:`bool`
        """

        return self.data["isMinimized"]

    @property
    def minimize_reason(self):
        """
        The reason for the minimizable being minimized.

        :type: :class:`~github.enums.MinimizeReason`
        """

        minimize_reason = self.data["minimizedReason"]
        return MinimizeReason.try_value(minimize_reason)

    @property
    def viewer_can_minimize(self):
        """
        Whether the authenticated user can minimize the minimizable.

        :type: :class:`bool`
        """

        return self.data["viewerCanMinimize"]
