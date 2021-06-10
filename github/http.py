import functools
import operator
import uuid

import aiohttp
import graphql

import github


class HTTPClient(graphql.client.HTTPClient):
    __slots__ = ("token", "user_agent", "uuid")

    def __init__(self, token, session, user_agent):
        super().__init__(session=session, url="https://api.github.com/graphql")

        self.uuid = str(uuid.uuid4())

        self.token = f"bearer {token}"
        self.user_agent = user_agent or f"ShineyDev/github@{github.version}:{self.uuid}"

    async def request(self, document, operation, variables):
        headers = {
            "Authorization": self.token,
            "User-Agent": self.user_agent,
        }

        try:
            data = await super().request(document, operation, variables, headers=headers)
        except graphql.client.ClientResponseHTTPError as e:
            try:
                exc_type = github.errors._response_error_map[e.response.status]
            except KeyError:
                exc_type = github.ClientResponseHTTPError

            raise exc_type(e.message, e.response, e.data) from e
        except graphql.client.ClientResponseGraphQLError as e:
            try:
                exc_type = github.errors._response_error_map[e.data["errors"][0]["type"]]
            except KeyError:
                exc_type = github.ClientResponseGraphQLError

            raise exc_type(e.message, e.response, e.data) from e
        except graphql.client.ClientResponseError as e:
            raise github.ClientResponseError(e) from e
        except graphql.client.ClientError as e:
            raise github.ClientError(e) from e
        else:
            return data

    async def fetch_field(self, __query, *path, **kwargs):
        data = await self.request(__query, kwargs)
        return functools.reduce(operator.getitem, path, data)


__all__ = [
    "HTTPClient",
]
