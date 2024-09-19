from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Iterable, Tuple, cast, overload
    from typing_extensions import Self

    from aiohttp import ClientResponse, ClientSession
    from github.connection.metadata import MetadataData
    from github.connection.ratelimit import RateLimitData
    from github.content import CodeOfConduct, License
    from github.content.codeofconduct import CodeOfConductData
    from github.content.license import LicenseData
    from github.interfaces import Node, UniformResourceLocatable
    from github.interfaces.profileowner import ProfileOwnerData
    from github.interfaces.starrable import StarrableData
    from github.repository import Topic
    from github.repository.topic import TopicData
    from github.user import User, UserStatus
    from github.user.user import UserData
    from github.user.userstatus import UserStatusData
    from github.utility.types import T_json_key, T_json_object, T_json_value

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
        self.user_agent = (user_agent or "ShineyDev/github@{version}:{uuid}").format(uuid=self.uuid, version=github.version)

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
                exc_type = github.core.errors._response_error_map[e.response.status]
            except KeyError:
                exc_type = github.ClientResponseHTTPError

            raise exc_type(e.message, e.response, e.data) from e
        except graphql.client.ClientResponseGraphQLError as e:
            try:
                exc_type = github.core.errors._response_error_map[e.data["errors"][0]["type"]]
            except KeyError:
                exc_type = github.ClientResponseGraphQLError

            raise exc_type(e.message, e.response, e.data) from e
        except graphql.client.ClientResponseError as e:
            raise github.ClientResponseError(e.message, e.response) from e
        except graphql.client.ClientError as e:
            raise github.ClientError(e.message) from e
        else:
            return data

    def _patch_profileownerdata(
        self: Self,
        data: ProfileOwnerData,
        /,
    ) -> ProfileOwnerData:
        if data.get("email", False) == "":
            data["email"] = None

        return data

    def _patch_userdata(
        self: Self,
        data: UserData,
        /,
    ) -> UserData:
        data = self._patch_profileownerdata(data)  # type: ignore

        if data.get("bio", False) == "":
            data["bio"] = None

        if data.get("bioHTML", False) == "":
            data["bioHTML"] = None

        if data.get("companyHTML", False) == "":
            data["companyHTML"] = None

        if data.get("pronouns", False) == "":
            data["pronouns"] = None

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
        return github.utility.follow(data, path)

    async def fetch_query_all_codes_of_conduct(
        self: Self,
        /,
        *,
        fields: Iterable[str] | None = None,
    ) -> tuple[CodeOfConductData, ...]:
        fields = github.utility.get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "{codesOfConduct{%s}}" % ",".join(fields)
        path = ("codesOfConduct",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(Tuple[CodeOfConductData, ...], value)

            if any([c.get("body", False) is None for c in value]):
                # NOTE: (body=null) 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch a code of conduct body.", response, data)

        value = await self._fetch(query, *path, _data_validate=validate)

        return value  # type: ignore

    async def fetch_query_all_licenses(
        self: Self,
        /,
        *,
        fields: Iterable[str] | None = None,
    ) -> tuple[LicenseData, ...]:
        fields = github.utility.get_merged_graphql_fields(github.License, fields)
        query = "{licenses{%s}}" % ",".join(fields)
        path = ("licenses",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(Tuple[LicenseData, ...], value)

            if any([l.get("body", False) == "" for l in value]):
                # NOTE: (body="") 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch a license body.", response, data)

        value = await self._fetch(query, *path, _data_validate=validate)

        return value  # type: ignore

    async def fetch_query_code_of_conduct(
        self: Self,
        /,
        key: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> CodeOfConductData:
        fields = github.utility.get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "query($key:String!){codeOfConduct(key:$key){%s}}" % ",".join(fields)
        path = ("codeOfConduct",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(CodeOfConductData, value)

            if value is None or key == "other":
                # NOTE: (value=null) 1143102
                # NOTE: (key="other") body=null
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a code of conduct with the key '{key}'.", response, data)

            if value.get("body", False) is None:
                # NOTE: (body=null) 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch the code of conduct body.", response, data)

        value = await self._fetch(query, *path, key=key, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(CodeOfConductData, value)

        if "key" not in value.keys():
            value["key"] = key

        return value

    async def fetch_query_license(
        self: Self,
        /,
        key: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> LicenseData:
        fields = github.utility.get_merged_graphql_fields(github.License, fields)
        query = "query($key:String!){license(key:$key){%s}}" % ",".join(fields)
        path = ("license",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(LicenseData, value)

            if value is None or key == "other":
                # NOTE: (value=null) 1143102
                # NOTE: (key="other") body=""
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a license with the key '{key}'.", response, data)

            if value.get("body", False) == "":
                # NOTE: (body="") 1240368
                raise github.ClientResponseGraphQLInternalError("The GraphQL service failed to fetch the license body.", response, data)

        value = await self._fetch(query, *path, key=key, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(LicenseData, value)

        if "key" not in value.keys():
            value["key"] = key

        return value

    async def fetch_query_metadata(
        self: Self,
        /,
        *,
        fields: Iterable[str] | None = None,
    ) -> MetadataData:
        fields = github.utility.get_merged_graphql_fields(github.Metadata, fields)
        query = "{meta{%s}}" % ",".join(fields)
        path = ("meta",)

        value = await self._fetch(query, *path)

        return value  # type: ignore

    if TYPE_CHECKING:

        @overload
        async def fetch_query_node(
            self: Self,
            /,
            type: type[CodeOfConduct],
            id: str,
            *,
            fields: Iterable[str] | None = None,
        ) -> CodeOfConductData:
            pass

        @overload
        async def fetch_query_node(
            self: Self,
            /,
            type: type[License],
            id: str,
            *,
            fields: Iterable[str] | None = None,
        ) -> LicenseData:
            pass

        @overload
        async def fetch_query_node(
            self: Self,
            /,
            type: type[Topic],
            id: str,
            *,
            fields: Iterable[str] | None = None,
        ) -> TopicData:
            pass

        @overload
        async def fetch_query_node(
            self: Self,
            /,
            type: type[User],
            id: str,
            *,
            fields: Iterable[str] | None = None,
        ) -> UserData:
            pass

        @overload
        async def fetch_query_node(
            self: Self,
            /,
            type: type[UserStatus],
            id: str,
            *,
            fields: Iterable[str] | None = None,
        ) -> UserStatusData:
            pass

    async def fetch_query_node(
        self: Self,
        /,
        type: type[Node],
        id: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utility.get_merged_graphql_fields(type, fields)
        query = "query($id:ID!){node(id:$id){...on %s{%s}}}" % (github.utility.get_graphql_type(type), ",".join(fields))
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
    ) -> RateLimitData:
        fields = github.utility.get_merged_graphql_fields(github.RateLimit, fields)
        query = "{rateLimit(dryRun:true){%s}}" % ",".join(fields)
        path = ("rateLimit",)

        value = await self._fetch(query, *path)

        return value  # type: ignore

    if TYPE_CHECKING:

        @overload
        async def fetch_query_resource(
            self: Self,
            /,
            type: type[CodeOfConduct],
            url: str,
            *,
            fields: Iterable[str] | None = None,
        ) -> CodeOfConductData:
            pass

        @overload
        async def fetch_query_resource(
            self: Self,
            /,
            type: type[User],
            url: str,
            *,
            fields: Iterable[str] | None = None,
        ) -> UserData:
            pass

    async def fetch_query_resource(
        self: Self,
        /,
        type: type[UniformResourceLocatable],
        url: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> T_json_object:
        fields = github.utility.get_merged_graphql_fields(type, fields)
        query = "query($url:URI!){resource(url:$url){...on %s{%s}}}" % (github.utility.get_graphql_type(type), ",".join(fields))
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
    ) -> TopicData:
        fields = github.utility.get_merged_graphql_fields(github.Topic, fields)
        query = "query($name:String!){topic(name:$name){%s}}" % ",".join(fields)
        path = ("topic",)

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(TopicData, value)

            if value is None:
                # NOTE: (value=null) 1143102
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a topic with the name '{name}'.", response, data)

        value = await self._fetch(query, *path, name=name, _data_validate=validate)

        if TYPE_CHECKING:
            value = cast(TopicData, value)

        if "name" not in value.keys():
            value["name"] = name

        return value

    async def fetch_query_user(
        self: Self,
        login: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> UserData:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)

        # NOTE: this holds together the hack in User._from_data
        if "isViewer" not in fields:
            fields.append("isViewer")

        query = "query($login:String!){user(login:$login){%s}}" % ",".join(fields)
        path = ("user",)

        value = await self._fetch(query, *path, login=login)

        if TYPE_CHECKING:
            value = cast(UserData, value)

        if "login" not in value.keys():
            value["login"] = login

        value = self._patch_userdata(value)

        return value

    async def fetch_query_viewer(
        self: Self,
        *,
        fields: Iterable[str] | None = None,
    ) -> UserData:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query{viewer{%s}}" % ",".join(fields)
        path = ("viewer",)

        value = await self._fetch(query, *path)

        if TYPE_CHECKING:
            value = cast(UserData, value)

        if "isViewer" not in value.keys():
            value["isViewer"] = True

        value = self._patch_userdata(value)

        return value

    async def fetch_topic_related_topics(
        self: Self,
        /,
        topic_id: str,
        limit: int | None,
        *,
        fields: Iterable[str] | None = None,
    ) -> tuple[TopicData, ...]:
        fields = github.utility.get_merged_graphql_fields(github.Topic, fields)
        query = "query($topic_id:ID!,$limit:Int){node(id:$topic_id){...on Topic{relatedTopics(first:$limit){%s}}}}" % ",".join(fields)
        path = ("node", "relatedTopics")

        value = await self._fetch(query, *path, limit=limit, topic_id=topic_id)

        return value  # type: ignore

    async def fetch_user_status(
        self: Self,
        /,
        user_id: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> UserStatusData:
        fields = github.utility.get_merged_graphql_fields(github.UserStatus, fields)
        query = "query($user_id:ID!){node(id:$user_id){...on User{status{%s}}}}" % ",".join(fields)
        path = ("node", "status")

        value = await self._fetch(query, *path, user_id=user_id)

        return value  # type: ignore

    async def fetch_userstatus_user(
        self: Self,
        /,
        userstatus_id: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> UserData:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($userstatus_id:ID!){node(id:$userstatus_id){...on UserStatus{user{%s}}}}" % ",".join(fields)
        path = ("node", "user")

        data = await self._fetch(query, *path, userstatus_id=userstatus_id)

        return data  # type: ignore

    async def _mutate(
        self: Self,
        document_: str,
        /,
        *path: T_json_key,
        _data_validate: Any | None = None,  # TODO
        **kwargs,  # TODO
    ) -> T_json_value:
        if "mutation_id" not in kwargs.keys():
            kwargs["mutation_id"] = self.uuid

        return await self._fetch(document_, *path, _data_validate=_data_validate, **kwargs)

    async def mutate_starrable_star(
        self: Self,
        /,
        starrable_id: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> StarrableData:
        fields = github.utility.get_merged_graphql_fields(github.Starrable, fields)
        query = "mutation($starrable_id:ID!,$mutation_id:String!){addStar(input:{clientMutationId:$mutation_id,starrableId:$starrable_id}){starrable{%s}}}" % ",".join(fields)
        path = ("addStar", "starrable")

        value = await self._mutate(query, *path, starrable_id=starrable_id)

        return value  # type: ignore

    async def mutate_starrable_unstar(
        self: Self,
        /,
        starrable_id: str,
        *,
        fields: Iterable[str] | None = None,
    ) -> StarrableData:
        fields = github.utility.get_merged_graphql_fields(github.Starrable, fields)
        query = "mutation($starrable_id:ID!,$mutation_id:String!){removeStar(input:{clientMutationId:$mutation_id,starrableId:$starrable_id}){starrable{%s}}}" % ",".join(fields)
        path = ("removeStar", "starrable")

        value = await self._mutate(query, *path, starrable_id=starrable_id)

        return value  # type: ignore

    async def mutate_user_update_status(
        self: Self,
        /,
        busy: bool | None,
        emoji: str | None,
        expires_at: str | None,
        message: str | None,
        organization_id: str | None,
        *,
        fields: Iterable[str] | None = None,
    ) -> UserStatusData | None:
        fields = github.utility.get_merged_graphql_fields(github.UserStatus, fields)
        query = "mutation($busy:Boolean,$emoji:String,$expires_at:DateTime,$message:String,$mutation_id:String!,$organization_id:ID){changeUserStatus(input:{clientMutationId:$mutation_id,emoji:$emoji,expiresAt:$expires_at,limitedAvailability:$busy,message:$message,organizationId:$organization_id}){status{%s}}}" % ",".join(fields)
        path = ("changeUserStatus", "status")

        # NOTE: temporary patch for 3004533
        busy = busy if busy is not None else False

        value = await self._mutate(query, *path, busy=busy, emoji=emoji, expires_at=expires_at, message=message, organization_id=organization_id)

        return value  # type: ignore


__all__: list[str] = [
    "HTTPClient",
]
