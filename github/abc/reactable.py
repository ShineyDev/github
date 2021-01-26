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

class Reactable():
    """
    Represents an entity that can be reacted to.
    """

    __slots__ = ()

    @property
    def viewer_can_react(self):
        """
        Whether the authenticated user can react to the reactable.

        :type: :class:`bool`
        """

        return self.data["viewerCanReact"]

    async def fetch_reaction_groups(self):
        """
        |coro|

        Fetches groups of reactions from the reactable.

        Returns
        -------
        List[:class:`~github.ReactionGroup`]
            The groups of reactions on the reactable.
        """

        from github.objects import ReactionGroup

        data = await self.http.fetch_reactable_reaction_groups(self.id)
        return ReactionGroup.from_data(data, self.http)

    def fetch_reactions(self, *, content=None, order_by=None, **kwargs):
        """
        |aiter|

        Fetches reactions from the reactable.

        Parameters
        ----------
        content: :class:`~github.enums.Reaction`
            The reaction to filter results to.
        order_by: :class:`~github.enums.ReactionOrderField`
            The field to order reactions by.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.Reaction`.
        """

        order_by = order_by and order_by.value

        from github.objects import Reaction

        def map_func(data):
            return Reaction.from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_reactable_reactions,
            self.id,
            content,
            order_by,
            map_func=map_func,
            **kwargs
        )
