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

    # this interface does not have an api equivalent

    __slots__ = ()

    async def fetch_participants(self) -> typing.List["User"]:
        """
        |coro|

        Fetches a list of users participating on the participable.

        Returns
        -------
        List[:class:`~github.User`]
            A list of users.
        """

        from github.objects import User

        map = {
            "Issue": self.http.fetch_issue_participants,
            "PullRequest": self.http.fetch_pull_request_participants,
        }

        meth = map[self.data["__typename"]]
        data = await meth(self.id)

        return User.from_data(data, self.http)
