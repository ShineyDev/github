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
from github.iterator import CollectionIterator
from github.abc import Actor
from github.abc import Node
from github.abc import ProfileOwner
from github.abc import ProjectOwner
from github.abc import RepositoryOwner
from github.abc import Sponsorable
from github.abc import Type
from github.abc import UniformResourceLocatable
from .commitcomment import CommitComment
from .status import Status


class User(Actor, Node, ProfileOwner, ProjectOwner, RepositoryOwner,
           Sponsorable, Type, UniformResourceLocatable):
    """
    Represents a GitHub user account.

    Implements:

    * :class:`~github.abc.Actor`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.ProfileOwner`
    * :class:`~github.abc.ProjectOwner`
    * :class:`~github.abc.RepositoryOwner`
    * :class:`~github.abc.Sponsorable`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://docs.github.com/en/graphql/reference/objects#user

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self):
        return "<{0.__class__.__name__} login='{0.login}'>".format(self)

    @property
    def bio(self):
        """
        The user's public profile bio.

        :type: :class:`str`
        """

        return self.data["bio"] or ""

    @property
    def company(self):
        """
        The user's public profile company.

        :type: Optional[:class:`str`]
        """

        return self.data["company"]

    @property
    def created_at(self):
        """
        The date and time the user was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def database_id(self):
        """
        The user's database ID.

        :type: :class:`int`
        """

        return self.data["databaseId"]

    @property
    def is_bounty_hunter(self):
        """
        Whether the user is a participant in the GitHub Security Bug Bounty.

        :type: :class:`bool`
        """

        return self.data["isBountyHunter"]

    @property
    def is_campus_expert(self):
        """
        Whether the user is a participant in the GitHub Campus Experts Program.

        :type: :class:`bool`
        """

        return self.data["isCampusExpert"]

    @property
    def is_developer_program_member(self):
        """
        Whether the user is a GitHub Developer Program member.

        :type: :class:`bool`
        """

        return self.data["isDeveloperProgramMember"]

    @property
    def is_employee(self):
        """
        Whether the user is a GitHub employee.

        :type: :class:`bool`
        """

        return self.data["isEmployee"]

    @property
    def is_hireable(self):
        """
        Whether the user has marked themselves as for hire.

        :type: :class:`bool`
        """

        return self.data["isHireable"]

    @property
    def is_site_administrator(self):
        """
        Whether the user is a site administrator.

        :type: :class:`bool`
        """

        return self.data["isSiteAdmin"]

    @property
    def is_viewer(self):
        """
        Whether the user is the authenticated user.

        :type: :class:`bool`
        """

        return self.data["isViewer"]

    @property
    def updated_at(self):
        """
        When the user was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    @property
    def viewer_can_follow(self):
        """
        Whether the viewer can follow the user.

        :type: :class:`bool`
        """

        return self.data["viewerCanFollow"]

    @property
    def viewer_is_following(self):
        """
        Whether the viewer is following the user.

        :type: :class:`bool`
        """

        return self.data["viewerIsFollowing"]

    def fetch_commit_comments(self, **kwargs):
        """
        |aiter|

        Fetches the user's commit comments.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.CommitComment`.
        """

        def map_func(data):
            return CommitComment.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_user_commit_comments,
                                  self.id, map_func=map_func, **kwargs)

    def fetch_followers(self, **kwargs):
        """
        |aiter|

        Fetches the user's followers.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.User`.
        """

        def map_func(data):
            return User.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_user_followers, self.id,
                                  map_func=map_func, **kwargs)

    def fetch_following(self, **kwargs):
        """
        |aiter|

        Fetches users followed by the user.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.User`.
        """

        def map_func(data):
            return User.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_user_following, self.id,
                                  map_func=map_func, **kwargs)

class AuthenticatedUser(User):
    """
    Represents the authenticated GitHub user account or "viewer".

    Implements:

    * :class:`~github.abc.Actor`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.ProfileOwner`
    * :class:`~github.abc.ProjectOwner`
    * :class:`~github.abc.RepositoryOwner`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    async def clear_status(self):
        """
        |coro|

        Clears the authenticated user's status.
        """

        await self.http.mutate_user_update_status(None, None, False, None, None)

    async def update_status(self, *, message, emoji, busy=False, expires=None, organization=None):
        """
        |coro|

        Updates the authenticated user's status.

        Parameters
        ----------
        message: Optional[:class:`str`]
            The message to display on the status.
        emoji: Optional[:class:`str`]
            The emoji to display on the status. This can either be a
            unicode emoji or its name with colons.
        busy: :class:`bool`
            Whether to mark the user as busy.
        expires: :class:`~datetime.datetime`
            When to expire the status in UTC.
        organization: :class:`~github.Organization`
            The organization whose members will be allowed to see the
            status.

        Returns
        -------
        :class:`~github.Status`
            The new status.
        """

        if expires:
            expires = utils.datetime_to_iso(expires)

        if organization:
            organization = organization.id

        data = await self.http.mutate_user_update_status(message, emoji, busy, expires, organization)
        return Status.from_data(data, self.http)
