"""
/github/objects/user.py

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
from github.abc import ProfileOwner
from github.abc import ProjectOwner
from github.abc import RepositoryOwner
from github.abc import Type
from github.abc import UniformResourceLocatable
from .commitcomment import CommitComment


class User(Actor, Node, ProfileOwner, ProjectOwner, RepositoryOwner, Type,
           UniformResourceLocatable):
    """
    Represents a GitHub user account.

    https://developer.github.com/v4/object/user/

    Implements:

    * :class:`~github.abc.Actor`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.ProfileOwner`
    * :class:`~github.abc.ProjectOwner`
    * :class:`~github.abc.RepositoryOwner`
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
            return [cls(user, http) for user in data]

    @property
    def bio(self) -> str:
        """
        The user's public profile bio.
        """

        return self.data["bio"] or ""

    @property
    def company(self) -> typing.Optional[str]:
        """
        The user's public profile company.
        """

        return self.data["company"]
    
    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time the user was created.
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def database_id(self) -> int:
        """
        The user's primary key from the database.
        """

        return self.data["databaseId"]

    @property
    def is_bounty_hunter(self) -> bool:
        """
        Whether the user is a participant in the GitHub Security Bug Bounty.
        """

        return self.data["isBountyHunter"]

    @property
    def is_campus_expert(self) -> bool:
        """
        Whether the user is a participant in the GitHub Campus Experts Program.
        """

        return self.data["isCampusExpert"]

    @property
    def is_developer_program_member(self) -> bool:
        """
        Whether the user is a GitHub Developer Program member.
        """

        return self.data["isDeveloperProgramMember"]

    @property
    def is_employee(self) -> bool:
        """
        Whether the user is a GitHub employee.
        """

        return self.data["isEmployee"]

    @property
    def is_hireable(self) -> bool:
        """
        Whether the user has marked themselves as for hire.
        """

        return self.data["isHireable"]

    @property
    def is_site_administrator(self) -> bool:
        """
        Whether the user is a site administrator.
        """

        return self.data["isSiteAdmin"]

    @property
    def is_viewer(self) -> bool:
        """
        Whether or not the user is the viewing user.
        """

        return self.data["isViewer"]
    
    @property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time the user was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    async def fetch_commit_comments(self) -> typing.List[CommitComment]:
        """
        Fetches the user's commit comments.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The user does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.CommitComment`]
            A list of commit comments created by the user.
        """

        data = await self.http.fetch_user_commit_comments(self.id)
        return CommitComment.from_data(data, self.http)

class AuthenticatedUser(User):
    """
    Represents the authenticated GitHub user account, "viewer".

    https://developer.github.com/v4/object/user/

    Implements:

    * :class:`~github.abc.Actor`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.ProfileOwner`
    * :class:`~github.abc.ProjectOwner`
    * :class:`~github.abc.RepositoryOwner`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    @classmethod
    def from_data(cls, data, http):
        return cls(data, http)
