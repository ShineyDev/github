class Starrable:
    @property
    def stargazer_count(self) -> int: ...
    @property
    def viewer_has_starred(self) -> bool: ...

    async def fetch_stargazer_count(self) -> int: ...
    async def fetch_viewer_has_starred(self) -> bool: ...
