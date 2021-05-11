import functools
import operator
import uuid

import aiohttp

import github
from github.errors import GraphQLError, HTTPError, error_exception_map


class HTTPClient:
    __slots__ = ("token", "session", "uuid", "base_url", "user_agent")

    def __init__(self, token, session, user_agent):
        self.token = token
        self.session = session

        self.uuid = str(uuid.uuid4())

        self.base_url = "https://api.github.com/graphql"
        self.user_agent = user_agent or f"ShineyDev/github@{github.version}:{self.uuid}"

    async def request(self, document, operation, variables):
        json = dict()
        json["query"] = document

        if operation:
            json["operationName"] = operation

        if variables:
            json["variables"] = variables

        headers = {
            "Authorization": f"bearer {self.token}",
            "User-Agent": self.user_agent,
        }

        async with self.session.post(self.base_url, json=json, headers=headers) as response:
            if not 200 <= response.status < 300:
                try:
                    data = await response.json()
                    message = data["message"]
                except (aiohttp.ContentTypeError, KeyError):
                    data = None
                    message = response.reason

                try:
                    exc_type = error_exception_map[response.status]
                except KeyError:
                    exc_type = HTTPError

                raise exc_type(message, response, data)

            data = await response.json()

            try:
                errors = data["errors"]
            except KeyError:
                errors = None

            if errors:
                exceptions = list()

                for error in errors:
                    message = error["message"]

                    try:
                        exc_type = error_exception_map[error["type"]]
                    except KeyError:
                        exc_type = GraphQLError

                    exceptions.append(exc_type(message, response, data))

                if False:  # len(exceptions) > 1:
                    # TODO: I'm not sure I love this interface.
                    raise GraphQLErrorCollection(exceptions)
                else:
                    raise exceptions[0]

        return data["data"]

    async def fetch_field(self, _query, *path, **kwargs):
        data = await self.request(_query, kwargs)
        return functools.reduce(operator.getitem, path, data)


__all__ = [
    "HTTPClient",
]
