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

from github import utils
from github.enums import CommentAuthorAssociation


class Comment():
    """
    Represents a comment on a GitHub subject.

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    # https://docs.github.com/en/graphql/reference/interfaces#comment

    __slots__ = ()

    @property
    def author(self):
        """
        The actor who authored the comment.

        :type: Union[:class:`~github.Bot`, \
                     :class:`~github.Mannequin`, \
                     :class:`~github.Organization`, \
                     :class:`~github.User`]
        """

        from github import objects

        data = self.data["author"]

        cls = objects._TYPE_MAP[data["__typename"]]
        return cls.from_data(data, self.http)

    @property
    def author_association(self):
        """
        The :attr:`.author`'s association with the subject of the comment.

        :type: :class:`~github.enums.CommentAuthorAssociation`
        """

        association = self.data["authorAssociation"]
        return CommentAuthorAssociation.try_value(association)

    @property
    def body(self):
        """
        The body of the comment.

        :type: :class:`str`
        """

        return self.data["body"]

    @property
    def body_html(self):
        """
        The :attr:`.body` of the comment as HTML.

        :type: :class:`str`
        """

        return self.data["bodyHTML"]

    @property
    def body_text(self):
        """
        The :attr:`.body` of the comment with markdown removed.

        :type: :class:`str`
        """

        return self.data["bodyText"]

    @property
    def created_at(self):
        """
        When the comment was created.

        :type: :class:`~datetime.datetime`
        """

        created_at = self.data["createdAt"]
        return utils.iso_to_datetime(created_at)

    @property
    def created_via_email(self):
        """
        Whether the comment was created via email.

        :type: :class:`bool`
        """

        return self.data["createdViaEmail"]

    @property
    def editor(self):
        """
        The actor who last edited the comment.

        :type: Union[:class:`~github.Bot`, \
                     :class:`~github.Mannequin`, \
                     :class:`~github.Organization`, \
                     :class:`~github.User`]
        """

        from github import objects

        data = self.data["editor"]

        if data:
            cls = objects._TYPE_MAP[data["__typename"]]
            return cls.from_data(data, self.http)

    @property
    def edited_at(self):
        """
        When the comment was last edited.

        :type: :class:`~datetime.datetime`
        """

        edited_at = self.data["lastEditedAt"]
        return utils.iso_to_datetime(edited_at)

    @property
    def published_at(self):
        """
        When the comment was published.

        :type: :class:`~datetime.datetime`
        """

        published_at = self.data["publishedAt"]
        return utils.iso_to_datetime(published_at)

    @property
    def updated_at(self):
        """
        When the comment was last updated.

        :type: :class:`~datetime.datetime`
        """

        updated_at = self.data["updatedAt"]
        return utils.iso_to_datetime(updated_at)

    @property
    def viewer_is_author(self):
        """
        Whether the viewer authored this comment.

        :type: :class:`bool`
        """

        return self.data["viewerDidAuthor"]
