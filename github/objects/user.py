"""
/github/objects/user.py

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

import datetime

from github import utils
from github.objects import abc


"""
... not implemented ...
repositoriesContributedTo
starredRepositories
bioHTML
companyHTML
contributionsCollection
itemShowcase
pinnedItemsRemaining
projectsResourcePath
projectsUrl
viewerCanChangePinnedItems
viewerCanCreateProjects
viewerCanFollow
viewerIsFollowing
"""
class User(abc.Actor, abc.Node, abc.RepositoryOwner):
    """
    Represents a GitHub user account.

    https://developer.github.com/v4/object/user/
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self):
        return "<{0} login='{1}'>".format(self.__class__.__name__, self.login)

    @classmethod
    def from_data(cls, data, http):
        return cls(data["user"], http)

    @property
    def bio(self) -> str:
        """
        The user's public profile bio.
        """

        return self.data.get("bio")

    @property
    def company(self) -> str:
        """
        The user's public profile company.
        """

        return self.data.get("company")
    
    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time this user was created.
        """

        return utils.iso_to_datetime(self.data.get("createdAt"))

    @property
    def database_id(self) -> int:
        """
        The user's primary key from the database.
        """

        return self.data.get("databaseId")

    @property
    def email(self) -> str:
        """
        The user's publicly visible profile email.
        """

        return self.data.get("email")

    @property
    def is_bounty_hunter(self) -> bool:
        """
        Whether this user is a participant in the GitHub Security Bug Bounty.
        """

        return self.data.get("isBountyHunter")

    @property
    def is_campus_expert(self) -> bool:
        """
        Whether this user is a participant in the GitHub Campus Experts Program.
        """

        return self.data.get("isCampusExpert")

    @property
    def is_developer_program_member(self) -> bool:
        """
        Whether this user is a GitHub Developer Program member.
        """

        return self.data.get("isDeveloperProgramMember")

    @property
    def is_employee(self) -> bool:
        """
        Whether this user is a GitHub employee.
        """

        return self.data.get("isEmployee")

    @property
    def is_hireable(self) -> bool:
        """
        Whether this user has marked themselves as for hire.
        """

        return self.data.get("isHireable")

    @property
    def is_site_administrator(self) -> bool:
        """
        Whether this user is a site administrator.
        """

        return self.data.get("isSiteAdmin")

    @property
    def is_viewer(self) -> bool:
        """
        Whether or not this user is the viewing user.
        """

        return self.data.get("isViewer")

    @property
    def location(self) -> str:
        """
        The user's public profile location.
        """

        return self.data.get("location")

    @property
    def name(self) -> str:
        """
        The user's public profile name.
        """

        return self.data.get("name")
    
    @property
    def updated_at(self) -> datetime.datetime:
        """
        The date and time this user was last updated.
        """

        return utils.iso_to_datetime(self.data.get("updatedAt"))

    @property
    def website(self) -> str:
        """
        A url pointing to this user's public website/blog.
        """

        return self.data.get("websiteUrl")

    async def fetch_email(self, *, cache: bool=True) -> str:
        """

        """

        data = await self.http.fetch_user_email(self.login)
        email = data["user"]["email"]

        if cache:
            self.data["email"] = email

        return email

class AuthenticatedUser(User):
    """
    Represents the authenticated GitHub user account, "viewer".
    """

    @classmethod
    def from_data(cls, data, http):
        return cls(data["viewer"], http)
