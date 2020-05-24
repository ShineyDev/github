"""
/github/objects/repository.py

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
from github.abc import ProjectOwner
from github.abc import Subscribable
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.enums import RepositoryLockReason
from github.enums import RepositoryPermissions
from .codeofconduct import CodeOfConduct
from .language import Language
from .license import License
from .organization import Organization
from .user import User


class Repository(Node, ProjectOwner, Subscribable, Type, UniformResourceLocatable):
    """
    Represents a GitHub repository.

    https://developer.github.com/v4/object/repository/

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.ProjectOwner`
    * :class:`~github.abc.Subscribable`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} owner='{0.owner.login}' name='{0.name}'>".format(self)

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

    @utils._cached_property
    def code_of_conduct(self) -> typing.Optional[CodeOfConduct]:
        """
        The repository's code of conduct.
        """

        codeofconduct = self.data["codeOfConduct"]
        if codeofconduct:
            return CodeOfConduct.from_data(codeofconduct_)

    @utils._cached_property
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

    @utils._cached_property
    def license(self) -> typing.Optional[License]:
        """
        The repository's license.
        """

        license = self.data["licenseInfo"]
        if license:
            return License.from_data(license)

    @utils._cached_property
    def lock_reason(self) -> typing.Optional[RepositoryLockReason]:
        """
        The reason for the repository to be in a locked state.
        """

        reason = self.data["lockReason"]
        return RepositoryLockReason.try_value(reason)

    @property
    def name(self) -> str:
        """
        The name of the repository.
        """

        return self.data["name"]

    @utils._cached_property
    def owner(self) -> typing.Union[Organization, User]:
        """
        The owner of the repository.
        """

        owner = self.data["owner"]
        
        if owner["__typename"] == "Organization":
            return Organization.from_data(owner, self.http)
        elif owner["__typename"] == "User":
            return User.from_data(owner, self.http)

    @utils._cached_property
    def primary_language(self) -> Language:
        """
        The primary language of the repository.
        """

        primary_language = self.data["primaryLanguage"]
        if primary_language:
            return Language.from_data(primary_language)

    @utils._cached_property
    def pushed_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time when the repository was last pushed to.
        """

        pushed_at = self.data["pushedAt"]
        if pushed_at:
            return utils.iso_to_datetime(pushed_at)

    @utils._cached_property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time when the repository was last updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    @property
    def viewer_can_administer(self) -> bool:
        """
        Whether or not the authenticated user can administer the repository.
        """

        return self.data["viewerCanAdminister"]

    @property
    def viewer_can_update_topics(self) -> bool:
        """
        Whether or not the authenticated user can update topics in the repository.
        """

        return self.data["viewerCanUpdateTopics"]

    @utils._cached_property
    def viewer_permissions(self) -> RepositoryPermissions:
        """
        The authenticated user's permissions in the repository.
        """

        permissions = self.data["viewerPermission"]
        return RepositoryPermissions.try_value(permissions)

    async def fetch_assignable_users(self):
        """
        Fetches a list of users that can be assigned to issues in the repository.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.User`]
            A list of users that can be assigned to issues in the repository.
        """

        data = await self.http.fetch_repository_assignable_users(self.id)
        return User.from_data(data, self.http)

    async def fetch_collaborators(self):
        """
        Fetches a list of collaborators associated with the repository.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.User`]
            A list of collaborators associated with the repository.
        """

        data = await self.http.fetch_repository_collaborators(self.id)
        return User.from_data(data, self.http)

    async def fetch_parent(self):
        """
        |coro|

        Fetches the repository's parent, if it is a fork.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        Optional[:class:`~github.Repository`]
            The repository parent.
        """

        data = await self.http.fetch_repository_parent(self.id)
        return Repository.from_data(data, self.http)

    async def fetch_template(self):
        """
        |coro|

        Fetches the repository's template, if it has one.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The repository does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        Optional[:class:`~github.Repository`]
            The repository template.
        """

        data = await self.http.fetch_repository_template(self.id)
        return Repository.from_data(data, self.http)
