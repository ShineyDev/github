"""
/github/objects/mannequin.py

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

import datetime
import typing

from github import utils
from github.abc import Actor
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class Mannequin(Actor, Node, Type, UniformResourceLocatable):
    """
    Represents a GitHub placeholder account.

    https://developer.github.com/v4/object/mannequin/

    Implements:

    * :class:`~github.abc.Actor`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} login='{0.login}'>".format(self)

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(bot, http) for bot in data]
    
    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time the mannequin was created.
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def database_id(self) -> int:
        """
        The mannequin's primary key from the database.
        """

        return self.data["databaseId"]
    
    @property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time the mannequin was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)
    
    async def fetch_email(self) -> typing.Optional[str]:
        """
        |coro|

        Fetches the mannequin's email.

        Requires the ``user:email`` scope.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The mannequin does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        Optional[:class:`str`]
            The url pointing to the mannequin's email.
        """

        email = await self.http.fetch_profileowner_email(self.id)
        return email
