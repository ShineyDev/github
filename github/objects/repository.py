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

from github import utils
from github.abc import Lockable
from github.abc import Node
from github.abc import ProjectOwner
from github.abc import Subscribable
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.enums import RepositoryLockReason
from github.enums import RepositoryPermissions
from .codeofconduct import CodeOfConduct
from .issue import Issue
from .language import Language
from .license import License
from .organization import Organization
from .user import User


class Repository(Lockable, Node, ProjectOwner, Subscribable, Type, UniformResourceLocatable):
    """
    Represents a GitHub repository.

    Implements:

    * :class:`~github.abc.Lockable`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.ProjectOwner`
    * :class:`~github.abc.Subscribable`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://developer.github.com/v4/object/repository/

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self):
        return "<{0.__class__.__name__} owner='{0.owner.login}' name='{0.name}'>".format(self)

    @property
    def allows_merge_commit(self):
        """
        Whether pull requests can be merged with a merge commit on the repository.

        :type: :class:`bool`
        """

        return self.data["mergeCommitAllowed"]

    @property
    def allows_rebase_merge(self):
        """
        Whether rebase-merging is enabled on the repository.

        :type: :class:`bool`
        """

        return self.data["rebaseMergeAllowed"]

    @property
    def allows_squash_merge(self):
        """
        Whether squash-merging is enabled on the repository.

        :type: :class:`bool`
        """

        return self.data["squashMergeAllowed"]

    @property
    def code_of_conduct(self):
        """
        The repository's code of conduct.

        :type: :class:`~github.CodeOfConduct`
        """

        codeofconduct = self.data["codeOfConduct"]
        return CodeOfConduct.from_data(codeofconduct_)

    @property
    def created_at(self):
        """
        When the repository was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self):
        """
        The primary key for the repository from the database.

        :type: :class:`int`
        """

        return self.data["databaseId"]

    @property
    def default_branch(self):
        """
        The name of the default branch.

        :type: :class:`str`
        """

        return self.data["defaultBranchRef"]["name"]

    @property
    def description(self):
        """
        The description of the repository.

        :type: :class:`str`
        """

        return self.data["description"] or ""

    @property
    def disk_usage(self):
        """
        The number of kilobytes the repository occupies on disk.

        :type: :class:`int`
        """

        return self.data["diskUsage"]

    @property
    def fork_count(self):
        """
        The number of forks created from the repository.

        :type: :class:`int`
        """

        return self.data["forkCount"]

    @property
    def has_issues(self):
        """
        Whether the repository has issues enabled.

        :type: :class:`bool`
        """

        return self.data["hasIssuesEnabled"]

    @property
    def has_wiki(self):
        """
        Whether the repository has wiki enabled.

        :type: :class:`bool`
        """

        return self.data["hasWikiEnabled"]

    @property
    def is_archived(self):
        """
        Whether the repository is archived.

        :type: :class:`bool`
        """

        return self.data["isArchived"]

    @property
    def is_disabled(self):
        """
        Whether the repository is disabled.

        :type: :class:`bool`
        """

        return self.data["isDisabled"]

    @property
    def is_fork(self):
        """
        Whether the repository is a fork of another repository.

        :type: :class:`bool`
        """

        return self.data["isFork"]

    @property
    def is_locked(self):
        """
        Whether the repository is locked.

        :type: :class:`bool`
        """

        return self.data["isLocked"]

    @property
    def is_mirror(self):
        """
        Whether the repository is a mirror of another repository.

        :type: :class:`bool`
        """

        return self.data["isMirror"]

    @property
    def is_private(self):
        """
        Whether the repository is private.

        :type: :class:`bool`
        """

        return self.data["isPrivate"]

    @property
    def is_template(self):
        """
        Whether the repository is a template repository.

        :type: :class:`bool`
        """

        return self.data["isTemplate"]

    @property
    def license(self):
        """
        The repository's license.

        :type: :class:`~github.License`
        """

        license = self.data["licenseInfo"]
        if license:
            return License.from_data(license)

    @property
    def name(self):
        """
        The name of the repository.

        :type: :class:`str`
        """

        return self.data["name"]

    @property
    def owner(self):
        """
        The owner of the repository.

        :type: Union[:class:`~github.Organization`, \
                     :class:`~github.User`]
        """

        owner = self.data["owner"]

        if owner["__typename"] == "Organization":
            return Organization.from_data(owner, self.http)
        elif owner["__typename"] == "User":
            return User.from_data(owner, self.http)

    @property
    def primary_language(self):
        """
        The primary language of the repository.

        :type: :class:`~github.Language`
        """

        primary_language = self.data["primaryLanguage"]
        if primary_language:
            return Language.from_data(primary_language)

    @property
    def pushed_at(self):
        """
        When the repository was last pushed to.

        :type: :class:`~datetime.datetime`
        """

        pushed_at = self.data["pushedAt"]
        return utils.iso_to_datetime(pushed_at)

    @property
    def updated_at(self):
        """
        The date and time when the repository was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    @property
    def viewer_can_administer(self):
        """
        Whether the authenticated user can administer the repository.

        :type: :class:`bool`
        """

        return self.data["viewerCanAdminister"]

    @property
    def viewer_can_update_topics(self):
        """
        Whether the authenticated user can update topics in the repository.

        :type: :class:`bool`
        """

        return self.data["viewerCanUpdateTopics"]

    @property
    def viewer_permissions(self):
        """
        The authenticated user's permissions in the repository.

        :type: :class:`~github.enums.RepositoryPermissions`
        """

        permissions = self.data["viewerPermission"]
        return RepositoryPermissions.try_value(permissions)

    async def fetch_assignable_users(self):
        """
        |coro|

        Fetches a list of users that can be assigned to issues in the repository.

        Returns
        -------
        List[:class:`~github.User`]
            A list of users.
        """

        data = await self.http.fetch_repository_assignable_users(self.id)
        return User.from_data(data, self.http)

    async def fetch_collaborators(self):
        """
        |coro|

        Fetches a list of collaborators associated with the repository.

        Returns
        -------
        List[:class:`~github.User`]
            A list of users.
        """

        data = await self.http.fetch_repository_collaborators(self.id)
        return User.from_data(data, self.http)

    async def fetch_issue(self, number):
        """
        |coro|

        Fetches an issue from the repository.

        Parameters
        ----------
        number: :class:`int`
            The issue number.

        Raises
        ------
        ~github.errors.NotFound
            An issue with the given number does not exist.

        Returns
        -------
        :class:`~github.Issue`
            The issue.
        """

        data = await self.http.fetch_repository_issue(self.id, number)
        return Issue.from_data(data, self.http)

    async def fetch_issues(self):
        """
        |coro|

        Fetches a list of issues from the repository.

        Returns
        -------
        List[:class:`~github.Issue`]
            A list of issues.
        """

        data = await self.http.fetch_repository_issues(self.id)
        return Issue.from_data(data, self.http)

    async def fetch_parent(self):
        """
        |coro|

        Fetches the repository's parent, if it is a fork.

        Returns
        -------
        Optional[:class:`~github.Repository`]
            The repository's parent.
        """

        data = await self.http.fetch_repository_parent(self.id)
        return Repository.from_data(data, self.http)

    async def fetch_template(self):
        """
        |coro|

        Fetches the repository's template, if it has one.

        Returns
        -------
        Optional[:class:`~github.Repository`]
            The repository's template.
        """

        data = await self.http.fetch_repository_template(self.id)
        return Repository.from_data(data, self.http)
