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
    Represents an entity that can be commented on.
    """

    __slots__ = ()

    def fetch_comments(self, **kwargs):
        """
        |aiter|

        Fetches comments on the commentable.

        Parameters
        ----------
        **kwargs
            Keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of Union[:class:`~github.CommitComment`, \
                                 :class:`~github.GistComment`, \
                                 :class:`~github.IssueComment`, \
                                 :class:`~github.PullRequestComment`, \
                                 :class:`~github.PullRequestReviewComment`, \
                                 :class:`~github.TeamDiscussionComment`].
        """

        from github import objects

        def map_func(data):
            if data["__typename"] == "IssueComment" and self.data["__typename"] == "PullRequest":
                # special case for lack of API PullRequestComment
                cls = objects.PullRequestComment
            else:
                cls = objects._TYPE_MAP[data["__typename"]]

            return cls.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_commentable_comments,
            self.id,
            map_func=map_func,
            **kwargs
        )
