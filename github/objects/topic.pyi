from typing import List

from github.abc import Node
from github.abc import Type


class Topic(Node, Type):
    @property
    def name(self) -> str: ...

    async def fetch_related_topics(self) -> List[Topic]: ...
