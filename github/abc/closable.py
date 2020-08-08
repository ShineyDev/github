"""
/github/abc/closable.py

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


class Closable():
    """
    Represents an object which can be closed.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    # https://docs.github.com/en/graphql/reference/interfaces#closable

    __slots__ = ()

    @property
    def closed_at(self):
        """
        When the closable was last closed.

        :type: :class:`~datetime.datetime`
        """

        closed_at = self.data["closedAt"]
        return utils.iso_to_datetime(closed_at)

    @property
    def is_closed(self):
        """
        Whether the closable is closed.

        :type: :class:`bool`
        """

        return self.data["closed"]

    async def close(self):
        """
        |coro|

        Closes the closable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to close the closable.
        """

        # https://docs.github.com/en/graphql/reference/mutations#closeissue
        # https://docs.github.com/en/graphql/reference/mutations#closepullrequest

        map = {
            "Issue": self.http.mutate_issue_close,
            "PullRequest": self.http.mutate_pullrequest_close,
        }

        await map[self.data["__typename"]](self.id)

    async def reopen(self):
        """
        |coro|

        Reopens the closable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to reopen the closable.
        """

        # https://docs.github.com/en/graphql/reference/mutations#reopenissue
        # https://docs.github.com/en/graphql/reference/mutations#reopenpullrequest

        map = {
            "Issue": self.http.mutate_issue_reopen,
            "PullRequest": self.http.mutate_pullrequest_reopen,
        }

        await map[self.data["__typename"]](self.id)
