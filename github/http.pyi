from aiohttp import ClientSession


class HTTPClient():
    async def request(self, *, json: dict, headers: dict=..., session: ClientSession=...) -> dict: ...
