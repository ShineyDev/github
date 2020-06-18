"""
/github/abc/reactable.py

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

from github import utils
from github.enums import Reaction as enums_Reaction


class Reactable():
    """
    Represents an object which can be reacted to.

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    # https://developer.github.com/v4/interface/reactable/

    __slots__ = ()

    @property
    def viewer_can_react(self) -> bool:
        """
        Whether the authenticated user can react to this reactable.

        :type: :class:`bool`
        """

        return self.data["viewerCanReact"]

    async def add_reaction(self, reaction: enums_Reaction):
        """
        |coro|

        Adds a reaction to the reactable.

        Example
        -------

        .. code:: py

            comment = g.fetch_node("MDU6SXNzdWU0Nzg1MzgwMzA=")
            await comment.add_reaction(enums.Reaction.eyes)

        Parameters
        ----------
        reaction: :class:`~github.enums.Reaction`
            The reaction to add.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add reactions to the
            reactable.
        """

        ... # TODO

    async def remove_reaction(self, reaction: enums_Reaction):
        """
        |coro|

        Removes a reaction from the reactable.

        Example
        -------

        .. code:: py

            comment = g.fetch_node("MDU6SXNzdWU0Nzg1MzgwMzA=")
            await comment.remove_reaction(enums.Reaction.eyes)

        Parameters
        ----------
        reaction: :class:`~github.enums.Reaction`
            The reaction to remove.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to remove reactions from the
            reactable.
        """

        ... # TODO
