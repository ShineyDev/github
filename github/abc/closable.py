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

import datetime
import typing

from github import utils


class Closable():
    """
    Represents an object which can be closed.

    https://developer.github.com/v4/interface/closable/

    Implemented by:

    * :class:`github.Issue`
    * :class:`github.PullRequest`
    """

    __slots__ = ()

    @property
    def closed_at(self) -> typing.Optional[datetime.datetime]:
        """
        The date and time at which the closable was closed.
        """

        closed_at = self.data["closedAt"]

        if closed_at:
            return utils.iso_to_datetime(closed_at)

    @property
    def is_closed(self) -> bool:
        """
        Whether or not the closable is closed.
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
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The closable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        if self.data["__typename"] == "Issue":
            await self.http.close_issue(self.id)
        elif self.data["__typename"] == "PullRequest":
            await self.http.close_pull_request(self.id)

    async def reopen(self):
        """
        |coro|

        Reopens the closable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to reopen the closable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The closable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        if self.data["__typename"] == "Issue":
            await self.http.reopen_issue(self.id)
        elif self.data["__typename"] == "PullRequest":
            await self.http.reopen_pull_request(self.id)
