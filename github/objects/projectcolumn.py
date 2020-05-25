"""
/github/objects/projectcolumn.py

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
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.enums import ProjectColumnPurpose
from .projectcard import ProjectCard


class ProjectColumn(Node, Type, UniformResourceLocatable):
    """
    Represents a column in a GitHub project.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://developer.github.com/v4/object/projectcolumn/

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @utils._cached_property
    def created_at(self) -> datetime.datetime:
        """
        When the column was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self) -> int:
        """
        The column's primary key from the database.

        :type: :class:`int`
        """

        return self.data["databaseId"]

    @property
    def name(self) -> str:
        """
        The name of the column.

        :type: :class:`str`
        """

        return self.data["name"]

    @utils._cached_property
    def purpose(self) -> ProjectColumnPurpose:
        """
        The column's purpose.

        :type: :class:`~github.enums.ProjectColumnPurpose`
        """

        purpose = self.data["purpose"]
        return ProjectColumnPurpose.try_value(purpose)

    @utils._cached_property
    def updated_at(self) -> datetime.datetime:
        """
        When the column was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    async def fetch_cards(self) -> typing.List[ProjectCard]:
        """
        |coro|

        Fetches a list of cards in the column.

        Returns
        -------
        List[:class:`~github.ProjectCard`]
            A list of cards.
        """

        data = await self.http.fetch_projectcolumn_cards(self.id)
        return ProjectCard.from_data(data, self.http)
