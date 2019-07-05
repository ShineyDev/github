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
https://developer.github.com/v4/object/user/

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
    """

    def __init__(self, http, data):
        self.http = http
        self.data = data

    @classmethod
    def from_data(cls, http, data):
        return cls(http, data["user"])

    @property
    def bio(self) -> str:
        """

        """

        return self.data.get("bio")

    @property
    def company(self) -> str:
        """

        """

        return self.data.get("company")
    
    @property
    def created_at(self) -> datetime.datetime:
        """

        """

        return utils.iso_to_datetime(self.data.get("createdAt"))

    @property
    def database_id(self) -> int:
        """

        """

        return self.data.get("databaseId")

    @property
    def email(self) -> str:
        """

        """

        return self.data.get("email")

    @property
    def has_pinnable_items(self) -> bool:
        """

        """

        return self.data.get("anyPinnableItems")

    @property
    def is_bounty_hunter(self) -> bool:
        """

        """

        return self.data.get("isBountyHunter")

    @property
    def is_campus_expert(self) -> bool:
        """

        """

        return self.data.get("isCampusExpert")

    @property
    def is_developer_program_member(self) -> bool:
        """

        """

        return self.data.get("isDeveloperProgramMember")

    @property
    def is_employee(self) -> bool:
        """

        """

        return self.data.get("isEmployee")

    @property
    def is_hireable(self) -> bool:
        """

        """

        return self.data.get("isHireable")

    @property
    def is_site_administrator(self) -> bool:
        """

        """

        return self.data.get("isSiteAdmin")

    @property
    def is_viewer(self) -> bool:
        """

        """

        return self.data.get("isViewer")

    @property
    def location(self) -> str:
        """

        """

        return self.data.get("location")

    @property
    def name(self) -> str:
        """

        """

        return self.data.get("name")
    
    @property
    def updated_at(self) -> datetime.datetime:
        """

        """

        return utils.iso_to_datetime(self.data.get("updatedAt"))

    @property
    def website(self) -> str:
        """

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

    """

    @classmethod
    def from_data(cls, http, data):
        return cls(http, data["viewer"])
