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

    async def request(self, document_, operation_, variables_, **kwargs):
        headers = kwargs.pop("headers", None) or dict()
        headers["Authorization"] = self.token
        headers["User-Agent"] = self.user_agent

        try:
            data = await super().request(document_, operation_, variables_, headers=headers, **kwargs)
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

    async def _fetch_field(self, document_, *path, _data_validate=None, **kwargs):
        data = await self.request(document_, None, kwargs, _data_validate=_data_validate)
        return github.utils._follow(data, path)

    async def fetch_query_all_codes_of_conduct(self, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "{codesOfConduct{%s}}" % ",".join(fields)
        path = ("codesOfConduct",)

        def validate(data):
            data = github.utils._follow(data, path)

            if any([c.get("body", False) is None for c in data]):
                # NOTE: 1240368
                return (
                    github.ClientResponseGraphQLValidationError,
                    "The GraphQL service failed to fetch a code of conduct body.",
                )

            return None, None

        return await self._fetch_field(query, *path, _data_validate=validate)

    async def fetch_query_code_of_conduct(self, key, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "query($key:String!){codeOfConduct(key:$key){%s}}" % ",".join(fields)
        path = ("codeOfConduct",)

        def validate(data):
            data = github.utils._follow(data, path)

            if data is None:
                # NOTE: 1143102
                return (
                    github.ClientResponseGraphQLNotFoundError,
                    f"Could not resolve to a code of conduct with the key '{key}'.",
                )

            if data.get("body", False) is None:
                # NOTE: 1240368
                return (
                    github.ClientResponseGraphQLValidationError,
                    "The GraphQL service failed to fetch the CodeOfConduct body.",
                )

            return None, None

        data = await self._fetch_field(query, *path, key=key, _data_validate=validate)

        if "key" not in data.keys():
            data["key"] = key

        return data


__all__ = [
    "HTTPClient",
]
