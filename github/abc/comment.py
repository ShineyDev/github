"""
/github/abc/comment.py

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
from github.enums import CommentAuthorAssociation


class Comment():
    """
    Represents a GitHub comment.

    https://developer.github.com/v4/interface/comment/

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def author(self) -> typing.Union["Organization", "User"]:
        """
        The actor who authored the comment.
        """
        
        # prevent cyclic imports
        from github.objects import Bot
        from github.objects import Mannequin
        from github.objects import Organization
        from github.objects import User

        author = self.data["author"]

        if author["__typename"] == "Bot":
            return Bot.from_data(author, self.http)
        elif author["__typename"] == "Mannequin":
            return Mannequin.from_data(author, self.http)
        elif author["__typename"] == "Organization":
            return Organization.from_data(author, self.http)
        elif author["__typename"] == "User":
            return User.from_data(author, self.http)

    @property
    def author_association(self) -> CommentAuthorAssociation:
        """
        The :attr:`.author`'s association with the subject of the comment.
        """

        association = self.data["authorAssociation"]
        return CommentAuthorAssociation.from_data(association)

    @property
    def body(self) -> str:
        """
        The body of the comment.
        """

        return self.data["body"]

    @property
    def body_html(self) -> str:
        """
        The :attr:`.body` of the comment as HTML.
        """

        return self.data["bodyHTML"]

    @property
    def body_text(self) -> str:
        """
        The :attr:`.body` of the comment with markdown removed.
        """

        return self.data["bodyText"]

    @property
    def created_at(self) -> datetime.datetime:
        """
        The date and time at which the comment was created.
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def created_via_email(self) -> bool:
        """
        Whether or not the comment was created via email.
        """

        return self.data["createdViaEmail"]

    @property
    def editor(self) -> typing.Optional[typing.Union["User"]]:
        """
        The actor who edited the comment.
        """

        # prevent cyclic imports
        from github.objects import Bot
        from github.objects import Mannequin
        from github.objects import Organization
        from github.objects import User

        editor = self.data["author"]

        if editor["__typename"] == "Bot":
            return Bot.from_data(editor, self.http)
        elif editor["__typename"] == "Mannequin":
            return Mannequin.from_data(editor, self.http)
        elif editor["__typename"] == "Organization":
            return Organization.from_data(editor, self.http)
        elif editor["__typename"] == "User":
            return User.from_data(editor, self.http)

    @property
    def edited_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time at which the comment was edited.
        """

        edited_at = self.data["lastEditedAt"]
        return utils.iso_to_datetime(edited_at)

    @property
    def published_at(self) -> datetime.datetime:
        """
        The date and time at which the comment was published.
        """

        published_at = self.data["publishedAt"]
        return utils.iso_to_datetime(published_at)

    @property
    def updated_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time at which the comment was updated.
        """

        updated_at = self.data["updatedAt"]
        if updated_at:
            return utils.iso_to_datetime(updated_at)

    @property
    def viewer_is_author(self) -> bool:
        """
        Whether or not the viewer authored this comment.
        """

        return self.data["viewerDidAuthor"]
