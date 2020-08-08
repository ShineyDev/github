"""
/github/objects/projectcard.py

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
from github.enums import ProjectCardState


class ProjectCard(Node, Type, UniformResourceLocatable):
    """
    Represents a card in a GitHub project.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://docs.github.com/en/graphql/reference/objects#projectcard

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def body(self):
        """
        The body of the card.

        :type: Optional[:class:`str`]
        """

        return self.data["note"]

    @property
    def created_at(self):
        """
        When the card was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self):
        """
        The card's database ID.

        :type: :class:`int`
        """

        return self.data["databaseId"]

    @property
    def is_archived(self):
        """
        Whether the card is archived.

        :type: :class:`bool`
        """

        return self.data["isArchived"]

    @property
    def state(self):
        """
        The card's state.

        :type: :class:`~github.enums.ProjectCardState`
        """

        state = self.data["state"]
        return ProjectCardState.try_value(state)

    @property
    def updated_at(self):
        """
        When the card was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    async def move_to(self, column, *, after=None):
        """
        |coro|

        Moves the card to a column.

        Parameters
        ----------
        column: :class:`~github.ProjectColumn`
            The column to move the card to.
        after: :class:`~github.ProjectCard`
            The card to place the card after. Pass ``None`` to place it
            at the top. Defaults to ``None``.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to move the card.
        """

        # https://docs.github.com/en/graphql/reference/mutations#moveprojectcard

        if after is not None:
            after = after.id

        await self.http.mutate_projectcard_move_to(self.id, column.id, after)
