"""
/github/objects/repository.py

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
import typing

from github import utils
from github.abc import Node
from github.enums import RepositoryLockReason
from github.enums import RepositoryPermissions
from github.enums import RepositorySubscription
from .codeofconduct import CodeOfConduct
from .language import Language
from .license import License
from .user import User


class Repository(Node):
    """
    Represents a GitHub repository.

    https://developer.github.com/v4/object/repository/
    """

    __slots__ = ("data", "http")

    def __init__(self, data: dict, http):
        self.data = data
        self.http = http

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} owner='{0.owner.login}' name='{0.name}'>".format(self)

    @classmethod
    def from_data(cls, data: dict, http) -> "Repository":
        return cls(data, http)

    @property
    def allows_merge_commit(self) -> bool:
        """
        Whether or not pull requests can be merged with a merge commit on the repository.
        """

        return self.data["mergeCommitAllowed"]

    @property
    def allows_rebase_merge(self) -> bool:
        """
        Whether or not rebase-merging is enabled on the repository.
        """

        return self.data["rebaseMergeAllowed"]

    @property
    def allows_squash_merge(self) -> bool:
        """
        Whether or not squash-merging is enabled on the repository.
        """

        return self.data["squashMergeAllowed"]

    @property
    def code_of_conduct(self) -> typing.Optional[CodeOfConduct]:
        """
        The repository's code of conduct.
        """

        codeofconduct = self.data["codeOfConduct"]
        if codeofconduct:
            return CodeOfConduct.from_data(codeofconduct_)

    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time when the repository was created.
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self) -> int:
        """
        The primary key for the repository from the database.
        """

        return self.data["databaseId"]

    @property
    def default_branch(self) -> str:
        """
        The name of the default branch.
        """

        return self.data["defaultBranchRef"]["name"]

    @property
    def description(self) -> str:
        """
        The description of the repository.
        """

        return self.data["description"] or ""

    @property
    def disk_usage(self) -> int:
        """
        The number of kilobytes the repository occupies on disk.
        """

        return self.data["diskUsage"]

    @property
    def fork_count(self) -> int:
        """
        The number of forks created from the repository.
        """

        return self.data["forkCount"]

    @property
    def has_issues(self) -> bool:
        """
        Whether or not the repository has issues enabled.
        """

        return self.data["hasIssuesEnabled"]

    @property
    def has_wiki(self) -> bool:
        """
        Whether or not the repository has wiki enabled.
        """

        return self.data["hasWikiEnabled"]

    @property
    def is_archived(self) -> bool:
        """
        Whether or not the repository is archived.
        """

        return self.data["isArchived"]

    @property
    def is_disabled(self) -> bool:
        """
        Whether or not the repository is disabled.
        """

        return self.data["isDisabled"]

    @property
    def is_fork(self) -> bool:
        """
        Whether or not the repository is a fork of another repository.
        """

        return self.data["isFork"]

    @property
    def is_locked(self) -> bool:
        """
        Whether or not the repository is locked.
        """

        return self.data["isLocked"]

    @property
    def is_mirror(self) -> bool:
        """
        Whether or not the repository is a mirror of another repository.
        """

        return self.data["isMirror"]

    @property
    def is_private(self) -> bool:
        """
        Whether or not the repository is private.
        """

        return self.data["isPrivate"]

    @property
    def is_template(self) -> bool:
        """
        Whether or not the repository is a template repository.
        """

        return self.data["isTemplate"]

    @property
    def license(self) -> typing.Optional[License]:
        """
        The repository's license.
        """

        license = self.data["licenseInfo"]
        if license:
            return License.from_data(license)

    @property
    def lock_reason(self) -> typing.Optional[RepositoryLockReason]:
        """
        The reason for the repository to be in a locked state.
        """

        lock_reason = self.data["lockReason"]
        if lock_reason:
            return RepositoryLockReason.from_data(lock_reason)

    @property
    def name(self) -> str:
        """
        The name of the repository.
        """

        return self.data["name"]

    @property
    def owner(self) -> typing.Union[User]:
        """
        The owner of the repository.
        """

        owner = self.data["owner"]
        
        if owner["__typename"] == "Organization":
            # TODO: implement github.Organization
            ...
        elif owner["__typename"] == "User":
            return User.from_data(owner, self.http)

    @property
    def parent(self) -> typing.Optional["PartialRepository"]:
        """
        The repository's parent repository.
        """

        parent = self.data.get("parent", None)
        if not parent:
            return None

        return PartialRepository.from_data(parent, self.http)

    @property
    def primary_language(self) -> Language:
        """
        The primary language of the repository.
        """

        primary_language = self.data["primaryLanguage"]
        if primary_language:
            return Language.from_data(primary_language)

    @property
    def pushed_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time when the repository was last pushed to.
        """

        pushed_at = self.data["pushedAt"]
        if pushed_at:
            return utils.iso_to_datetime(pushed_at)

    @property
    def template(self) -> typing.Optional["PartialRepository"]:
        """
        The repository's template repository.
        """

        template = self.data.get("templateRepository", None)
        if not template:
            return None

        return PartialRepository.from_data(template, self.http)

    @property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time when the repository was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    @property
    def url(self) -> str:
        """
        The repository's url.
        """

        return self.data["url"]

    @property
    def viewer_can_administer(self) -> bool:
        """
        Whether or not the authenticated user can administer the repository.
        """

        return self.data["viewerCanAdminister"]

    @property
    def viewer_can_create_projects(self) -> bool:
        """
        Whether or not the authenticated user can create projects in the repository.
        """

        return self.data["viewerCanCreateProjects"]

    @property
    def viewer_can_subscribe(self) -> bool:
        """
        Whether or not the authenticated user can subscribe to the repository.
        """

        return self.data["viewerCanSubscribe"]

    @property
    def viewer_can_update_topics(self) -> bool:
        """
        Whether or not the authenticated user can update topics in the repository.
        """

        return self.data["viewerCanUpdateTopics"]

    @property
    def viewer_permissions(self) -> RepositoryPermissions:
        """
        The authenticated user's permissions in the repository.
        """

        permissions = self.data["viewerPermission"]
        return RepositoryPermissions.from_data(permissions)

    @property
    def viewer_subscription(self) -> RepositorySubscription:
        """
        The authenticated user's subscription to the repository.
        """

        subscription = self.data["viewerSubscription"]
        return RepositorySubscription.from_data(subscription)

    async def fetch_assignable_users(self):
        """
        Fetches a list of users that can be assigned to issues in the repository.
        """

        data = await self.http.fetch_repository_assignable_users(self.owner.login, self.name)
        return User.from_data(data, self.http)

    async def fetch_collaborators(self):
        """
        Fetches a list of collaborators associated with the repository.
        """

        data = await self.http.fetch_repository_collaborators(self.owner.login, self.name)
        return User.from_data(data, self.http)

class PartialRepository(Node):
    """
    Represents a GitHub repository.

    https://developer.github.com/v4/object/repository/

    This partial-class doesn't implement the :attr:`Repository.parent` and :attr:`Repository.template` attributes.
    """

    __slots__ = ("data", "http")

    def __init__(self, data: dict, http):
        self.data = data
        self.http = http

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} owner='{0.owner.login}' name='{0.name}'>".format(self)

    @classmethod
    def from_data(cls, data: dict, http) -> "PartialRepository":
        return cls(data, http)

    @property
    def allows_merge_commit(self) -> bool:
        """
        Whether or not pull requests can be merged with a merge commit on the repository.
        """

        return self.data["mergeCommitAllowed"]

    @property
    def allows_rebase_merge(self) -> bool:
        """
        Whether or not rebase-merging is enabled on the repository.
        """

        return self.data["rebaseMergeAllowed"]

    @property
    def allows_squash_merge(self) -> bool:
        """
        Whether or not squash-merging is enabled on the repository.
        """

        return self.data["squashMergeAllowed"]

    @property
    def code_of_conduct(self) -> typing.Optional[CodeOfConduct]:
        """
        The repository's code of conduct.
        """

        codeofconduct = self.data["codeOfConduct"]
        if codeofconduct:
            return CodeOfConduct.from_data(codeofconduct)

    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time when the repository was created.
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self) -> int:
        """
        The primary key for the repository from the database.
        """

        return self.data["databaseId"]

    @property
    def default_branch(self) -> str:
        """
        The name of the default branch.
        """

        return self.data["defaultBranchRef"]["name"]

    @property
    def description(self) -> str:
        """
        The description of the repository.
        """

        return self.data["description"] or ""

    @property
    def disk_usage(self) -> int:
        """
        The number of kilobytes the repository occupies on disk.
        """

        return self.data["diskUsage"]

    @property
    def fork_count(self) -> int:
        """
        The number of forks created from the repository.
        """

        return self.data["forkCount"]

    @property
    def has_issues(self) -> bool:
        """
        Whether or not the repository has issues enabled.
        """

        return self.data["hasIssuesEnabled"]

    @property
    def has_wiki(self) -> bool:
        """
        Whether or not the repository has wiki enabled.
        """

        return self.data["hasWikiEnabled"]

    @property
    def is_archived(self) -> bool:
        """
        Whether or not the repository is archived.
        """

        return self.data["isArchived"]

    @property
    def is_disabled(self) -> bool:
        """
        Whether or not the repository is disabled.
        """

        return self.data["isDisabled"]

    @property
    def is_fork(self) -> bool:
        """
        Whether or not the repository is a fork of another repository.
        """

        return self.data["isFork"]

    @property
    def is_locked(self) -> bool:
        """
        Whether or not the repository is locked.
        """

        return self.data["isLocked"]

    @property
    def is_mirror(self) -> bool:
        """
        Whether or not the repository is a mirror of another repository.
        """

        return self.data["isMirror"]

    @property
    def is_private(self) -> bool:
        """
        Whether or not the repository is private.
        """

        return self.data["isPrivate"]

    @property
    def is_template(self) -> bool:
        """
        Whether or not the repository is a template repository.
        """

        return self.data["isTemplate"]

    @property
    def license(self) -> typing.Optional[License]:
        """
        The repository's license.
        """

        license = self.data["licenseInfo"]
        if license:
            return License.from_data(license)

    @property
    def lock_reason(self) -> typing.Optional[RepositoryLockReason]:
        """
        The reason for the repository to be in a locked state.
        """

        lock_reason = self.data["lockReason"]
        if lock_reason:
            return RepositoryLockReason.from_data(lock_reason)

    @property
    def name(self) -> str:
        """
        The name of the repository.
        """

        return self.data["name"]

    @property
    def owner(self) -> typing.Union[User]:
        """
        The owner of the repository.
        """

        owner = self.data["owner"]
        
        if owner["__typename"] == "Organization":
            # TODO: implement github.Organization
            ...
        elif owner["__typename"] == "User":
            return User.from_data(owner, self.http)

    @property
    def primary_language(self) -> Language:
        """
        The primary language of the repository.
        """

        primary_language = self.data["primaryLanguage"]
        if primary_language:
            return Language.from_data(primary_language)

    @property
    def pushed_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time when the repository was last pushed to.
        """

        pushed_at = self.data["pushedAt"]
        if pushed_at:
            return utils.iso_to_datetime(pushed_at)

    @property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time when the repository was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    @property
    def url(self) -> str:
        """
        The repository's url.
        """

        return self.data["url"]

    @property
    def viewer_can_administer(self) -> bool:
        """
        Whether or not the authenticated user can administer the repository.
        """

        return self.data["viewerCanAdminister"]

    @property
    def viewer_can_create_projects(self) -> bool:
        """
        Whether or not the authenticated user can create projects in the repository.
        """

        return self.data["viewerCanCreateProjects"]

    @property
    def viewer_can_subscribe(self) -> bool:
        """
        Whether or not the authenticated user can subscribe to the repository.
        """

        return self.data["viewerCanSubscribe"]

    @property
    def viewer_can_update_topics(self) -> bool:
        """
        Whether or not the authenticated user can update topics in the repository.
        """

        return self.data["viewerCanUpdateTopics"]

    @property
    def viewer_permissions(self) -> RepositoryPermissions:
        """
        The authenticated user's permissions in the repository.
        """

        permissions = self.data["viewerPermission"]
        return RepositoryPermissions.from_data(permissions)

    @property
    def viewer_subscription(self) -> RepositorySubscription:
        """
        The authenticated user's subscription to the repository.
        """

        subscription = self.data["viewerSubscription"]
        return RepositorySubscription.from_data(subscription)

    async def fetch_assignable_users(self) -> typing.List[User]:
        """
        Fetches a list of users that can be assigned to issues in the repository.
        """

        data = await self.http.fetch_repository_assignable_users(self.owner.login, self.name)
        return User.from_data(data, self.http)

    async def fetch_collaborators(self) -> typing.List[User]:
        """
        Fetches a list of collaborators associated with the repository.
        """

        data = await self.http.fetch_repository_collaborators(self.owner.login, self.name)
        return User.from_data(data, self.http)
