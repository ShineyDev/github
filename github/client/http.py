from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Iterable, cast
    from typing_extensions import Self

    from aiohttp import ClientResponse, ClientSession

    from github.interfaces import Type
    from github.utilities.types import T_json_key, T_json_object, T_json_value

import uuid

import graphql

import github


class HTTPClient(graphql.client.http.HTTPClient):
    __slots__ = ("token", "user_agent", "uuid")

    def __init__(
        self: Self,
        /,
        token: str,
        session: ClientSession,
        user_agent: str | None,
    ) -> None:
        super().__init__(session=session, url="https://api.github.com/graphql")

        self.uuid = str(uuid.uuid4())

        self.token = f"bearer {token}"
        self.user_agent = user_agent or f"ShineyDev/github@{github.version}:{self.uuid}"

    async def request(
        self: Self,
        document_: str,
        operation_: str | None,
        variables_: T_json_object,
        /,
        *,
        headers: dict[str, str] | None = None,
        **kwargs,  # TODO
    ) -> T_json_object:
        headers = headers or dict()
        headers["Authorization"] = self.token
        headers["User-Agent"] = self.user_agent

        try:
            data = await super().request(document_, operation_, variables_, headers=headers, **kwargs)
        except github.ClientError:
            raise
        except graphql.client.ClientResponseHTTPError as e:
            try:
                exc_type = github.client.errors._response_error_map[e.response.status]
            except KeyError:
                exc_type = github.ClientResponseHTTPError

            raise exc_type(e.message, e.response, e.data) from e
        except graphql.client.ClientResponseGraphQLError as e:
            try:
                exc_type = github.client.errors._response_error_map[e.data["errors"][0]["type"]]
            except KeyError:
                exc_type = github.ClientResponseGraphQLError

            raise exc_type(e.message, e.response, e.data) from e
        except graphql.client.ClientResponseError as e:
            raise github.ClientResponseError(e.message) from e
        except graphql.client.ClientError as e:
            raise github.ClientError(e.message) from e
        else:
            return data

    async def _fetch(
        self: Self,
        document_: str,
        /,
        *path: T_json_key,
        _data_validate: Any | None = None,  # TODO
        **kwargs,  # TODO
    ) -> T_json_value:
        data = await self.request(document_, None, kwargs, _data_validate=_data_validate)
        return github.utilities.follow(data, path)

    async def fetch_query_all_codes_of_conduct(
        self: Self,
        /,
        *,
        fields: Iterable[str] | None = None,
    ) -> list[T_json_object]:
        fields = github.utilities.get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "{codesOfConduct{%s}}" % ",".join(fields)
        path = ("codesOfConduct",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utilities.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(list[T_json_object], value)

            if any([c.get("body", False) is None for c in value]):
                # NOTE: (body=null) 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch a code of conduct body.", response, data)

        value = await self._fetch(query, *path, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(list[T_json_object], value)

        return value

    async def fetch_query_all_licenses(
        self: Self,
        /,
        *,
        fields: Iterable[str] | None = None,
    ) -> list[T_json_object]:
        fields = github.utilities.get_merged_graphql_fields(github.License, fields)
        query = "{licenses{%s}}" % ",".join(fields)
        path = ("licenses",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utilities.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(list[T_json_object], value)

            if any([l.get("body", False) == "" for l in value]):
                # NOTE: (body="") 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch a license body.", response, data)

        value = await self._fetch(query, *path, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(list[T_json_object], value)

        return value

    async def fetch_query_code_of_conduct(
        self: Self,
        /,
        key: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utilities.get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "query($key:String!){codeOfConduct(key:$key){%s}}" % ",".join(fields)
        path = ("codeOfConduct",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utilities.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(T_json_object, value)

            if value is None or key == "other":
                # NOTE: (value=null) 1143102
                # NOTE: (key="other") body=null
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a code of conduct with the key '{key}'.", response, data)

            if value.get("body", False) is None:
                # NOTE: (body=null) 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch the code of conduct body.", response, data)

        value = await self._fetch(query, *path, key=key, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(T_json_object, value)

        if "key" not in value.keys():
            value["key"] = key

        return value

    async def fetch_query_license(
        self: Self,
        /,
        key: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utilities.get_merged_graphql_fields(github.License, fields)
        query = "query($key:String!){license(key:$key){%s}}" % ",".join(fields)
        path = ("license",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utilities.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(T_json_object, value)

            if value is None or key == "other":
                # NOTE: (value=null) 1143102
                # NOTE: (key="other") body=""
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a license with the key '{key}'.", response, data)

            if value.get("body", False) == "":
                # NOTE: (body="") 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch the license body.", response, data)

        value = await self._fetch(query, *path, key=key, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(T_json_object, value)

        if "key" not in value.keys():
            value["key"] = key

        return value

    async def fetch_query_metadata(
        self: Self,
        /,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utilities.get_merged_graphql_fields(github.Metadata, fields)
        query = "{meta{%s}}" % ",".join(fields)
        path = ("meta",)

        value = await self._fetch(query, *path)

        if TYPE_CHECKING:
            value = cast(T_json_object, value)

        return value

    async def fetch_query_node(
        self: Self,
        /,
        type: type[Type],
        id: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utilities.get_merged_graphql_fields(type, fields)
        query = "query($id:ID!){node(id:$id){...on %s{%s}}}" % (github.utilities.get_graphql_type(type), ",".join(fields))
        path = ("node",)

        value = await self._fetch(query, *path, id=id)

        if TYPE_CHECKING:
            value = cast(T_json_object, value)

        if "id" not in value.keys():
            value["id"] = id

        return value

    async def fetch_query_rate_limit(
        self: Self,
        /,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utilities.get_merged_graphql_fields(github.RateLimit, fields)
        query = "{rateLimit(dryRun:true){%s}}" % ",".join(fields)
        path = ("rateLimit",)

        value = await self._fetch(query, *path)

        if TYPE_CHECKING:
            value = cast(T_json_object, value)

        return value

    async def fetch_query_resource(
        self: Self,
        /,
        type: type[Type],
        url: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utilities.get_merged_graphql_fields(type, fields)
        query = "query($url:URI!){resource(url:$url){...on %s{%s}}}" % (github.utilities.get_graphql_type(type), ",".join(fields))
        path = ("resource",)

        value = await self._fetch(query, *path, url=url)

        if TYPE_CHECKING:
            value = cast(T_json_object, value)

        if "url" not in value.keys():
            value["url"] = url

        return value

    async def fetch_query_topic(
        self: Self,
        name: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utilities.get_merged_graphql_fields(github.Topic, fields)
        query = "query($name:String!){topic(name:$name){%s}}" % ",".join(fields)
        path = ("topic",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utilities.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(T_json_object, value)

            if value is None:
                # NOTE: (value=null) 1143102
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a topic with the name '{name}'.", response, data)

        value = await self._fetch(query, *path, name=name, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(T_json_object, value)

        if "name" not in value.keys():
            value["name"] = name

        return value

    async def fetch_topic_related_topics(
        self: Self,
        /,
        topic_id: str,
        limit: int | None,
        *,
        fields: Iterable[str] | None = None,
    ) -> list[T_json_object]:
        fields = github.utilities.get_merged_graphql_fields(github.Topic, fields)
        query = "query($topic_id:ID!,$limit:Int){node(id:$topic_id){...on Topic{relatedTopics(first:$limit){%s}}}}" % ",".join(fields)
        path = ("node", "relatedTopics")

        value = await self._fetch(query, *path, limit=limit, topic_id=topic_id)

        if TYPE_CHECKING:
            value = cast(list[T_json_object], value)

        return value


__all__: list[str] = [
    "HTTPClient",
]