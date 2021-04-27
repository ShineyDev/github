from aiohttp import ClientSession


class Client:
    def __init__(self, token: str, *, session: ClientSession, user_agent: str=...) -> None: ...

    async def request(self, query: str, variables: dict=...) -> dict: ...
