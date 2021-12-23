from github.interfaces import Starrable, Type


class Topic(Starrable, Type):
    @property
    def name(self) -> str: ...

    async def fetch_name(self) -> str: ...

    async def fetch_related_topics(self, *, limit: int=..., **kwargs) -> list[Topic]: ...
