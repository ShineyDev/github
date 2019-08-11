"""
/github/abc/reactable.py

    Copyright (c) 2019 ShineyDev
    
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

    .. versionadded:: 0.2.0
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
        Whether or not the authenticated user can react to this reactable.
        """

        return self.data["viewerCanReact"]

    async def add_reaction(self, reaction: str):
        """
        Adds a reaction to the reactable.
        """

        if reaction not in reaction_enum._dict.keys():
            reaction = reaction_enum._dict_flipped[reaction]
            
        # TODO: implement HTTPClient.add_reaction
        ...

    async def remove_reaction(self, reaction: str):
        """
        Removes a reaction from the reactable.
        """

        if reaction not in reaction_enum._dict.keys():
            reaction = reaction_enum._dict_flipped[reaction]
            
        # TODO: implement HTTPClient.remove_reaction
        ...
