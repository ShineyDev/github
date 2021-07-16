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

    async def request(self, document, operation, variables, **kwargs):
        headers = kwargs.pop("headers", None) or dict()
        headers["Authorization"] = self.token
        headers["User-Agent"] = self.user_agent

        try:
            data = await super().request(document, operation, variables, headers=headers, **kwargs)
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
            raise github.ClientResponseError(e.message) from e
        except graphql.client.ClientError as e:
            raise github.ClientError(e.message) from e
        else:
            return data

    async def fetch_field(self, __document, *path, **kwargs):
        data = await self.request(__document, None, kwargs)
        return functools.reduce(operator.getitem, path, data)

    async def fetch_query_code_of_conduct(self, key, *, fields=None):
        fields = fields or github.utils._get_fields(github.CodeOfConduct)
        q = "query($key:String!){codeOfConduct(key:$key){%s}}" % ",".join(fields)
        o = await self.fetch_field(q, "codeOfConduct", key=key)
        o.setdefault("key", key)
        return o


__all__ = [
    "HTTPClient",
]
