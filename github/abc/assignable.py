"""
/github/abc/assignable.py

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


class Assignable():
    """
    Represents an object which can be assigned to.

    https://developer.github.com/v4/interface/assignable/

    Implemented by:

    * :class:`github.Issue`
    * :class:`github.PullRequest`
    """

    __slots__ = ()

    async def fetch_assignees(self) -> typing.List["User"]:
        """
        |coro|

        Fetches a list of users assigned to the assignable.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The assignable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`github.User`]
            A list of assigned users.
        """

        # prevent cyclic imports
        from github.objects import User

        data = await self.http.fetch_assignable_assignees(self.id)
        return User.from_data(data, self.http)

    async def add_assignees(self, *users: "User"):
        """
        |coro|

        Assigns an iterable of users to the assignable.

        Parameters
        ----------
        \\*users: Iterable[:class:`github.User`]
            An iterable of users.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add assignees to the assignable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The assignable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        users = [user.id for user in users]
        await self.http.add_assignees(self.id, users)

    async def remove_assignees(self, *users: "User"):
        """
        |coro|

        Unassigns an iterable of users from the assignable.

        Parameters
        ----------
        \\*users: Iterable[:class:`github.User`]
            An iterable of users.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to remove assignees from the assignable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The assignable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        users = [user.id for user in users]
        await self.http.remove_assignees(self.id, users)
