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
from github.iterator import CollectionIterator
from github.enums import CommentAuthorAssociation


class Comment():
    """
    Represents a GitHub comment.
    """

    __slots__ = ()

    @property
    def author_association(self):
        """
        The author's association with a subject of the comment.

        :type: :class:`~github.enums.CommentAuthorAssociation`
        """

        author_association = self.data["authorAssociation"]
        return CommentAuthorAssociation.try_value(author_association)

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
        The :attr:`.body` of the comment with Markdown removed.

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
    def edited_at(self):
        """
        When the comment was last edited.

        :type: Optional[:class:`~datetime.datetime`]
        """

        edited_at = self.data["lastEditedAt"]
        return utils.iso_to_datetime(edited_at)

    @property
    def is_edited(self):
        """
        Whether the comment was edited.

        :type: :class:`bool`
        """

        return self.data["includesCreatedEdit"]

    @property
    def is_email_response(self):
        """
        Whether the comment was created from an e-mail response.

        :type: :class:`bool`
        """

        return self.data["createdViaEmail"]

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
        Whether the authenticated user authored the comment.

        :type: :class:`bool`
        """

        return self.data["viewerDidAuthor"]

    async def fetch_author(self):
        """
        |coro|

        Fetches the author of the comment.

        Returns
        -------
        Union[:class:`~github.Bot`, \
              :class:`~github.User`]
            The author of the comment.
        """

        from github.objects import _TYPE_MAP

        data = await self.http.fetch_comment_author(self.id)
        return _TYPE_MAP[data["__typename"]].from_data(data, self.http)

    async def fetch_editor(self):
        """
        |coro|

        Fetches the most recent editor of the comment.

        Returns
        -------
        Union[:class:`~github.Bot`, \
              :class:`~github.User`]
            The editor of the comment.
        """

        from github.objects import _TYPE_MAP

        data = await self.http.fetch_comment_editor(self.id)
        return _TYPE_MAP[data["__typename"]].from_data(data, self.http)

    def fetch_edits(self, **kwargs):
        """
        |aiter|

        Fetches edits made to this comment's :attr:`.body`.

        Parameters
        ----------
        **kwargs
            Keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.CommentContentEdit`.
        """

        from github.objects import CommentContentEdit

        def map_func(data):
            return CommentContentEdit.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_comment_edits,
            self.id,
            map_func=map_func,
            **kwargs
        )
