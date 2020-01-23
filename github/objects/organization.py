"""
/github/objects/organization.py

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

import typing

from github.abc import Actor
from github.abc import Node
from github.abc import ProfileOwner
from github.abc import ProjectOwner
from github.abc import RepositoryOwner
from github.abc import Type
from github.abc import UniformResourceLocatable


class Organization(Actor, Node, ProfileOwner, ProjectOwner, RepositoryOwner, Type,
                   UniformResourceLocatable):
    """
    Represents a GitHub organization.

    https://developer.github.com/v4/object/organization/

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
            return [cls(organization, http) for organization in data]

    @property
    def database_id(self) -> int:
        """
        The organization's primary key from the database.
        """

        return self.data["databaseId"]

    @property
    def description(self) -> str:
        """
        The organization's description.
        """

        return self.data["description"] or ""

    @property
    def is_verified(self) -> bool:
        """
        Whether or not the organization's public email is verified.
        """

        return self.data["isVerified"]

    @property
    def new_team_resource_path(self) -> str:
        """
        The organization's new team resource path.
        """

        return self.data["newTeamResourcePath"]

    @property
    def new_team_url(self) -> str:
        """
        The organization's new team url.
        """

        return self.data["newTeamUrl"]

    @property
    def teams_resource_path(self) -> str:
        """
        The organization's teams resource path.
        """

        return self.data["teamsResourcePath"]

    @property
    def teams_url(self) -> str:
        """
        The organization's teams url.
        """

        return self.data["teamsUrl"]

    @property
    def viewer_can_administer(self) -> bool:
        """
        Whether or not the authenticated user can administer the organization.
        """

        return self.data["viewerCanAdminister"]

    @property
    def viewer_can_create_repositories(self) -> bool:
        """
        Whether or not the authenticated user can create repositories in the organization.
        """

        return self.data["viewerCanCreateRepositories"]

    @property
    def viewer_can_create_teams(self) -> bool:
        """
        Whether or not the authenticated user can create teams in the organization.
        """

        return self.data["viewerCanCreateTeams"]

    @property
    def viewer_is_member(self) -> bool:
        """
        Whether or not the authenticated user is a member of the organization.
        """

        return self.data["viewerIsAMember"]
