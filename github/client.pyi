import aiohttp
import graphql

from github.content import CodeOfConduct


class Client:
    def __init__(self, token: str, *, session: aiohttp.ClientSession, user_agent: str=...) -> None: ...

    async def fetch_all_codes_of_conduct(self, **kwargs) -> list[CodeOfConduct]: ...
    async def fetch_code_of_conduct(self, key: str, **kwargs) -> CodeOfConduct: ...
