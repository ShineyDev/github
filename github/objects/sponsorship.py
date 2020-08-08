"""
/github/objects/sponsorship.py

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
from github.enums import SponsorshipPrivacy


class Sponsorship(Node, Type):
    """
    Represents a GitHub Sponsorship.

    https://developer.github.com/v4/object/sponsorship/

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def created_at(self):
        """
        The date and time the sponsor listing was created.

        :type: :class:`~datetime.datetime`
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def privacy(self):
        """
        The privacy level for the sponsorship.

        :type: :class:`~github.enums.SponsorshipPrivacy`
        """

        privacy = self.data["privacyLevel"]
        return SponsorshipPrivacy.try_value(privacy)
