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

    https://developer.github.com/v4/object/label/

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.RepositoryNode`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(label, http) for label in data]

    @property
    def color(self) -> str:
        """
        The color of the label in the GitHub UI.
        """

        return self.data["color"]

    @property
    def colour(self) -> str:
        """
        An alias for :attr:`~github.Label.color`.
        """

        return self.data["color"]

    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time at which the label was created.
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def description(self) -> str:
        """
        The description of the label.
        """

        return self.data["description"] or ""

    @property
    def is_default(self) -> bool:
        """
        Whether or not the label is a default label.
        """

        return self.data["isDefault"]

    @property
    def name(self) -> str:
        """
        The name of the label.
        """

        return self.data["name"]

    @property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time at which the label was updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    async def fetch_issues(self) -> typing.List[Issue]:
        """
        Fetches a list of issues with the label.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The label does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.Issue`]
            A list of issues with the label.
        """

        data = await self.http.fetch_label_issues(self.id)
        return Issue.from_data(data, self.http)

    async def fetch_pull_requests(self) -> typing.List[PullRequest]:
        """
        Fetches a list of pull requests with the label.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The label does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.PullRequest`]
            A list of pull requests with the label.
        """

        data = await self.http.fetch_label_pull_requests(self.id)
        return PullRequest.from_data(data, self.http)
