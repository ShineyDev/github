from typing import List

from github.iterator import CollectionIterator
from github.enums import Reaction as _enums_Reaction
from github.objects import Reaction
from github.objects import ReactionGroup


class Reactable():
    @property
    def viewer_can_react(self) -> bool: ...

    async def fetch_reaction_groups(self) -> List[ReactionGroup]: ...

    def fetch_reactions(self, *, content: _enums_Reaction=..., **kwargs) -> CollectionIterator[Reaction]: ...
