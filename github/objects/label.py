"""
/github/objects/label.py

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
from github.abc import RepositoryNode
from github.abc import Type
from github.abc import UniformResourceLocatable
from .issue import Issue
from .pullrequest import PullRequest


class Label(Node, RepositoryNode, Type, UniformResourceLocatable):
    """
    Represents a label on a :class:`~github.abc.Labelable`.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.RepositoryNode`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://developer.github.com/v4/object/label/

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def color(self) -> str:
        """
        The color of the label in the GitHub UI.

        :type: :class:`str`
        """

        return self.data["color"]

    colour = color

    @utils._cached_property
    def created_at(self) -> datetime.datetime:
        """
        When the label was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def description(self) -> str:
        """
        The description of the label.

        :type: :class:`str`
        """

        return self.data["description"] or ""

    @property
    def is_default(self) -> bool:
        """
        Whether the label is a default label.

        :type: :class:`bool`
        """

        return self.data["isDefault"]

    @property
    def name(self) -> str:
        """
        The name of the label.

        :type: :class:`str`
        """

        return self.data["name"]

    @utils._cached_property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        When the label was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    async def fetch_issues(self) -> typing.List[Issue]:
        """
        Fetches a list of issues with the label.

        Returns
        -------
        List[:class:`~github.Issue`]
            A list of issues.
        """

        data = await self.http.fetch_label_issues(self.id)
        return Issue.from_data(data, self.http)

    async def fetch_pull_requests(self) -> typing.List[PullRequest]:
        """
        Fetches a list of pull requests with the label.

        Returns
        -------
        List[:class:`~github.PullRequest`]
            A list of pull requests.
        """

        data = await self.http.fetch_label_pull_requests(self.id)
        return PullRequest.from_data(data, self.http)
