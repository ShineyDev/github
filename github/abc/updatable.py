"""
/github/abc/updatable.py

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

from github.enums import CannotUpdateReason


class Updatable():
    """
    Represents an object which can be updated.

    https://developer.github.com/v4/interface/updatable/

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def viewer_can_update(self) -> bool:
        """
        Whether or not the authenticated user can update the updatable.
        """

        return self.data["viewerCanUpdate"]

    @property
    def viewer_cannot_update_reasons(self) -> typing.List[CannotUpdateReason]:
        """
        A list of reasons why the authenticated user cannot update this updatable.
        """

        reasons = self.data["viewerCannotUpdateReasons"]
        return CannotUpdateReason.from_data(reasons)

    async def update(self, **kwargs):
        """
        |coro|

        Updates the updatable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to update the updatable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The updatable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        ...
