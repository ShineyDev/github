"""
/github/abc/participable.py

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


class Participable():
    """
    Represents an object which can be participated in.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    async def fetch_participants(self) -> typing.List["User"]:
        """
        |coro|

        Fetches a list of users participating on the participable.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The participable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.User`]
            A list of users participating on the participable.
        """

        from github.objects import User

        if self.data["__typename"] == "Issue":
            data = await self.http.fetch_issue_participants(self.id)
        elif self.data["__typename"] == "PullRequest":
            data = await self.http.fetch_pull_request_participants(self.id)

        return User.from_data(data, self.http)
