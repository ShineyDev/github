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

from github.enums import Reaction as reaction_enum


class Reactable():
    """
    Represents an object which can be reacted to.

    https://developer.github.com/v4/interface/reactable/

    Implemented by:

    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    """

    __slots__ = ()

    @property
    def reactions(self) -> typing.List["Reaction"]:
        """
        A list of :class:`~github.Reaction`.
        """

        # prevent cyclic imports
        from github.objects import Reaction

        reactions = self.data["reactionGroups"]
        return Reaction.from_data(reactions, self.http)

    @property
    def viewer_can_react(self) -> bool:
        """
        Whether or not the authenticated user can react to this
        reactable.
        """

        return self.data["viewerCanReact"]

    async def add_reaction(self, reaction: str):
        """
        |coro|

        Adds a reaction to the reactable.

        Example
        -------

        .. code:: py

            comment = g.fetch_node("MDU6SXNzdWU0Nzg1MzgwMzA=")
            await comment.add_reaction(github.enums.Reaction.EYES)

        Parameters
        ----------
        reaction: :class:`str`
            The reaction to add.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to add reactions to the
            reactable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The reactable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        if reaction not in reaction_enum._dict.keys():
            reaction = reaction_enum._dict_flipped[reaction]
            
        # TODO: implement HTTPClient.add_reaction
        ...

    async def remove_reaction(self, reaction: str):
        """
        |coro|

        Removes a reaction from the reactable.

        Example
        -------

        .. code:: py

            comment = g.fetch_node("MDU6SXNzdWU0Nzg1MzgwMzA=")
            await comment.remove_reaction(github.enums.Reaction.EYES)

        Parameters
        ----------
        reaction: :class:`str`
            The reaction to remove.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to remove reactions from the
            reactable.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The reactable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        """

        if reaction not in reaction_enum._dict.keys():
            reaction = reaction_enum._dict_flipped[reaction]
            
        # TODO: implement HTTPClient.remove_reaction
        ...
