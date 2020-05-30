"""
/github/objects/project.py

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
from github.abc import Closable
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.abc import Updatable
from github.enums import ProjectState
from .projectcolumn import ProjectColumn


class Project(Closable, Node, Type, UniformResourceLocatable, Updatable):
    """
    Represents a GitHub project.

    Implements:
    
    * :class:`~github.abc.Closable`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    * :class:`~github.abc.Updatable`
    """

    # https://developer.github.com/v4/object/project/

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def body(self) -> str:
        """
        The project's description.

        :type: :class:`str`
        """

        return self.data["body"]

    @property
    def body_html(self) -> str:
        """
        The project's description as HTML.

        :type: :class:`str`
        """

        return self.data["bodyHTML"]

    @utils._cached_property
    def created_at(self) -> datetime.datetime:
        """
        When the project was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self) -> int:
        """
        The project's primary key from the database.

        :type: :class:`int`
        """

        return self.data["databaseId"]

    @property
    def name(self) -> str:
        """
        The name of the project.

        :type: :class:`str`
        """

        return self.data["name"]

    @property
    def number(self) -> int:
        """
        The project's number.

        :type: :class:`int`
        """

        return self.data["number"]

    @utils._cached_property
    def state(self) -> typing.List[ProjectState]:
        """
        The project's state.

        :type: :class:`~github.enums.ProjectState`
        """

        state = self.data["state"]
        return ProjectState.try_value(state)

    @utils._cached_property
    def updated_at(self) -> datetime.datetime:
        """
        When the project was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    async def fetch_columns(self) -> typing.List[ProjectColumn]:
        """
        |coro|

        Fetches a list of columns in the project.

        Returns
        -------
        List[:class:`~github.ProjectColumn`]
            A list of columns.
        """

        data = await self.http.fetch_project_columns(self.id)
        return ProjectColumn.from_data(data, self.http)

    async def create_column(self, *, name: str) -> ProjectColumn:
        """
        |coro|

        Creates a new column in the project.

        Parameters
        ----------
        name: :class:`str`
            The name of the new column.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to create columns in the
            project.

        Returns
        -------
        :class:`~github.ProjectColumn`
            The created column.
        """

        # https://developer.github.com/v4/mutation/addprojectcolumn/

        data = await self.http.mutate_project_create_column(self.id, name)
        return ProjectColumn.from_data(data, self.http)
