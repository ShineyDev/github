import aiohttp
import graphql


class Client(graphql.client.Client):
    def __init__(self, token: str, *, session: aiohttp.ClientSession, user_agent: str=...) -> None: ...
