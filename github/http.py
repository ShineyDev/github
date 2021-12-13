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

        def validate(response, data):
            value = github.utils._follow(data["data"], path)

            if any([c.get("body", False) is None for c in value]):
                # NOTE: (body=null) 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch a code of conduct body.", response, data)

        return await self._fetch_field(query, *path, _data_validate=validate)

    async def fetch_query_all_licenses(self, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(github.License, fields)
        query = "{licenses{%s}}" % ",".join(fields)
        path = ("licenses",)

        def validate(response, data):
            value = github.utils._follow(data["data"], path)

            if any([l.get("body", False) == "" for l in value]):
                # NOTE: (body="") 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch a license body.", response, data)

        return await self._fetch_field(query, *path)

    async def fetch_query_code_of_conduct(self, key, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "query($key:String!){codeOfConduct(key:$key){%s}}" % ",".join(fields)
        path = ("codeOfConduct",)

        def validate(response, data):
            value = github.utils._follow(data["data"], path)

            if value is None or key == "other":
                # NOTE: (value=null) 1143102
                # NOTE: (key="other") body=null
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a code of conduct with the key '{key}'.", response, data)

            if value.get("body", False) is None:
                # NOTE: (body=null) 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch the code of conduct body.", response, data)

        value = await self._fetch_field(query, *path, key=key, _data_validate=validate)

        if "key" not in value.keys():
            value["key"] = key

        return value

    async def fetch_query_license(self, key, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(github.License, fields)
        query = "query($key:String!){license(key:$key){%s}}" % ",".join(fields)
        path = ("license",)

        def validate(response, data):
            value = github.utils._follow(data["data"], path)

            if value is None or key == "other":
                # NOTE: (value=null) 1143102
                # NOTE: (key="other") body=""
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a license with the key '{key}'.", response, data)

            if value.get("body", False) == "":
                # NOTE: (body="") 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch the license body.", response, data)

        value = await self._fetch_field(query, *path, key=key, _data_validate=validate)

        if "key" not in value.keys():
            value["key"] = key

        return value

    async def fetch_query_metadata(self, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(github.Metadata, fields)
        query = "{meta{%s}}" % ",".join(fields)
        path = ("meta",)

        return await self._fetch_field(query, *path)

    async def fetch_query_node(self, type, id, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(type, fields)
        query = "query($id:ID!){node(id:$id){...on %s{%s}}}" % (type._graphql_type, ",".join(fields))
        path = ("node",)

        return await self._fetch_field(query, *path, id=id)

    async def fetch_query_rate_limit(self, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(github.RateLimit, fields)
        query = "{rateLimit(dryRun:true){%s}}" % ",".join(fields)
        path = ("rateLimit",)

        return await self._fetch_field(query, *path)

    async def fetch_query_resource(self, type, url, *, fields=None):
        fields = github.utils._get_merged_graphql_fields(type, fields)
        query = "query($url:URI!){resource(url:$url){...on %s{%s}}}" % (type._graphql_type, ",".join(fields))
        path = ("resource",)

        return await self._fetch_field(query, *path, url=url)


__all__ = [
    "HTTPClient",
]
