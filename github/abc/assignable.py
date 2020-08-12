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

from github.iterator import CollectionIterator


class Assignable():
    """
    Represents an object which can be assigned to.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    # https://docs.github.com/en/graphql/reference/interfaces#assignable

    __slots__ = ()

    def fetch_assignees(self, **kwargs):
        """
        |aiter|

        Fetches users assigned to the assignable.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.User`.
        """

        from github.objects import User

        def map_func(data):
            return User.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_assignable_assignees,
                                  self.id, map_func=map_func, **kwargs)

    async def add_assignees(self, *users):
        """
        |coro|

        Assigns users to the assignable.

        Parameters
        ----------
        *users: :class:`~github.User`
            An iterable of users.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add assignees to the
            assignable.
        """

        # https://docs.github.com/en/graphql/reference/mutations#addassigneestoassignable

        users = [user.id for user in users]
        await self.http.mutate_assignable_add_assignees(self.id, users)

    async def remove_assignees(self, *users):
        """
        |coro|

        Unassigns users from the assignable.

        Parameters
        ----------
        *users: :class:`~github.User`
            An iterable of users.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to remove assignees from the
            assignable.
        """

        # https://docs.github.com/en/graphql/reference/mutations#removeassigneesfromassignable

        users = [user.id for user in users]
        await self.http.mutate_assignable_remove_assignees(self.id, users)
