"""
/github/objects/organization.py

    Copyright (c) 2019 ShineyDev
    
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
from github.abc import RepositoryOwner


class Organization(Actor, Node, RepositoryOwner):
    """
    Represents a GitHub organization.

    https://developer.github.com/v4/object/organization/
    """

    __slots__ = ("data", "http")

    def __init__(self, data: dict, http):
        self.data = data
        self.http = http

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} login='{0.login}'>".format(self)

    @classmethod
    def from_data(cls, data: typing.Union[dict, list], http) -> typing.Union["Organization", typing.List["Organization"]]:
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            organizations = list()

            for (organization) in data:
                organizations.append(cls(organization, http))

            return organizations

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
    def email(self) -> typing.Optional[str]:
        """
        The organization's public email.
        """

        return self.data["email"]

    @property
    def is_verified(self) -> bool:
        """
        Whether or not the organization's public email is verified.
        """

        return self.data["isVerified"]

    @property
    def location(self) -> typing.Optional[str]:
        """
        The organization's location.
        """

        return self.data["location"]

    @property
    def name(self) -> str:
        """
        The organization's name.
        """

        return self.data["name"]

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
    def projects_resource_path(self) -> str:
        """
        The organization's projects resource path.
        """

        return self.data["projectsResourcePath"]

    @property
    def projects_url(self) -> str:
        """
        The organization's projects url.
        """

        return self.data["projectsUrl"]

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
    def viewer_can_change_pinned_items(self) -> bool:
        """
        Whether or not the authenticated user can change the items pinned to the organization's profile.
        """

        return self.data["viewerCanCreateProjects"]

    @property
    def viewer_can_create_projects(self) -> bool:
        """
        Whether or not the authenticated user can create projects in the organization.
        """

        return self.data["viewerCanCreateProjects"]

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

    @property
    def website(self) -> typing.Optional[str]:
        """
        The organization's website.
        """

        return self.data["websiteUrl"]
