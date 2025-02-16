from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Iterable, Tuple, cast, overload

    from aiohttp import ClientResponse, ClientSession
    from github.api.metadata import MetadataData
    from github.api.ratelimit import RateLimitData
    from github.automation.bot import BotData
    from github.automation.mannequin import MannequinData
    from github.connection.connection import ConnectionData
    from github.content import CodeOfConduct, License
    from github.content.announcement import AnnouncementData
    from github.content.codeofconduct import CodeOfConductData
    from github.content.language import LanguageData
    from github.content.license import LicenseData
    from github.content.reaction import ReactionData
    from github.git.blob import BlobData
    from github.git.commit import CommitData
    from github.git.reference import ReferenceData
    from github.git.tag import TagData
    from github.git.tree import TreeData
    from github.interfaces import Node, Resource
    from github.interfaces.assignable import AssignableData
    from github.interfaces.labelable import LabelableData
    from github.interfaces.reactable import ReactableData
    from github.interfaces.repositoryowner import RepositoryOwnerData
    from github.interfaces.starrable import StarrableData
    from github.interfaces.subscribable import SubscribableData
    from github.organization.organization import OrganizationData
    from github.organization.team import TeamData
    from github.repository import Topic
    from github.repository.discussion import DiscussionData
    from github.repository.discussioncategory import DiscussionCategoryData
    from github.repository.issue import IssueData
    from github.repository.label import LabelData
    from github.repository.milestone import MilestoneData
    from github.repository.pull import PullData
    from github.repository.release import ReleaseData
    from github.repository.repository import RepositoryData
    from github.repository.topic import TopicData
    from github.security.advisory import AdvisoryData
    from github.security.vulnerability import VulnerabilityData
    from github.user import User, UserStatus
    from github.user.user import UserData, ViewerData
    from github.user.userstatus import UserStatusData
    from github.utility.types import T_json_key, T_json_object, T_json_value

import uuid

import graphql

import github
from github.utility import MISSING


DEFAULT_MAXIMUM_NODES: int = 50
DEFAULT_MINIMUM_NODES: int = 10


class HTTPClient(graphql.client.http.HTTPClient):
    __slots__ = ("token", "user_agent", "uuid")

    def __init__(
        self,
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
        self,
        document_: str,
        operation_: str | None,
        variables_: T_json_object,
        /,
        *,
        headers: dict[str, str] = MISSING,
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

    async def _fetch(
        self,
        document_: str,
        /,
        *path: T_json_key,
        _data_validate: Any | None = None,  # TODO
        **kwargs,  # TODO
    ) -> T_json_value:
        data = await self.request(document_, None, kwargs, _data_validate=_data_validate)
        return github.utility.follow(data, path)

    async def fetch_announcementowner_announcement(
        self,
        /,
        announcementowner_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> AnnouncementData | None:
        fields = github.utility.get_merged_graphql_fields(github.Announcement, fields)
        query = "query($announcementowner_id: ID!){node(id:$announcementowner_id){...on Enterprise{announcementBanner{%(f)s}}...on Organization{announcementBanner{%(f)s}}}}" % {"f": ",".join(fields)}
        path = ("node", "announcementBanner")

        data = await self._fetch(query, *path, announcementowner_id=announcementowner_id)

        return data  # type: ignore

    async def fetch_assigneeaddevent_assignee(
        self,
        /,
        assigneeaddevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> MannequinData | UserData:
        mannequin_fields = github.utility.get_merged_graphql_fields(github.Mannequin, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($assigneeaddevent_id:ID!){node(id:$assigneeaddevent_id){...on AssignedEvent{assignee{...on Mannequin{%s}...on User{%s}}}}}" % (",".join(mannequin_fields), ",".join(user_fields))
        path = ("node", "assignee")

        data = await self._fetch(query, *path, assigneeaddevent_id=assigneeaddevent_id)

        if TYPE_CHECKING:
            data = cast(MannequinData | UserData, data)

        return data

    async def fetch_assigneeaddevent_subject(
        self,
        /,
        assigneeaddevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($assigneeaddevent_id:ID!){node(id:$assigneeaddevent_id){...on AssignedEvent{assignable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "assignable")

        data = await self._fetch(query, *path, assigneeaddevent_id=assigneeaddevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_assigneeremoveevent_assignee(
        self,
        /,
        assigneeremoveevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> MannequinData | UserData:
        mannequin_fields = github.utility.get_merged_graphql_fields(github.Mannequin, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($assigneeremoveevent_id:ID!){node(id:$assigneeremoveevent_id){...on UnassignedEvent{assignee{...on Mannequin{%s}...on User{%s}}}}}" % (",".join(mannequin_fields), ",".join(user_fields))
        path = ("node", "assignee")

        data = await self._fetch(query, *path, assigneeremoveevent_id=assigneeremoveevent_id)

        if TYPE_CHECKING:
            data = cast(MannequinData | UserData, data)

        return data

    async def fetch_assigneeremoveevent_subject(
        self,
        /,
        assigneeremoveevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($assigneeremoveevent_id:ID!){node(id:$assigneeremoveevent_id){...on UnassignedEvent{assignable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "assignable")

        data = await self._fetch(query, *path, assigneeremoveevent_id=assigneeremoveevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_childaddevent_parent(
        self,
        /,
        childaddevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($childaddevent_id:ID!){node(id:$childaddevent_id){...on SubIssueAddedEvent{subIssue{%s}}}}" % ",".join(fields)
        path = ("node", "subIssue")

        data = await self._fetch(query, *path, childaddevent_id=childaddevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData, data)

        return data

    async def fetch_childremoveevent_parent(
        self,
        /,
        childremoveevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($childremoveevent_id:ID!){node(id:$childremoveevent_id){...on SubIssueRemovedEvent{subIssue{%s}}}}" % ",".join(fields)
        path = ("node", "subIssue")

        data = await self._fetch(query, *path, childremoveevent_id=childremoveevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData, data)

        return data

    async def fetch_closeevent_subject(
        self,
        /,
        closeevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($closeevent_id:ID!){node(id:$closeevent_id){...on ClosedEvent{closable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "closable")

        data = await self._fetch(query, *path, closeevent_id=closeevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_comment_author(
        self,
        /,
        comment_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> BotData | MannequinData | UserData:
        bot_fields = github.utility.get_merged_graphql_fields(github.Bot, fields)
        mannequin_fields = github.utility.get_merged_graphql_fields(github.Mannequin, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($comment_id:ID!){node(id:$comment_id){...on Comment{author{...on Bot{%s}...on Mannequin{%s}...on User{%s}}}}}" % (",".join(bot_fields), ",".join(mannequin_fields), ",".join(user_fields))
        path = ("node", "author")

        data = await self._fetch(query, *path, comment_id=comment_id)

        if TYPE_CHECKING:
            data = cast(BotData | MannequinData | UserData, data)

        return data

    async def fetch_comment_editor(
        self,
        /,
        comment_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> BotData | UserData | None:
        bot_fields = github.utility.get_merged_graphql_fields(github.Bot, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($comment_id:ID!){node(id:$comment_id){...on Comment{author{...on Bot{%s}...on User{%s}}}}}" % (",".join(bot_fields), ",".join(user_fields))
        path = ("node", "editor")

        data = await self._fetch(query, *path, comment_id=comment_id)

        if data is None:
            return None

        if TYPE_CHECKING:
            data = cast(BotData | UserData, data)

        return data

    async def fetch_discussion_category(
        self,
        /,
        discussion_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> DiscussionCategoryData:
        fields = github.utility.get_merged_graphql_fields(github.DiscussionCategory, fields)
        query = "query($discussion_id:ID!){node(id:$discussion_id){...on Discussion{category{%s}}}}" % ",".join(fields)
        path = ("node", "category")

        return await self._fetch(query, *path, discussion_id=discussion_id)  # type: ignore

    async def fetch_issue_milestone(
        self,
        /,
        issue_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> MilestoneData | None:
        fields = github.utility.get_merged_graphql_fields(github.Milestone, fields)
        query = "query($issue_id:ID!){node(id:$issue_id){...on Issue{milestone{%s}}}}" % ",".join(fields)
        path = ("node", "milestone")

        return await self._fetch(query, *path, issue_id=issue_id)  # type: ignore

    async def fetch_issue_parent(
        self,
        /,
        issue_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | None:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($issue_id:ID!){node(id:$issue_id){...on Issue{parent{%s}}}}" % ",".join(fields)
        path = ("node", "parent")

        return await self._fetch(query, *path, issue_id=issue_id)  # type: ignore

    async def fetch_labeladdevent_label(
        self,
        /,
        labeladdevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> LabelData:
        fields = github.utility.get_merged_graphql_fields(github.Label, fields)
        query = "query($labeladdevent_id:ID!){node(id:$labeladdevent_id){...on LabeledEvent{label{%s}}}}" % ",".join(fields)
        path = ("node", "label")

        data = await self._fetch(query, *path, labeladdevent_id=labeladdevent_id)

        if TYPE_CHECKING:
            data = cast(LabelData, data)

        return data

    async def fetch_labeladdevent_subject(
        self,
        /,
        labeladdevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($labeladdevent_id:ID!){node(id:$labeladdevent_id){...on LabeledEvent{labelable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "labelable")

        data = await self._fetch(query, *path, labeladdevent_id=labeladdevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_labelremoveevent_label(
        self,
        /,
        labelremoveevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> LabelData:
        fields = github.utility.get_merged_graphql_fields(github.Label, fields)
        query = "query($labelremoveevent_id:ID!){node(id:$labelremoveevent_id){...on UnlabeledEvent{label{%s}}}}" % ",".join(fields)
        path = ("node", "label")

        data = await self._fetch(query, *path, labelremoveevent_id=labelremoveevent_id)

        if TYPE_CHECKING:
            data = cast(LabelData, data)

        return data

    async def fetch_labelremoveevent_subject(
        self,
        /,
        labelremoveevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($labelremoveevent_id:ID!){node(id:$labelremoveevent_id){...on UnlabeledEvent{labelable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "labelable")

        data = await self._fetch(query, *path, labelremoveevent_id=labelremoveevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_lockevent_subject(
        self,
        /,
        lockevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($lockevent_id:ID!){node(id:$lockevent_id){...on LockedEvent{lockable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "lockable")

        data = await self._fetch(query, *path, lockevent_id=lockevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_organization_team(
        self,
        /,
        organization_id: str,
        team_slug: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> TeamData:
        fields = github.utility.get_merged_graphql_fields(github.Team, fields)
        query = "query($organization_id:ID!,$team_slug:String!){node(id:$organization_id){...on Organization{team(slug:$team_slug){%s}}}}" % ",".join(fields)
        path = ("node", "team")

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if value is None:
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a team with the slug '{team_slug}'.", response, data)

        data = await self._fetch(query, *path, organization_id=organization_id, team_slug=team_slug, _data_validate=validate)

        if TYPE_CHECKING:
            data = cast(TeamData, data)

        if "slug" not in data.keys():
            data["slug"] = team_slug

        return data

    async def fetch_parentaddevent_parent(
        self,
        /,
        parentaddevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($parentaddevent_id:ID!){node(id:$parentaddevent_id){...on ParentIssueAddedEvent{parent{%s}}}}" % ",".join(fields)
        path = ("node", "parent")

        data = await self._fetch(query, *path, parentaddevent_id=parentaddevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData, data)

        return data

    async def fetch_parentremoveevent_parent(
        self,
        /,
        parentremoveevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($parentremoveevent_id:ID!){node(id:$parentremoveevent_id){...on ParentIssueRemovedEvent{parent{%s}}}}" % ",".join(fields)
        path = ("node", "parent")

        data = await self._fetch(query, *path, parentremoveevent_id=parentremoveevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData, data)

        return data

    async def fetch_pinevent_subject(
        self,
        /,
        pinevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($pinevent_id:ID!){node(id:$pinevent_id){...on PinnedEvent{issue{%s}}}}" % ",".join(fields)
        path = ("node", "issue")

        data = await self._fetch(query, *path, pinevent_id=pinevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData, data)

        return data

    async def fetch_pull_milestone(
        self,
        /,
        pull_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> MilestoneData | None:
        fields = github.utility.get_merged_graphql_fields(github.Milestone, fields)
        query = "query($pull_id:ID!){node(id:$pull_id){...on PullRequest{milestone{%s}}}}" % ",".join(fields)
        path = ("node", "milestone")

        return await self._fetch(query, *path, pull_id=pull_id)  # type: ignore

    async def fetch_query_all_codes_of_conduct(
        self,
        /,
        *,
        fields: Iterable[str] = MISSING,
    ) -> list[CodeOfConductData]:
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
        self,
        /,
        *,
        fields: Iterable[str] = MISSING,
    ) -> list[LicenseData]:
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
        self,
        /,
        key: str,
        *,
        fields: Iterable[str] = MISSING,
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
        self,
        /,
        key: str,
        *,
        fields: Iterable[str] = MISSING,
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
        self,
        /,
        *,
        fields: Iterable[str] = MISSING,
    ) -> MetadataData:
        fields = github.utility.get_merged_graphql_fields(github.Metadata, fields)
        query = "{meta{%s}}" % ",".join(fields)
        path = ("meta",)

        value = await self._fetch(query, *path)

        return value  # type: ignore

    if TYPE_CHECKING:

        @overload
        async def fetch_query_node(
            self,
            /,
            type: type[CodeOfConduct],
            id: str,
            *,
            fields: Iterable[str] = ...,
        ) -> CodeOfConductData: ...

        @overload
        async def fetch_query_node(
            self,
            /,
            type: type[License],
            id: str,
            *,
            fields: Iterable[str] = ...,
        ) -> LicenseData: ...

        @overload
        async def fetch_query_node(
            self,
            /,
            type: type[Topic],
            id: str,
            *,
            fields: Iterable[str] = ...,
        ) -> TopicData: ...

        @overload
        async def fetch_query_node(
            self,
            /,
            type: type[User],
            id: str,
            *,
            fields: Iterable[str] = ...,
        ) -> UserData: ...

        @overload
        async def fetch_query_node(
            self,
            /,
            type: type[UserStatus],
            id: str,
            *,
            fields: Iterable[str] = ...,
        ) -> UserStatusData: ...

    async def fetch_query_node(
        self,
        /,
        type: type[Node],
        id: str,
        *,
        fields: Iterable[str] = MISSING,
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

    async def fetch_query_organization(
        self,
        login: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> OrganizationData:
        fields = github.utility.get_merged_graphql_fields(github.Organization, fields)
        query = "query($login:String!){organization(login:$login){%s}}" % ",".join(fields)
        path = ("organization",)

        data = await self._fetch(query, *path, login=login)

        if TYPE_CHECKING:
            data = cast(OrganizationData, data)

        if "login" not in data.keys():
            data["login"] = login

        return data

    async def fetch_query_rate_limit(
        self,
        /,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RateLimitData:
        fields = github.utility.get_merged_graphql_fields(github.RateLimit, fields)
        query = "{rateLimit(dryRun:true){%s}}" % ",".join(fields)
        path = ("rateLimit",)

        value = await self._fetch(query, *path)

        return value  # type: ignore

    async def fetch_query_repository(
        self,
        /,
        owner: str,
        name: str,
        follow_renames: bool | None,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RepositoryData:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($follow_renames:Boolean,$name:String!,$owner:String!){repository(followRenames:$follow_renames,name:$name,owner:$owner){%s}}" % ",".join(fields)
        path = ("repository",)

        data = await self._fetch(query, *path, owner=owner, name=name, follow_renames=follow_renames)

        if TYPE_CHECKING:
            data = cast(RepositoryData, data)

        if follow_renames is False:
            if "name" not in data.keys():
                data["name"] = name

            if "nameWithOwner" not in data.keys():
                data["nameWithOwner"] = f"{owner}/{name}"

        return data

    async def fetch_query_repository_owner(
        self,
        /,
        login: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> OrganizationData | UserData:
        organization_fields = github.utility.get_merged_graphql_fields(github.Organization, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($login:String!){repositoryOwner(login:$login){...on Organization{%s}...on User{%s}}}" % (",".join(organization_fields), ",".join(user_fields))
        path = ("repositoryOwner",)

        data = await self._fetch(query, *path, login=login)

        if TYPE_CHECKING:
            data = cast(OrganizationData | UserData, data)

        return data

    if TYPE_CHECKING:

        @overload
        async def fetch_query_resource(
            self,
            /,
            type: type[CodeOfConduct],
            url: str,
            *,
            fields: Iterable[str] = ...,
        ) -> CodeOfConductData: ...

        @overload
        async def fetch_query_resource(
            self,
            /,
            type: type[User],
            url: str,
            *,
            fields: Iterable[str] = ...,
        ) -> UserData: ...

    async def fetch_query_resource(
        self,
        /,
        type: type[Resource],
        url: str,
        *,
        fields: Iterable[str] = MISSING,
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
        self,
        name: str,
        *,
        fields: Iterable[str] = MISSING,
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
        self,
        login: str,
        *,
        fields: Iterable[str] = MISSING,
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

        return value

    async def fetch_query_viewer(
        self,
        *,
        fields: Iterable[str] = MISSING,
    ) -> ViewerData:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query{viewer{%s}}" % ",".join(fields)
        path = ("viewer",)

        value = await self._fetch(query, *path)

        if TYPE_CHECKING:
            value = cast(ViewerData, value)

        if "isViewer" not in value.keys():
            value["isViewer"] = True

        return value

    async def fetch_reaction_author(
        self,
        /,
        reaction_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> UserData | None:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($reaction_id:ID!){node(id:$reaction_id){...on Reaction{user{%s}}}}" % ",".join(fields)
        path = ("node", "user")

        return await self._fetch(query, *path, reaction_id=reaction_id)  # type: ignore

    async def fetch_reference_target(
        self,
        /,
        reference_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> CommitData | TagData:
        commit_fields = github.utility.get_merged_graphql_fields(github.Commit, fields)
        tag_fields = github.utility.get_merged_graphql_fields(github.Tag, fields)
        query = "query($reference_id:ID!){node(id:$reference_id){...on Ref{target{...on Commit{%s}...on Tag{%s}}}}}" % (",".join(commit_fields), ",".join(tag_fields))
        path = ("node", "target")

        return await self._fetch(query, *path, reference_id=reference_id)  # type: ignore

    async def fetch_reopenevent_subject(
        self,
        /,
        reopenevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($reopenevent_id:ID!){node(id:$reopenevent_id){...on ReopenedEvent{closable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "closable")

        data = await self._fetch(query, *path, reopenevent_id=reopenevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_repository_code_of_conduct(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> CodeOfConductData | None:
        fields = github.utility.get_merged_graphql_fields(github.CodeOfConduct, fields)
        query = "query($repository_id:ID!){node(id:$repository_id){...on Repository{codeOfConduct{%s}}}}" % ",".join(fields)
        path = ("node", "codeOfConduct")

        return await self._fetch(query, *path, repository_id=repository_id)  # type: ignore

    async def fetch_repository_discussion(
        self,
        /,
        repository_id: str,
        number: int,
        *,
        fields: Iterable[str] = MISSING,
    ) -> DiscussionData:
        fields = github.utility.get_merged_graphql_fields(github.Discussion, fields)
        query = "query($number:Int!,$repository_id:ID!){node(id:$repository_id){...on Repository{discussion(number:$number){%s}}}}" % ",".join(fields)
        path = ("node", "discussion")

        data = await self._fetch(query, *path, repository_id=repository_id, number=number)

        if TYPE_CHECKING:
            data = cast(DiscussionData, data)

        if "number" not in data.keys():
            data["number"] = number

        return data

    async def fetch_repository_discussion_category(
        self,
        /,
        repository_id: str,
        discussioncategory_slug: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> DiscussionCategoryData:
        fields = github.utility.get_merged_graphql_fields(github.DiscussionCategory, fields)
        query = "query($discussioncategory_slug:String!,$repository_id:ID!){node(id:$repository_id){...on Repository{discussionCategory(slug:$discussioncategory_slug){%s}}}}" % ",".join(fields)
        path = ("node", "discussionCategory")

        data = await self._fetch(query, *path, repository_id=repository_id, discussioncategory_slug=discussioncategory_slug)

        if TYPE_CHECKING:
            data = cast(DiscussionCategoryData, data)

        if "slug" not in data.keys():
            data["slug"] = discussioncategory_slug

        return data

    async def fetch_repository_issue(
        self,
        /,
        repository_id: str,
        number: int,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($number:Int!,$repository_id:ID!){node(id:$repository_id){...on Repository{issue(number:$number){%s}}}}" % ",".join(fields)
        path = ("node", "issue")

        data = await self._fetch(query, *path, repository_id=repository_id, number=number)

        if TYPE_CHECKING:
            data = cast(IssueData, data)

        if "number" not in data.keys():
            data["number"] = number

        return data

    async def fetch_repository_issue_or_pull(
        self,
        /,
        repository_id: str,
        number: int,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($number:Int!,$repository_id:ID!){node(id:$repository_id){...on Repository{issueOrPullRequest(number:$number){...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "issueOrPullRequest")

        data = await self._fetch(query, *path, repository_id=repository_id, number=number)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        if "number" not in data.keys():
            data["number"] = number

        return data

    async def fetch_repository_label(
        self,
        /,
        repository_id: str,
        name: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> LabelData:
        fields = github.utility.get_merged_graphql_fields(github.Label, fields)
        query = "query($name:String!,$repository_id:ID!){node(id:$repository_id){...on Repository{label(name:$name){%s}}}}" % ",".join(fields)
        path = ("node", "label")

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(LabelData, value)

            if value is None:
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a label with the name '{name}'.", response, data)

        data = await self._fetch(query, *path, repository_id=repository_id, name=name, _data_validate=validate)

        if TYPE_CHECKING:
            data = cast(LabelData, data)

        if "name" not in data.keys():
            data["name"] = name

        return data

    async def fetch_repository_language(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> LanguageData | None:
        fields = github.utility.get_merged_graphql_fields(github.Language, fields)
        query = "query($repository_id:ID!){node(id:$repository_id){...on Repository{primaryLanguage{%s}}}}" % ",".join(fields)
        path = ("node", "primaryLanguage")

        return await self._fetch(query, *path, repository_id=repository_id)  # type: ignore

    async def fetch_repository_latest_release(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> ReleaseData | None:
        fields = github.utility.get_merged_graphql_fields(github.Release, fields)
        query = "query($repository_id:ID!){node(id:$repository_id){...on Repository{latestRelease{%s}}}}" % ",".join(fields)
        path = ("node", "latestRelease")

        return await self._fetch(query, *path, repository_id=repository_id)  # type: ignore

    async def fetch_repository_license(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> LicenseData | None:
        fields = github.utility.get_merged_graphql_fields(github.License, fields)
        query = "query($repository_id:ID!){node(id:$repository_id){...on Repository{licenseInfo{%s}}}}" % ",".join(fields)
        path = ("node", "licenseInfo")

        return await self._fetch(query, *path, repository_id=repository_id)  # type: ignore

    async def fetch_repository_milestone(
        self,
        /,
        repository_id: str,
        number: int,
        *,
        fields: Iterable[str] = MISSING,
    ) -> MilestoneData:
        fields = github.utility.get_merged_graphql_fields(github.Milestone, fields)
        query = "query($number:Int!,$repository_id:ID!){node(id:$repository_id){...on Repository{milestone(number:$number){%s}}}}" % ",".join(fields)
        path = ("node", "milestone")

        data = await self._fetch(query, *path, repository_id=repository_id, number=number)

        if TYPE_CHECKING:
            data = cast(MilestoneData, data)

        if "number" not in data.keys():
            data["number"] = number

        return data

    async def fetch_repository_object(
        self,
        /,
        repository_id: str,
        object_id: str | None,
        object_expression: str | None,
        *,
        fields: Iterable[str] = MISSING,
    ) -> BlobData | CommitData | TagData | TreeData:
        blob_fields = github.utility.get_merged_graphql_fields(github.Blob, fields)
        commit_fields = github.utility.get_merged_graphql_fields(github.Commit, fields)
        tag_fields = github.utility.get_merged_graphql_fields(github.Tag, fields)
        tree_fields = github.utility.get_merged_graphql_fields(github.Tree, fields)
        query = "query($object_expression:String,$object_id:GitObjectID,$repository_id:ID!){node(id:$repository_id){...on Repository{object(expression:$object_expression,oid:$object_id){...on Blob{%s}...on Commit{%s}...on Tag{%s}...on Tree{%s}}}}}" % (",".join(blob_fields), ",".join(commit_fields), ",".join(tag_fields), ",".join(tree_fields))
        path = ("node", "object")

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if value is None:
                if object_expression:
                    raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to an object with the expression '{object_expression}'.", response, data)
                else:
                    raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to an object with the id '{object_id}'.", response, data)

        data = await self._fetch(query, *path, repository_id=repository_id, object_id=object_id, object_expression=object_expression, _data_validate=validate)

        if TYPE_CHECKING:
            data = cast(BlobData | CommitData | TagData | TreeData, data)

        if object_id:
            if "oid" not in data.keys():
                data["oid"] = object_id

        return data

    async def fetch_repository_owner(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> OrganizationData | UserData:
        organization_fields = github.utility.get_merged_graphql_fields(github.Organization, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($repository_id:ID!){node(id:$repository_id){...on Repository{owner{...on Organization{%s}...on User{%s}}}}}" % (",".join(organization_fields), ",".join(user_fields))
        path = ("node", "owner")

        return await self._fetch(query, *path, repository_id=repository_id)  # type: ignore

    async def fetch_repository_parent(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RepositoryData | None:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($repository_id:ID!){node(id:$repository_id){...on Repository{parent{%s}}}}" % ",".join(fields)
        path = ("node", "parent")

        return await self._fetch(query, *path, repository_id=repository_id)  # type: ignore

    async def fetch_repository_pull(
        self,
        /,
        repository_id: str,
        number: int,
        *,
        fields: Iterable[str] = MISSING,
    ) -> PullData:
        fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($number:Int!,$repository_id:ID!){node(id:$repository_id){...on Repository{pullRequest(number:$number){%s}}}}" % ",".join(fields)
        path = ("node", "pullRequest")

        data = await self._fetch(query, *path, repository_id=repository_id, number=number)

        if TYPE_CHECKING:
            data = cast(PullData, data)

        if "number" not in data.keys():
            data["number"] = number

        return data

    async def fetch_repository_reference(
        self,
        /,
        repository_id: str,
        name: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> ReferenceData:
        fields = github.utility.get_merged_graphql_fields(github.Reference, fields)
        query = "query($name:String!,$repository_id:ID!){node(id:$repository_id){...on Repository{ref(qualifiedName:$name){%s}}}}" % ",".join(fields)
        path = ("node", "ref")

        return await self._fetch(query, *path, repository_id=repository_id, name=name)  # type: ignore

    async def fetch_repository_release(
        self,
        /,
        repository_id: str,
        tag_name: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> ReleaseData:
        fields = github.utility.get_merged_graphql_fields(github.Release, fields)
        query = "query($repository_id:ID!,$tag_name:String!){node(id:$repository_id){...on Repository{release(tagName:$tag_name){%s}}}}" % ",".join(fields)
        path = ("node", "release")

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if TYPE_CHECKING:
                value = cast(ReleaseData | None, value)

            if value is None:
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a release with the tag '{tag_name}'.", response, data)

        data = await self._fetch(query, *path, repository_id=repository_id, tag_name=tag_name, _data_validate=validate)

        if TYPE_CHECKING:
            data = cast(ReleaseData, data)

        return data

    async def fetch_repository_template(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RepositoryData | None:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($repository_id:ID!){node(id:$repository_id){...on Repository{templateRepository{%s}}}}" % ",".join(fields)
        path = ("node", "templateRepository")

        return await self._fetch(query, *path, repository_id=repository_id)  # type: ignore

    async def fetch_repositorynode_repository(
        self,
        /,
        repositorynode_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RepositoryData:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($repositorynode_id:ID!){node(id:$repositorynode_id){...on Label{repository{%(f)s}}...on Milestone{repository{%(f)s}}...on Ref{repository{%(f)s}}...on Release{repository{%(f)s}}...on RepositoryNode{repository{%(f)s}}}}" % {"f": ",".join(fields)}
        path = ("node", "repository")

        data = await self._fetch(query, *path, repositorynode_id=repositorynode_id)

        if TYPE_CHECKING:
            data = cast(RepositoryData, data)

        return data

    async def fetch_repositoryowner_repository(
        self,
        /,
        repositoryowner_id: str,
        name: str,
        follow_renames: bool | None,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RepositoryData:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($follow_renames:Boolean,$name:String!,$repositoryowner_id:ID!){node(id:$repositoryowner_id){...on RepositoryOwner{repository(followRenames:$follow_renames,name:$name){%s}}}}" % ",".join(fields)
        path = ("node", "repository")

        data = await self._fetch(query, *path, repositoryowner_id=repositoryowner_id, name=name, follow_renames=follow_renames)

        if TYPE_CHECKING:
            data = cast(RepositoryData, data)

        if follow_renames is False:
            if "name" not in data.keys():
                data["name"] = name

        return data

    async def fetch_subscribeevent_subject(
        self,
        /,
        subscribeevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($subscribeevent_id:ID!){node(id:$subscribeevent_id){...on SubscribedEvent{subscribable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "subscribable")

        data = await self._fetch(query, *path, subscribeevent_id=subscribeevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_tag_target(
        self,
        /,
        tag_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> BlobData | CommitData | TreeData:
        blob_fields = github.utility.get_merged_graphql_fields(github.Blob, fields)
        commit_fields = github.utility.get_merged_graphql_fields(github.Commit, fields)
        tree_fields = github.utility.get_merged_graphql_fields(github.Tree, fields)
        query = "query($tag_id:ID!){node(id:$tag_id){...on Tag{target{...on Blob{%s}...on Commit{%s}...on Tree{%s}}}}}" % (",".join(blob_fields), ",".join(commit_fields), ",".join(tree_fields))
        path = ("node", "target")

        return await self._fetch(query, *path, tag_id=tag_id)  # type: ignore

    async def fetch_timelineitem_actor(
        self,
        /,
        timelineitem_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> BotData | MannequinData | OrganizationData | UserData:
        bot_fields = github.utility.get_merged_graphql_fields(github.Bot, fields)
        mannequin_fields = github.utility.get_merged_graphql_fields(github.Mannequin, fields)
        organization_fields = github.utility.get_merged_graphql_fields(github.Organization, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        raise NotImplementedError  # TODO: this query
        query = "" % {"bf": ",".join(bot_fields), "mf": ",".join(mannequin_fields), "of": ",".join(organization_fields), "uf": ",".join(user_fields)}
        path = ("node", "actor")

        return await self._fetch(query, *path, timelineitem_id=timelineitem_id)  # type: ignore

    async def fetch_topic_related_topics(
        self,
        /,
        topic_id: str,
        limit: int | None,
        *,
        fields: Iterable[str] = MISSING,
    ) -> tuple[TopicData, ...]:
        fields = github.utility.get_merged_graphql_fields(github.Topic, fields)
        query = "query($topic_id:ID!,$limit:Int){node(id:$topic_id){...on Topic{relatedTopics(first:$limit){%s}}}}" % ",".join(fields)
        path = ("node", "relatedTopics")

        value = await self._fetch(query, *path, limit=limit, topic_id=topic_id)

        return value  # type: ignore

    async def fetch_unlockevent_subject(
        self,
        /,
        unlockevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($unlockevent_id:ID!){node(id:$unlockevent_id){...on UnlockedEvent{lockable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "lockable")

        data = await self._fetch(query, *path, unlockevent_id=unlockevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_unpinevent_subject(
        self,
        /,
        unpinevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($unpinevent_id:ID!){node(id:$unpinevent_id){...on UnpinnedEvent{issue{%s}}}}" % ",".join(fields)
        path = ("node", "issue")

        data = await self._fetch(query, *path, unpinevent_id=unpinevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData, data)

        return data

    async def fetch_unsubscribeevent_subject(
        self,
        /,
        unsubscribeevent_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> IssueData | PullData:
        issue_fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        pull_fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($unsubscribeevent_id:ID!){node(id:$unsubscribeevent_id){...on UnsubscribedEvent{subscribable{...on Issue{%s}...on PullRequest{%s}}}}}" % (",".join(issue_fields), ",".join(pull_fields))
        path = ("node", "subscribable")

        data = await self._fetch(query, *path, unsubscribeevent_id=unsubscribeevent_id)

        if TYPE_CHECKING:
            data = cast(IssueData | PullData, data)

        return data

    async def fetch_user_organization(
        self,
        /,
        user_id: str,
        organization_login: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> OrganizationData:
        fields = github.utility.get_merged_graphql_fields(github.Organization, fields)
        query = "query($organization_login:String!,$user_id:ID!){node(id:$user_id){...on User{organization(login:$organization_login){%s}}}}" % ",".join(fields)
        path = ("node", "organization")

        def validate(
            response: ClientResponse,
            data: T_json_object,
            /,
        ) -> None:
            value = github.utility.follow(data, ("data", *path))

            if value is None:
                raise github.ClientResponseGraphQLNotFoundError(f"Could not resolve to a organization with the name '{organization_login}'.", response, data)

        data = await self._fetch(query, *path, user_id=user_id, organization_login=organization_login, _data_validate=validate)

        if TYPE_CHECKING:
            data = cast(OrganizationData, data)

        if "login" not in data.keys():
            data["login"] = organization_login

        return data

    async def fetch_user_status(
        self,
        /,
        user_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> UserStatusData:
        fields = github.utility.get_merged_graphql_fields(github.UserStatus, fields)
        query = "query($user_id:ID!){node(id:$user_id){...on User{status{%s}}}}" % ",".join(fields)
        path = ("node", "status")

        value = await self._fetch(query, *path, user_id=user_id)

        return value  # type: ignore

    async def fetch_userstatus_organization(
        self,
        /,
        userstatus_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> OrganizationData | None:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($userstatus_id:ID!){node(id:$userstatus_id){...on UserStatus{organization{%s}}}}" % ",".join(fields)
        path = ("node", "organization")

        data = await self._fetch(query, *path, userstatus_id=userstatus_id)

        if data is None:
            return None

        if TYPE_CHECKING:
            data = cast(OrganizationData, data)

        return data

    async def fetch_userstatus_user(
        self,
        /,
        userstatus_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> UserData:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)

        # NOTE: this holds together the hack in User._from_data
        if "isViewer" not in fields:
            fields.append("isViewer")

        query = "query($userstatus_id:ID!){node(id:$userstatus_id){...on UserStatus{user{%s}}}}" % ",".join(fields)
        path = ("node", "user")

        data = await self._fetch(query, *path, userstatus_id=userstatus_id)

        if TYPE_CHECKING:
            data = cast(UserData, data)

        return data

    async def _collect(
        self,
        document_: str,
        /,
        *path: T_json_key,
        _data_validate: Any | None = None,  # TODO
        cursor: str | None,
        length: int | None,
        reverse: bool,
        **kwargs,
    ) -> ConnectionData[Any]:
        direction_name = "last" if reverse else "first"
        position_name = "before" if reverse else "after"

        kwargs[direction_name] = length if length is not None else DEFAULT_MAXIMUM_NODES
        kwargs[position_name] = cursor

        data = await self._fetch(document_, *path, _data_validate=_data_validate, **kwargs)

        if TYPE_CHECKING:
            data = cast(ConnectionData[Any], data)

        if reverse:
            try:
                data["edges"] = list(reversed(data["edges"]))
            except KeyError:
                pass

            try:
                data["nodes"] = list(reversed(data["nodes"]))
            except KeyError:
                pass

        return data

    async def collect_advisory_vulnerabilities(
        self,
        /,
        advisory_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[VulnerabilityData]:
        fields = github.utility.get_merged_graphql_fields(github.Vulnerability, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:SecurityVulnerabilityOrder,$advisory_id:ID!){node(id:$advisory_id){...on SecurityAdvisory{vulnerabilities(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "vulnerabilities")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, advisory_id=advisory_id, order_by=order_by_data, **kwargs)

    async def collect_assignable_assignees(
        self,
        /,
        assignable_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($assignable_id:ID!){node(id:$assignable_id){...on Assignable{assignees(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "assignees")

        return await self._collect(query, *path, assignable_id=assignable_id, **kwargs)

    async def collect_discussionauthor_discussions(
        self,
        /,
        discussionauthor_id: str,
        order_by: str | None,
        repository_id: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[DiscussionData]:
        fields = github.utility.get_merged_graphql_fields(github.Discussion, fields)
        query = "query($after:String,$before:String,$discussionauthor_id:ID!,$first:Int,$last:Int,$order_by:DiscussionOrder,$repository_id:ID){node(id:$discussionauthor_id){...on RepositoryDiscussionAuthor{repositoryDiscussions(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by,repositoryId:$repository_id){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "repositoryDiscussions")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, discussionauthor_id=discussionauthor_id, order_by=order_by_data, repository_id=repository_id, **kwargs)

    async def collect_issue_children(
        self,
        /,
        issue_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[IssueData]:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($issue_id:ID!){node(id:$issue_id){...on Issue{subIssues(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "subIssues")

        return await self._collect(query, *path, issue_id=issue_id, **kwargs)

    async def collect_issue_participants(
        self,
        /,
        issue_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($issue_id:ID!){node(id:$issue_id){...on Issue{participants(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "participants")

        return await self._collect(query, *path, issue_id=issue_id, **kwargs)

    async def collect_label_issues(
        self,
        /,
        label_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[IssueData]:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$label_id:ID!){node(id:$label_id){...on Label{issues(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "issues")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, label_id=label_id, order_by=order_by_data, **kwargs)

    async def collect_label_pulls(
        self,
        /,
        label_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[PullData]:
        fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$label_id:ID!){node(id:$label_id){...on Label{pullRequests(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "pullRequests")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, label_id=label_id, order_by=order_by_data, **kwargs)

    async def collect_labelable_labels(
        self,
        /,
        labelable_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[LabelData]:
        fields = github.utility.get_merged_graphql_fields(github.Label, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:LabelOrder,$labelable_id:ID!){node(id:$labelable_id){...on Labelable{labels(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "labels")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, labelable_id=labelable_id, order_by=order_by_data, **kwargs)

    async def collect_milestone_issues(
        self,
        /,
        milestone_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[IssueData]:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$milestone_id:ID!){node(id:$milestone_id){...on Milestone{issues(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "issues")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, milestone_id=milestone_id, order_by=order_by_data, **kwargs)

    async def collect_milestone_pulls(
        self,
        /,
        milestone_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[PullData]:
        fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$milestone_id:ID!){node(id:$milestone_id){...on Milestone{pullRequests(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "pullRequests")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, milestone_id=milestone_id, order_by=order_by_data, **kwargs)

    async def collect_organization_mannequins(
        self,
        /,
        organization_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[MannequinData]:
        fields = github.utility.get_merged_graphql_fields(github.Mannequin, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:MannequinOrder,$organization_id:ID!){node(id:$organization_id){...on Organization{mannequins(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "mannequins")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, organization_id=organization_id, order_by=order_by_data, **kwargs)

    async def collect_organization_teams(
        self,
        /,
        organization_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[TeamData]:
        fields = github.utility.get_merged_graphql_fields(github.Team, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:TeamOrder,$organization_id:ID!){node(id:$organization_id){...on Organization{teams(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "teams")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, organization_id=organization_id, order_by=order_by_data, **kwargs)

    async def collect_pull_participants(
        self,
        /,
        pull_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($pull_id:ID!){node(id:$pull_id){...on PullRequest{participants(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "participants")

        return await self._collect(query, *path, pull_id=pull_id, **kwargs)

    async def collect_query_advisories(
        self,
        /,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[AdvisoryData]:
        fields = github.utility.get_merged_graphql_fields(github.Advisory, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:SecurityAdvisoryOrder){securityAdvisories(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}" % ",".join(fields)
        path = ("securityAdvisories",)

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, order_by=order_by_data, **kwargs)

    async def collect_query_sponsorables(
        self,
        /,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[OrganizationData | UserData]:
        organization_fields = github.utility.get_merged_graphql_fields(github.Organization, fields)
        user_fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:SponsorableOrder){sponsorables(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{...on Organization{%s}...on User{%s}},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}" % (",".join(organization_fields), ",".join(user_fields))
        path = ("sponsorables",)

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, order_by=order_by_data, **kwargs)

    async def collect_query_vulnerabilities(
        self,
        /,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[VulnerabilityData]:
        fields = github.utility.get_merged_graphql_fields(github.Vulnerability, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:SecurityVulnerabilityOrder){securityVulnerabilities(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}" % ",".join(fields)
        path = ("securityVulnerabilities",)

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, order_by=order_by_data, **kwargs)

    async def collect_reactable_reactions(
        self,
        /,
        reactable_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[ReactionData]:
        fields = github.utility.get_merged_graphql_fields(github.Reaction, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:ReactionOrder,$reactable_id:ID!){node(id:$reactable_id){...on Reactable{reactions(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "reactions")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, reactable_id=reactable_id, order_by=order_by_data, **kwargs)

    async def collect_reference_pulls(
        self,
        /,
        reference_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[PullData]:
        fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$reference_id:ID!){node(id:$reference_id){...on Ref{associatedPullRequests(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "associatedPullRequests")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, reference_id=reference_id, order_by=order_by_data, **kwargs)

    async def collect_repository_assignable_users(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$repository_id:ID!){node(id:$repository_id){...on Repository{assignableUsers(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "assignableUsers")

        return await self._collect(query, *path, repository_id=repository_id, **kwargs)

    async def collect_repository_collaborators(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$repository_id:ID!){node(id:$repository_id){...on Repository{collaborators(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "collaborators")

        return await self._collect(query, *path, repository_id=repository_id, **kwargs)

    async def collect_repository_discussion_categories(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[DiscussionData]:
        fields = github.utility.get_merged_graphql_fields(github.DiscussionCategory, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$repository_id:ID!){node(id:$repository_id){...on Repository{discussionCategories(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "discussionCategories")

        return await self._collect(query, *path, repository_id=repository_id, **kwargs)

    async def collect_repository_discussions(
        self,
        /,
        repository_id: str,
        discussioncategory_id: str | None,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[DiscussionData]:
        fields = github.utility.get_merged_graphql_fields(github.Discussion, fields)
        query = "query($after:String,$before:String,$discussioncategory_id:ID,$first:Int,$last:Int,$order_by:DiscussionOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{discussions(after:$after,before:$before,categoryId:$discussioncategory_id,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "discussions")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, discussioncategory_id=discussioncategory_id, order_by=order_by_data, **kwargs)

    async def collect_repository_forks(
        self,
        /,
        repository_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[RepositoryData]:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:RepositoryOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{forks(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "forks")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, order_by=order_by_data, **kwargs)

    async def collect_repository_issues(
        self,
        /,
        repository_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[IssueData]:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{issues(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "issues")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, order_by=order_by_data, **kwargs)

    async def collect_repository_labels(
        self,
        /,
        repository_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[LabelData]:
        fields = github.utility.get_merged_graphql_fields(github.Label, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:LabelOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{labels(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "labels")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, order_by=order_by_data, **kwargs)

    async def collect_repository_languages(
        self,
        /,
        repository_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[LanguageData]:
        fields = github.utility.get_merged_graphql_fields(github.Language, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:LanguageOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{languages(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "languages")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, order_by=order_by_data, **kwargs)

    async def collect_repository_milestones(
        self,
        /,
        repository_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[MilestoneData]:
        fields = github.utility.get_merged_graphql_fields(github.Milestone, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:MilestoneOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{milestones(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "milestones")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, order_by=order_by_data, **kwargs)

    async def collect_repository_pulls(
        self,
        /,
        repository_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[PullData]:
        fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{pullRequests(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "pullRequests")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, order_by=order_by_data, **kwargs)

    async def collect_repository_references(
        self,
        /,
        repository_id: str,
        reference_prefix: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[ReferenceData]:
        fields = github.utility.get_merged_graphql_fields(github.Reference, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:RefOrder,$reference_prefix:String!,$repository_id:ID!){node(id:$repository_id){...on Repository{refs(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by,refPrefix:$reference_prefix){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "refs")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, reference_prefix=reference_prefix, order_by=order_by_data, **kwargs)

    async def collect_repository_releases(
        self,
        /,
        repository_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[LabelData]:
        fields = github.utility.get_merged_graphql_fields(github.Release, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:ReleaseOrder,$repository_id:ID!){node(id:$repository_id){...on Repository{releases(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "releases")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repository_id=repository_id, order_by=order_by_data, **kwargs)

    async def collect_repository_topics(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[TopicData]:
        fields = github.utility.get_merged_graphql_fields(github.Topic, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$repository_id:ID!){node(id:$repository_id){...on Repository{repositoryTopics(after:$after,before:$before,first:$first,last:$last){nodes{topic{%s}},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "repositoryTopics")

        data = await self._collect(query, *path, repository_id=repository_id, **kwargs)

        nodes = list()

        for node in data["nodes"]:
            nodes.append(node["topic"])

        data["nodes"] = nodes

        return data

    async def collect_repository_mentionable_users(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$repository_id:ID!){node(id:$repository_id){...on Repository{mentionableUsers(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "mentionableUsers")

        return await self._collect(query, *path, repository_id=repository_id, **kwargs)

    async def collect_repository_watchers(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$repository_id:ID!){node(id:$repository_id){...on Repository{watchers(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "watchers")

        return await self._collect(query, *path, repository_id=repository_id, **kwargs)

    async def collect_repositoryowner_repositories(
        self,
        /,
        repositoryowner_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[RepositoryData]:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:RepositoryOrder,$repositoryowner_id:ID!){node(id:$repositoryowner_id){... on RepositoryOwner{repositories(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "repositories")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, repositoryowner_id=repositoryowner_id, order_by=order_by_data, **kwargs)

    async def collect_starrable_stargazers(
        self,
        /,
        starrable_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:StarOrder,$starrable_id:ID!){node(id:$starrable_id){...on Starrable{stargazers(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "stargazers")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, starrable_id=starrable_id, order_by=order_by_data, **kwargs)

    async def collect_team_ancestors(
        self,
        /,
        team_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[TeamData]:
        fields = github.utility.get_merged_graphql_fields(github.Team, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$team_id:ID!){node(id:$team_id){...on Team{ancestors(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "ancestors")

        return await self._collect(query, *path, team_id=team_id, **kwargs)

    async def collect_topic_repositories(
        self,
        /,
        topic_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[RepositoryData]:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:RepositoryOrder,$topic_id:ID!){node(id:$topic_id){... on Topic{repositories(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "repositories")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, topic_id=topic_id, order_by=order_by_data, **kwargs)

    async def collect_user_followers(
        self,
        /,
        user_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$user_id:ID!){node(id:$user_id){...on User{followers(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "followers")

        return await self._collect(query, *path, user_id=user_id, **kwargs)

    async def collect_user_following(
        self,
        /,
        user_id: str,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[UserData]:
        fields = github.utility.get_merged_graphql_fields(github.User, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$user_id:ID!){node(id:$user_id){...on User{following(after:$after,before:$before,first:$first,last:$last){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "following")

        return await self._collect(query, *path, user_id=user_id, **kwargs)

    async def collect_user_issues(
        self,
        /,
        user_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[IssueData]:
        fields = github.utility.get_merged_graphql_fields(github.Issue, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$user_id:ID!){node(id:$user_id){...on User{issues(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "issues")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, user_id=user_id, order_by=order_by_data, **kwargs)

    async def collect_user_organizations(
        self,
        /,
        user_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[OrganizationData]:
        fields = github.utility.get_merged_graphql_fields(github.Organization, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:OrganizationOrder,$user_id:ID!){node(id:$user_id){...on User{organizations(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "organizations")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, user_id=user_id, order_by=order_by_data, **kwargs)

    async def collect_user_pulls(
        self,
        /,
        user_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[PullData]:
        fields = github.utility.get_merged_graphql_fields(github.Pull, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:IssueOrder,$user_id:ID!){node(id:$user_id){...on User{pullRequests(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "pullRequests")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, user_id=user_id, order_by=order_by_data, **kwargs)

    async def collect_user_watching(
        self,
        /,
        user_id: str,
        order_by: str | None,
        *,
        fields: Iterable[str] = MISSING,
        **kwargs,
    ) -> ConnectionData[RepositoryData]:
        fields = github.utility.get_merged_graphql_fields(github.Repository, fields)
        query = "query($after:String,$before:String,$first:Int,$last:Int,$order_by:RepositoryOrder,$user_id:ID!){node(id:$user_id){... on User{watching(after:$after,before:$before,first:$first,last:$last,orderBy:$order_by){nodes{%s},pageInfo{endCursor,hasNextPage,hasPreviousPage,startCursor}}}}}" % ",".join(fields)
        path = ("node", "watching")

        if order_by is None:
            order_by_data = None
        else:
            order_by_data = {"direction": "ASC", "field": order_by}

        return await self._collect(query, *path, user_id=user_id, order_by=order_by_data, **kwargs)

    async def _mutate(
        self,
        document_: str,
        /,
        *path: T_json_key,
        _data_validate: Any | None = None,  # TODO
        **kwargs,  # TODO
    ) -> T_json_value:
        if "mutation_id" not in kwargs.keys():
            kwargs["mutation_id"] = self.uuid

        return await self._fetch(document_, *path, _data_validate=_data_validate, **kwargs)

    async def mutate_assignable_add_assignees(
        self,
        /,
        assignable_id: str,
        assignee_ids: list[str],
        *,
        fields: Iterable[str] = MISSING,
    ) -> AssignableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($assignable_id:ID!,$assignee_ids:[ID!]!,$mutation_id:String!){addAssigneesToAssignable(input:{clientMutationId:$mutation_id,assignableId:$assignable_id,assigneeIds:$assignee_ids}){assignable{%s}}}" % ",".join(fields)
        path = ("addAssigneesToAssignable", "assignable")

        data = await self._mutate(query, *path, assignable_id=assignable_id, assignee_ids=assignee_ids)

        return data  # type: ignore

    async def mutate_assignable_remove_assignees(
        self,
        /,
        assignable_id: str,
        assignee_ids: list[str],
        *,
        fields: Iterable[str] = MISSING,
    ) -> AssignableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($assignable_id:ID!,$assignee_ids:[ID!]!,$mutation_id:String!){removeAssigneesFromAssignable(input:{clientMutationId:$mutation_id,assignableId:$assignable_id,assigneeIds:$assignee_ids}){assignable{%s}}}" % ",".join(fields)
        path = ("removeAssigneesFromAssignable", "assignable")

        data = await self._mutate(query, *path, assignable_id=assignable_id, assignee_ids=assignee_ids)

        return data  # type: ignore

    async def mutate_label_delete(
        self,
        /,
        label_id: str,
    ) -> None:
        query = "mutation($label_id:ID!,$mutation_id:String!){deleteLabel(input:{clientMutationId:$mutation_id,id:$label_id}){__typename}}"

        await self._mutate(query, label_id=label_id)

    async def mutate_labelable_add_labels(
        self,
        /,
        labelable_id: str,
        label_ids: list[str],
        *,
        fields: Iterable[str] = MISSING,
    ) -> LabelableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($labelable_id:ID!,$label_ids:[ID!]!,$mutation_id:String!){addLabelsToLabelable(input:{clientMutationId:$mutation_id,labelableId:$labelable_id,labelIds:$label_ids}){labelable{%s}}}" % ",".join(fields)
        path = ("addLabelsToLabelable", "labelable")

        data = await self._mutate(query, *path, labelable_id=labelable_id, label_ids=label_ids)

        return data  # type: ignore

    async def mutate_labelable_clear_labels(
        self,
        /,
        labelable_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> LabelableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($labelable_id:ID!,$mutation_id:String!){clearLabelsFromLabelable(input:{clientMutationId:$mutation_id,labelableId:$labelable_id}){labelable{%s}}}" % ",".join(fields)
        path = ("clearLabelsFromLabelable", "labelable")

        data = await self._mutate(query, *path, labelable_id=labelable_id)

        return data  # type: ignore

    async def mutate_labelable_remove_labels(
        self,
        /,
        labelable_id: str,
        label_ids: list[str],
        *,
        fields: Iterable[str] = MISSING,
    ) -> LabelableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($labelable_id:ID!,$label_ids:[ID!]!,$mutation_id:String!){removeLabelsFromLabelable(input:{clientMutationId:$mutation_id,labelableId:$labelable_id,labelIds:$label_ids}){labelable{%s}}}" % ",".join(fields)
        path = ("removeLabelsFromLabelable", "labelable")

        data = await self._mutate(query, *path, labelable_id=labelable_id, label_ids=label_ids)

        return data  # type: ignore

    async def mutate_reactable_add_reaction(
        self,
        /,
        reactable_id: str,
        content: str,
        *,
        reactable_fields: Iterable[str] = MISSING,
        reaction_fields: Iterable[str] = MISSING,
    ) -> tuple[ReactableData, ReactionData]:
        reactable_fields = ("__typename",) if reactable_fields is MISSING else reactable_fields
        reaction_fields = github.utility.get_merged_graphql_fields(github.Reaction, reaction_fields)
        query = "mutation($reactable_id:ID!,$content:ReactionContent!,$mutation_id:String!){addReaction(input:{clientMutationId:$mutation_id,subjectId:$reactable_id,content:$content}){subject{%s},reaction{%s}}}" % (",".join(reactable_fields), ",".join(reaction_fields))
        path = ("addReaction",)

        data = await self._mutate(query, *path, reactable_id=reactable_id, content=content)

        return (data["subject"], data["reaction"])  # type: ignore

    async def mutate_reactable_remove_reaction(
        self,
        /,
        reactable_id: str,
        content: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> ReactableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($reactable_id:ID!,$content:ReactionContent!,$mutation_id:String!){removeReaction(input:{clientMutationId:$mutation_id,subjectId:$reactable_id,content:$content}){subject{%s}}}" % ",".join(fields)
        path = ("removeReaction", "subject")

        data = await self._mutate(query, *path, reactable_id=reactable_id, content=content)

        return data  # type: ignore

    async def mutate_repository_archive(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RepositoryData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($repository_id:ID!,$mutation_id:String!){archiveRepository(input:{clientMutationId:$mutation_id,repositoryId:$repository_id}){repository{%s}}}" % ",".join(fields)
        path = ("archiveRepository", "repository")

        data = await self._mutate(query, *path, repository_id=repository_id)

        return data  # type: ignore

    async def mutate_repository_create_label(
        self,
        /,
        repository_id: str,
        label_name: str,
        label_color: str,
        label_description: str | None,
        *,
        label_fields: Iterable[str] = MISSING,
        repository_fields: Iterable[str] = MISSING,
    ) -> tuple[RepositoryData, LabelData]:
        label_fields = github.utility.get_merged_graphql_fields(github.Label, label_fields)
        repository_fields = ("__typename",) if repository_fields is MISSING else repository_fields
        query = "mutation($label_color:String!,$label_description:String,$label_name:String!,$repository_id:ID!,$mutation_id:String!){createLabel(input:{clientMutationId:$mutation_id,color:$label_color,description:$label_description,name:$label_name,repositoryId:$repository_id}){label{%s,_r:repository{%s}}}}" % (",".join(label_fields), ",".join(repository_fields))
        path = ("createLabel",)

        data = await self._mutate(query, *path, repository_id=repository_id, label_name=label_name, label_color=label_color, label_description=label_description)

        label_data: dict[str, Any] = data["label"]  # type: ignore
        repository_data = label_data.pop("_r")

        return (repository_data, label_data)  # type: ignore

    async def mutate_repository_create_reference(
        self,
        /,
        repository_id: str,
        reference_name: str,
        reference_target: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> tuple[RepositoryData, LabelData]:
        fields = github.utility.get_merged_graphql_fields(github.Reference, fields)
        query = "mutation($reference_name:String!,$reference_target:GitObjectID!,$repository_id:ID!,$mutation_id:String!){createRef(input:{clientMutationId:$mutation_id,name:$reference_name,oid:$reference_target,repositoryId:$repository_id}){ref{%s}}}" % ",".join(fields)
        path = ("createRef",)

        data = await self._mutate(query, *path, repository_id=repository_id, reference_name=reference_name, reference_target=reference_target)

        return data  # type: ignore

    async def mutate_repository_unarchive(
        self,
        /,
        repository_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> RepositoryData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($repository_id:ID!,$mutation_id:String!){unarchiveRepository(input:{clientMutationId:$mutation_id,repositoryId:$repository_id}){repository{%s}}}" % ",".join(fields)
        path = ("unarchiveRepository", "repository")

        data = await self._mutate(query, *path, repository_id=repository_id)

        return data  # type: ignore

    async def mutate_repositoryowner_create_repository(
        self,
        /,
        repositoryowner_id: str | None,
        repository_name: str,
        repository_visibility: str,
        repository_description: str | None,
        *,
        repository_fields: Iterable[str] = MISSING,
        repositoryowner_fields: Iterable[str] = MISSING,
    ) -> tuple[RepositoryOwnerData, RepositoryData]:
        repository_fields = github.utility.get_merged_graphql_fields(github.Repository, repository_fields)
        repositoryowner_fields = ("__typename",) if repositoryowner_fields is MISSING else repositoryowner_fields
        query = "mutation($repository_description:String,$repository_name:String!,$repository_visibility:RepositoryVisibility!,$repositoryowner_id:ID!,$mutation_id:String!){createRepository(input:{clientMutationId:$mutation_id,description:$repository_description,name:$repository_name,visibility:$repository_visibility,ownerId:$repositoryowner_id}){repository{%s,_o:owner{%s}}}}" % (",".join(repository_fields), ",".join(repositoryowner_fields))
        path = ("createRepository",)

        data = await self._mutate(query, *path, repositoryowner_id=repositoryowner_id, repository_name=repository_name, repository_visibility=repository_visibility, repository_description=repository_description)

        repository_data: dict[str, Any] = data["repository"]  # type: ignore
        repositoryowner_data = repository_data.pop("_o")

        return (repositoryowner_data, repository_data)  # type: ignore

    async def mutate_starrable_star(
        self,
        /,
        starrable_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> StarrableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($starrable_id:ID!,$mutation_id:String!){addStar(input:{clientMutationId:$mutation_id,starrableId:$starrable_id}){starrable{%s}}}" % ",".join(fields)
        path = ("addStar", "starrable")

        value = await self._mutate(query, *path, starrable_id=starrable_id)

        return value  # type: ignore

    async def mutate_starrable_unstar(
        self,
        /,
        starrable_id: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> StarrableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($starrable_id:ID!,$mutation_id:String!){removeStar(input:{clientMutationId:$mutation_id,starrableId:$starrable_id}){starrable{%s}}}" % ",".join(fields)
        path = ("removeStar", "starrable")

        value = await self._mutate(query, *path, starrable_id=starrable_id)

        return value  # type: ignore

    async def mutate_subscribable_update_subscription(
        self,
        /,
        subscribable_id: str,
        state: str,
        *,
        fields: Iterable[str] = MISSING,
    ) -> SubscribableData:
        fields = ("__typename",) if fields is MISSING else fields
        query = "mutation($subscribable_id:ID!,$mutation_id:String!,$state:SubscriptionState!){updateSubscription(input:{clientMutationId:$mutation_id,subscribableId:$subscribable_id,state:$state}){subscribable{%s}}}" % ",".join(fields)
        path = ("updateSubscription", "subscribable")

        value = await self._mutate(query, *path, starrable_id=subscribable_id, state=state)

        return value  # type: ignore

    async def mutate_user_update_status(
        self,
        /,
        busy: bool | None,
        emoji: str | None,
        expires_at: str | None,
        message: str | None,
        organization_id: str | None,
        *,
        fields: Iterable[str] = MISSING,
    ) -> UserStatusData | None:
        fields = github.utility.get_merged_graphql_fields(github.UserStatus, fields)
        query = "mutation($busy:Boolean,$emoji:String,$expires_at:DateTime,$message:String,$mutation_id:String!,$organization_id:ID){changeUserStatus(input:{clientMutationId:$mutation_id,emoji:$emoji,expiresAt:$expires_at,limitedAvailability:$busy,message:$message,organizationId:$organization_id}){status{%s}}}" % ",".join(fields)
        path = ("changeUserStatus", "status")

        value = await self._mutate(query, *path, busy=busy, emoji=emoji, expires_at=expires_at, message=message, organization_id=organization_id)

        return value  # type: ignore


__all__ = [
    "HTTPClient",
]
