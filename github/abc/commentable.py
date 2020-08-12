"""
/github/abc/commentable.py

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

from github.iterator import CollectionIterator


class Commentable():
    """
    Represents an object which can be commented on.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    def fetch_comments(self, **kwargs):
        """
        |aiter|

        Fetches comments on the commentable.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.abc.Comment`.
        """

        from github import objects

        def map_func(data):
            if data["__typename"] == "IssueComment" and self.data["__typename"] == "PullRequest":
                # special case for lack of API PullRequestComment
                cls = objects.PullRequestComment
            else:
                cls = objects._TYPE_MAP[data["__typename"]]

            return cls.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_commentable_comments,
                                  self.id, map_func=map_func, **kwargs)

    async def add_comment(self, body):
        """
        |coro|

        Adds a comment to the commentable.

        Parameters
        ----------
        body: :class:`str`
            The body of the comment.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to comment on the commentable.

        Returns
        -------
        Union[:class:`~github.CommitComment`]
            The comment.
        """

        from github import objects

        data = await self.http.mutate_commentable_add_comment(self.id, body)

        if data["__typename"] == "IssueComment" and self.data["__typename"] == "PullRequest":
            # special case for lack of API PullRequestComment
            cls = objects.PullRequestComment
        else:
            cls = objects._TYPE_MAP[data["__typename"]]

        return cls.from_data(data, self.http)
