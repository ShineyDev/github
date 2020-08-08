"""
/github/objects/bot.py

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
from github.abc import Actor
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class Bot(Actor, Node, Type, UniformResourceLocatable):
    """
    Represents a GitHub bot account.

    Implements:

    * :class:`~github.abc.Actor`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://developer.github.com/v4/object/bot/

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self):
        return "<{0.__class__.__name__} login='{0.login}'>".format(self)

    @property
    def created_at(self):
        """
        When the bot was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self):
        """
        The bot's primary key from the database.

        :type: :class:`int`
        """

        return self.data["databaseId"]

    @property
    def updated_at(self):
        """
        When the bot was last updated.

        :type: Optional[:class:`~datetime.datetime`]
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)
