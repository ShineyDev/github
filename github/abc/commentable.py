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

import typing


class Commentable():
    """
    Represents an object which can be commented on.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    # this interface does not have an api equivalent

    __slots__ = ()

    async def fetch_comments(self) -> typing.List[typing.Union["CommitComment", "GistComment",
                                                               "IssueComment", "PullRequestComment",
                                                               "PullRequestReviewComment"]]:
        """
        |coro|

        Fetches a list of comments on the commentable.

        Returns
        -------
        List[Union[:class:`~github.CommitComment`, \
                   :class:`~github.GistComment`, \
                   :class:`~github.IssueComment`, \
                   :class:`~github.PullRequestComment`, \
                   :class:`~github.PullRequestReview`, \
                   :class:`~github.PullRequestReviewComment`, \
                   :class:`~github.TeamDiscussionComment`]]
            A list of comments.
        """

        # prevent cyclic imports
        from github import objects

        data_ = await self.http.fetch_commentable_comments(self.id)

        comments = list()

        for (data) in data_:
            if data["__typename"] == "IssueComment":
                # special case IssueComment for lack of API PullRequestComment

                if self.data["__typename"] == "Issue":
                    cls = objects.IssueComment
                elif self.data["__typename"] == "PullRequest":
                    cls = objects.PullRequestComment
            else:
                cls = objects._TYPE_MAP[data["__typename"]]

            comments.append(cls.from_data(data, self.http))

        return comments

    async def add_comment(self, body: str) -> typing.Union["CommitComment", "GistComment",
                                                           "IssueComment", "PullRequestComment",
                                                           "PullRequestReviewComment"]:
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
        Union[:class:`~github.CommitComment`, \
              :class:`~github.GistComment`, \
              :class:`~github.IssueComment`, \
              :class:`~github.PullRequestComment`, \
              :class:`~github.PullRequestReview`, \
              :class:`~github.PullRequestReviewComment`, \
              :class:`~github.TeamDiscussionComment`]
            The comment.
        """

        # prevent cyclic imports
        from github import objects

        data = await self.http.mutate_commentable_add_comment(self.id, body)

        if data["__typename"] == "IssueComment":
            # special case IssueComment for lack of API PullRequestComment

            if self.data["__typename"] == "Issue":
                cls = objects.IssueComment
            elif self.data["__typename"] == "PullRequest":
                cls = objects.PullRequestComment
        else:
            cls = objects._TYPE_MAP[data["__typename"]]

        return cls.from_data(data, self.http)
