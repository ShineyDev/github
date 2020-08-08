"""
/github/objects/status.py

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

from github import utils
from github.abc import Node
from github.abc import Type


class Status(Node, Type):
    """
    Represents a GitHub user status.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    """

    # https://developer.github.com/v4/object/userstatus/

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def created_at(self):
        """
        When the status was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def emoji(self):
        """
        The status emoji.

        :type: Optional[:class:`str`]
        """

        return self.data["emoji"]

    @property
    def emoji_html(self):
        """
        The status emoji as HTML.

        :type: Optional[:class:`str`]
        """

        return self.data["emojiHTML"]

    @property
    def expires_at(self):
        """
        When the status will expire.

        :type: Optional[:class:`~datetime.datetime`]
        """

        expires_at = self.data["expiresAt"]
        return utils.iso_to_datetime(expires_at)

    @property
    def is_busy(self):
        """
        Whether the status marks the user as busy.

        :type: :class:`bool`
        """

        return self.data["indicatesLimitedAvailability"]

    @property
    def message(self):
        """
        The status message.

        :type: Optional[:class:`str`]
        """

        return self.data["message"]

    @property
    def updated_at(self):
        """
        When the status was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)
