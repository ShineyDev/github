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
        except github.ClientError:
            raise
        except graphql.client.ClientResponseHTTPError as e:
            try:
                exc_type = github.errors._response_error_map[e.response.status]
            except KeyError:
                exc_type = github.ClientResponseHTTPError

            raise exc_type(e.message, e.response, e.data) from e
        except graphql.client.ClientResponseGraphQLValidationError as e:
            raise github.ClientResponseGraphQLValidationError(e.message, e.response, e.data)
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

    async def fetch_field(self, __document, *path, _data_validate=None, **kwargs):
        data = await self.request(__document, None, kwargs, _data_validate=_data_validate)
        return functools.reduce(operator.getitem, path, data)

    async def fetch_query_all_codes_of_conduct(self, *, fields=None):
        path = ("codesOfConduct",)

        def validate(data):
            data = functools.reduce(operator.getitem, path, data)

            if any([c["body"] is None for c in data]):
                # NOTE: 1240368
                return (
                    github.ClientResponseGraphQLValidationError,
                    "The GraphQL service failed to fetch the CodeOfConduct body.",
                )

            return None, None

        fields = github.utils._get_fields(github.CodeOfConduct, fields)
        q = "{codesOfConduct{%s}}" % ",".join(fields)
        return await self.fetch_field(q, *path, _data_validate=validate)

    async def fetch_query_code_of_conduct(self, key, *, fields=None):
        path = ("codeOfConduct",)

        def validate(data):
            data = functools.reduce(operator.getitem, path, data)

            if data is None:
                # NOTE: 1143102
                return (
                    github.ClientResponseGraphQLValidationError,
                    f"Could not resolve to a CodeOfConduct with the key '{key}'.",
                )

            if data["body"] is None:
                # NOTE: 1240368
                return (
                    github.ClientResponseGraphQLValidationError,
                    "The GraphQL service failed to fetch the CodeOfConduct body.",
                )

            return None, None

        fields = github.utils._get_fields(github.CodeOfConduct, fields)
        q = "query($key:String!){codeOfConduct(key:$key){%s}}" % ",".join(fields)
        o = await self.fetch_field(q, *path, key=key, _data_validate=validate)
        o.setdefault("key", key)
        return o


__all__ = [
    "HTTPClient",
]
