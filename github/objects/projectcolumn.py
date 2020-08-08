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

    @property
    def created_at(self):
        """
        When the column was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self):
        """
        The column's primary key from the database.

        :type: :class:`int`
        """

        return self.data["databaseId"]

    @property
    def name(self):
        """
        The name of the column.

        :type: :class:`str`
        """

        return self.data["name"]

    @property
    def purpose(self):
        """
        The column's purpose.

        :type: :class:`~github.enums.ProjectColumnPurpose`
        """

        purpose = self.data["purpose"]
        return ProjectColumnPurpose.try_value(purpose)

    @property
    def updated_at(self):
        """
        When the column was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    async def fetch_cards(self):
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

    async def create_card(self, *, body=None, content=None):
        """
        |coro|

        Creates a new card in the column.

        .. note::

            Either ``body`` or ``content`` must be provided but not
            both.

        Parameters
        ----------
        body: :class:`str`
            The body of the new card.
        content: Union[:class:`~github.Issue`, \
                       :class:`~github.PullRequest`]
            The content of the new card.

        Raises
        ------
        TypeError
            Both or neither of ``body`` and ``content`` we provided.
        ~github.errors.Forbidden
            You do not have permission to create cards in the project.

        Returns
        -------
        :class:`~github.ProjectCard`
            The created card.
        """

        # https://developer.github.com/v4/mutation/addprojectcard/

        if body is None and content is None:
            raise TypeError("at least one of body and content must be provided")
        elif body is not None and content is not None:
            raise TypeError("only one of body and content should be provided")

        if content is not None:
            content = content.id

        data = await self.http.mutate_projectcolumn_create_card(self.id, body, content)
        return ProjectCard.from_data(data, self.http)

    async def move_to(self, *, after):
        """
        |coro|

        Moves the column after another column.

        Parameters
        ----------
        after: Optional[:class:`~github.ProjectColumn`]
            The column to place the column after. Pass ``None`` to
            place it at the front.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to move the column.
        """

        # https://developer.github.com/v4/mutation/moveprojectcolumn/

        if after is not None:
            after = after.id

        await self.http.mutate_projectcolumn_move_to(self.id, after)
