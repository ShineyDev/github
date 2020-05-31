"""
/github/http.py

    Copyright (c) 2019-2020 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import functools
import operator
import uuid

import aiohttp

from github import context
from github import errors
from github import query


_DEFAULT_BASE_URL = "https://api.github.com/graphql"
_DEFAULT_USER_AGENT = "ShineyDev/github.py:{0}"


class HTTPClient():
    """
    Represents a GitHub 'connection' or client.

    This class contains the behind-the-scenes code for the
    :class:`~github.GitHub` class and should not be created by
    the user.

    This class is only exposed for :meth:`~HTTPClient.request`.
    """

    __slots__ = ("_exception_map", "_token", "_base_url", "_user_agent", "_uuid", "_session")

    def __init__(self, token, *, base_url=None, user_agent=None, session=None):
        self._exception_map = {
            # HTTP status-code
            401: errors.Unauthorized,

            # GitHub API status-message
            "FORBIDDEN": errors.Forbidden,
            "INTERNAL": errors.Internal,
            "NOT_FOUND": errors.NotFound,
        }
        
        self._uuid = str(uuid.uuid4())

        self._token = token
        self._base_url = base_url or _DEFAULT_BASE_URL
        self._user_agent = user_agent or _DEFAULT_USER_AGENT.format(self._uuid)
        self._session = session

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, value: str=None):
        self._base_url = value or _DEFAULT_BASE_URL

    @property
    def user_agent(self) -> str:
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value: str=None):
        self._user_agent = value or _DEFAULT_USER_AGENT.format(self._uuid)

    async def _request(self, *, method, json, headers, session):
        async with session.request(method, self._base_url, json=json, headers=headers) as response:
            if response.status not in range(200, 300):
                try:
                    # even when giving a status-code outside of the
                    # [200, 300) range gql can still give us json data
                    # with relevant metadata
                    data = await response.json()
                    message = data["message"]
                except (aiohttp.client_exceptions.ContentTypeError, KeyError) as e:
                    data = None
                    message = "response failed with status-code {0}".format(response.status)

                try:
                    # handled HTTP status-code
                    exception = self._exception_map[response.status]
                except (KeyError) as e:
                    # arbitrary HTTP status-code
                    exception = errors.HTTPException

                raise exception(message, response=response, data=data)

            if method.upper() == "GET":
                # we should only get here if the request came from
                # HTTPClient.fetch_scopes
                return response

            # this should, theoretically, never error since gql only
            # responds with json data unless it raises a HTTP
            # status-code outside of the [200, 300) range
            data = await response.json()

            if "errors" in data.keys():
                message = data["errors"][0]["message"]
                
                try:
                    # "we only return the type key for errors returned
                    # from the resolvers during execution, the
                    # validation stage doesn't return this type key as
                    # it's essentially validating the payload, by which
                    # it's checking the syntax, and for parse errors,
                    # then checking that the fields, connections and
                    # parameters are valid"
                    type = data["errors"][0]["type"]
                    
                    # handled GitHub status-message
                    exception = self._exception_map[type]
                except (KeyError) as e:
                    # arbitrary GitHub status-message
                    exception = errors.GitHubError

                raise exception(message, response=response, data=data)

            return data

    async def request(self, *, json: dict, headers: dict=None, session: aiohttp.ClientSession=None) -> dict:
        """
        Performs a request to the GitHub API.

        Parameters
        ----------
        json: :class:`dict`
            The JSON object to be posted to the API. This object must
            contain a ``"query"`` key and can optionally contain a
            ``"variables"`` key.
        headers: Optional[:class:`dict`]
            The headers to be passed to the API.

            .. warning::

                You cannot update the user-agent via this method and
                must use the :attr:`~github.GitHub.user_agent` property
                instead.
        session: Optional[:class:`aiohttp.ClientSession`]
            The session to request the API with.

        Raises
        ------
        ~github.errors.Forbidden
            A ``"FORBIDDEN"`` status-message was returned.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            A ``"NOT_FOUND"`` status-message was returned.
        ~github.errors.Unauthorized
            A ``401`` status-code was returned.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.

        Returns
        -------
        :class:`dict`
            The data returned by the API.

            .. note::
                This data only includes that within the ``"data"`` object.
        """

        headers = headers or dict()
        headers.update({"Authorization": "bearer {0}".format(self._token)})
        headers.update({"User-Agent": self._user_agent})
        
        session = session or self._session
        async with context.SessionContext(session) as session:
            data = await self._request(method="POST", json=json, headers=headers, session=session)

        return data["data"]

    # queries

    async def _fetch_collection(self, *path, query, **kwargs):
        nodes = list()

        cursor = None
        has_next_page = True

        while has_next_page:
            json = {
                "query": query,
                "variables": kwargs.update(cursor=cursor) or kwargs,
            }

            data = await self.request(json=json)
            data = functools.reduce(operator.getitem, path, data)

            nodes.extend(data["nodes"])

            cursor = data["pageInfo"]["endCursor"]
            has_next_page = data["pageInfo"]["hasNextPage"]

        return nodes

    async def _fetch_field(self, *path, query, **kwargs):
        json = {
            "query": query,
            "variables": kwargs,
        }

        data = await self.request(json=json)
        return functools.reduce(operator.getitem, path, data)

    async def fetch_actor_avatar_url(self, actor_id, size):
        return await self._fetch_field("node", "avatarUrl",
                                       query=query.FETCH_ACTOR_AVATAR_URL,
                                       actor_id=actor_id, size=size)

    async def fetch_assignable_assignees(self, assignable_id):
        raise NotImplementedError

    async def fetch_commentable_comments(self, commentable_id):
        raise NotImplementedError

    async def fetch_labelable_labels(self, labelable_id):
        return await self._fetch_collection("node", "labels",
                                            query=query.FETCH_LABELABLE_LABELS,
                                            labelable_id=labelable_id)

    async def fetch_profileowner_email(self, profileowner_id):
        return await self._fetch_field("node", "email",
                                       query=query.FETCH_PROFILEOWNER_EMAIL,
                                       profileowner_id=profileowner_id)

    async def fetch_projectowner_project(self, projectowner_id, project_number):
        return await self._fetch_field("node", "project",
                                       query=query.FETCH_PROJECTOWNER_PROJECT,
                                       projectowner_id=projectowner_id, project_number=project_number)

    async def fetch_projectowner_projects(self, projectowner_id):
        return await self._fetch_collection("node", "projects",
                                            query=query.FETCH_PROJECTOWNER_PROJECTS,
                                            projectowner_id=projectowner_id)

    async def fetch_repositorynode_repository(self, repositorynode_id):
        return await self._fetch_field("node", "repository",
                                       query=query.FETCH_REPOSITORYNODE_REPOSITORY,
                                       repositorynode_id=repositorynode_id)

    async def fetch_sponsorable_sponsor_listing(self, sponsorable_id):
        return await self._fetch_field("node", "sponsorsListing",
                                       query=query.FETCH_SPONSORABLE_SPONSOR_LISTING,
                                       sponsorable_id=sponsorable_id)

    async def fetch_all_codes_of_conduct(self):
        return await self._fetch_field("codesOfConduct",
                                       query=query.FETCH_ALL_CODES_OF_CONDUCT)

    async def fetch_all_licenses(self):
        return await self._fetch_field("licenses",
                                       query=query.FETCH_ALL_LICENSES)

    async def fetch_authenticated_user(self):
        return await self._fetch_field("viewer",
                                       query=query.FETCH_AUTHENTICATED_USER)

    async def fetch_code_of_conduct(self, key):
        return await self._fetch_field("codeOfConduct",
                                       query=query.FETCH_CODE_OF_CONDUCT, key=key)

    async def fetch_issue_participants(self, issue_id):
        raise NotImplementedError

    async def fetch_label_issues(self, label_id):
        raise NotImplementedError

    async def fetch_label_pull_requests(self, label_id):
        raise NotImplementedError

    async def fetch_license(self, key):
        return await self._fetch_field("license",
                                       query=query.FETCH_LICENSE, key=key)

    async def fetch_metadata(self):
        return await self._fetch_field("meta", query=query.FETCH_METADATA)

    async def fetch_node(self, id):
        return await self._fetch_field("node", query=query.FETCH_NODE, id=id)

    async def fetch_nodes(self, ids):
        return await self._fetch_field("nodes", query=query.FETCH_NODES, ids=ids)

    async def fetch_organization(self, login):
        return await self._fetch_field("organization",
                                       query=query.FETCH_ORGANIZATION,
                                       login=login)

    async def fetch_project_columns(self, project_id):
        return await self._fetch_collection("node", "columns",
                                            query=query.FETCH_PROJECT_COLUMNS,
                                            project_id=project_id)

    async def fetch_projectcolumn_cards(self, projectcolumn_id):
        return await self._fetch_collection("node", "cards",
                                            query=query.FETCH_PROJECTCOLUMN_CARDS,
                                            projectcolumn_id=projectcolumn_id)

    async def fetch_pull_request_participants(self, pull_request_id):
        raise NotImplementedError
    
    async def fetch_rate_limit(self):
        return await self._fetch_field("rateLimit",
                                       query=query.FETCH_RATE_LIMIT)

    async def fetch_repository(self, owner, name):
        return await self._fetch_field("repository",
                                       query=query.FETCH_REPOSITORY,
                                       owner=owner, name=name)

    async def fetch_repository_assignable_users(self, repository_id):
        return await self._fetch_collection("node", "assignableUsers",
                                            query=query.FETCH_REPOSITORY_ASSIGNABLE_USERS,
                                            repository_id=repository_id)

    async def fetch_repository_collaborators(self, repository_id):
        return await self._fetch_collection("node", "collaborators",
                                            query=query.FETCH_REPOSITORY_COLLABORATORS,
                                            repository_id=repository_id)

    async def fetch_repository_issue(self, repository_id, issue_number):
        return await self._fetch_field("node", "issue",
                                       query=query.FETCH_REPOSITORY_ISSUE,
                                       repository_id=repository_id, issue_number=issue_number)

    async def fetch_repository_issues(self, repository_id):
        return await self._fetch_collection("node", "issues",
                                            query=query.FETCH_REPOSITORY_ISSUES,
                                            repository_id=repository_id)

    async def fetch_repository_parent(self, repository_id):
        try:
            parent = await self._fetch_field("node", "parent",
                                             query=query.FETCH_REPOSITORY_PARENT,
                                             repository_id=repository_id)
        except (KeyError) as e:
            parent = None

        return parent

    async def fetch_repository_template(self, repository_id):
        try:
            template = await self._fetch_field("node", "template",
                                               query=query.FETCH_REPOSITORY_TEMPLATE,
                                               repository_id=repository_id)
        except (KeyError) as e:
            template = None

        return template

    async def fetch_scopes(self):
        headers = dict()
        headers.update({"Authorization": "bearer {0}".format(self._token)})
        headers.update({"User-Agent": self._user_agent})

        session = self._session
        async with context.SessionContext(session) as session:
            response = await self._request(method="GET", json=None, headers=headers, session=session)

        scopes = response.headers.get("X-OAuth-Scopes")
        return [s for s in scopes.split(", ") if s]

    async def fetch_sponsorlisting_tiers(self, sponsorlisting_id):
        return await self._fetch_collection("node", "tiers",
                                            query=query.FETCH_SPONSORLISTING_TIERS,
                                            sponsorlisting_id=sponsorlisting_id)

    async def fetch_sponsortier_sponsorships(self, sponsortier_id):
        return await self._fetch_collection("node", "adminInfo", "sponsorships",
                                            query=query.FETCH_SPONSORTIER_SPONSORSHIPS,
                                            sponsortier_id=sponsortier_id)

    async def fetch_topic(self, name):
        return await self._fetch_field("topic",
                                       query=query.FETCH_TOPIC,
                                       name=name)

    async def fetch_topic_related_topics(self, topic_id):
        return await self._fetch_field("node", "relatedTopics",
                                       query=query.FETCH_TOPIC_RELATED_TOPICS,
                                       topic_id=topic_id)

    async def fetch_user(self, login):
        return await self._fetch_field("user",
                                       query=query.FETCH_USER,
                                       login=login)

    async def fetch_user_commit_comments(self, user_id):
        return await self._fetch_collection("node", "commitComments",
                                            query=query.FETCH_USER_COMMIT_COMMENTS,
                                            user_id=user_id)

    async def fetch_user_followers(self, user_id):
        return await self._fetch_collection("node", "followers",
                                            query=query.FETCH_USER_FOLLOWERS,
                                            user_id=user_id)

    async def fetch_user_following(self, user_id):
        return await self._fetch_collection("node", "following",
                                            query=query.FETCH_USER_FOLLOWING,
                                            user_id=user_id)

    # mutations

    async def _mutate(self, *path, query, **kwargs):
        json = {
            "query": query,
            "variables": {
                "input": kwargs.update({"clientMutationId": self._uuid}) or kwargs,
            },
        }

        data = await self.request(json=json)
        return functools.reduce(operator.getitem, path, data)

    async def mutate_assignable_add_assignees(self, assignable_id, assignee_ids):
        await self._mutate(query=query.MUTATE_ASSIGNABLE_ADD_ASSIGNEES,
                           assignableId=assignable_id, assigneeIds=assignee_ids)

    async def mutate_assignable_remove_assignees(self, assignable_id, assignee_ids):
        await self._mutate(query=query.MUTATE_ASSIGNABLE_REMOVE_ASSIGNEES,
                           assignableId=assignable_id, assigneeIds=assignee_ids)

    async def mutate_commentable_add_comment(self, commentable_id, body):
        raise NotImplementedError

    async def mutate_issue_close(self, issue_id):
        await self._mutate(query=query.MUTATE_ISSUE_CLOSE,
                           issueId=issue_id)

    async def mutate_issue_reopen(self, issue_id):
        await self._mutate(query=query.MUTATE_ISSUE_REOPEN,
                           issueId=issue_id)

    async def mutate_labelable_add_labels(self, labelable_id, label_ids):
        await self._mutate(query=query.MUTATE_LABELABLE_ADD_LABELS,
                           labelableId=labelable_id, labelIds=label_ids)

    async def mutate_labelable_clear_labels(self, labelable_id):
        await self._mutate(query=query.MUTATE_LABELABLE_CLEAR_LABELS,
                           labelableId=labelable_id)

    async def mutate_labelable_remove_labels(self, labelable_id, label_ids):
        await self._mutate(query=query.MUTATE_LABELABLE_REMOVE_LABELS,
                           labelableId=labelable_id, labelIds=label_ids)

    async def mutate_lockable_lock(self, lockable_id, reason):
        await self._mutate(query=query.MUTATE_LOCKABLE_LOCK,
                           lockableId=lockable_id, lockReason=reason)

    async def mutate_lockable_unlock(self, lockable_id):
        await self._mutate(query=query.MUTATE_LOCKABLE_UNLOCK,
                           lockableId=lockable_id)

    async def mutate_project_create_column(self, project_id, name):
        return await self._mutate("addProjectColumn", "columnEdge", "node",
                                  query=query.MUTATE_PROJECT_CREATE_COLUMN,
                                  name=name, projectId=project_id)

    async def mutate_projectcard_move_to(self, projectcard_id, projectcolumn_id, projectcard_after_id):
        return await self._mutate("moveProjectCard", "cardEdge", "node",
                                  query=query.MUTATE_PROJECTCARD_MOVE_TO,
                                  afterCardId=projectcard_after_id, cardId=projectcard_id, columnId=projectcolumn_id)

    async def mutate_projectcolumn_create_card(self, projectcolumn_id, body, content):
        return await self._mutate("addProjectCard", "cardEdge", "node",
                                  query=query.MUTATE_PROJECTCOLUMN_CREATE_CARD,
                                  contentId=content, note=body, projectColumnId=projectcolumn_id)

    async def mutate_projectcolumn_move_to(self, projectcolumn_id, projectcolumn_after_id):
        return await self._mutate("moveProjectColumn", "columnEdge", "node",
                                  query=query.MUTATE_PROJECTCOLUMN_MOVE_TO,
                                  afterColumnId=projectcolumn_after_id, columnId=projectcolumn_id)

    async def mutate_projectowner_create_project(self, projectowner_id, name, body, template):
        return await self._mutate("createProject", "project",
                                  query=query.MUTATE_PROJECTOWNER_CREATE_PROJECT,
                                  body=body, name=name, ownerId=projectowner_id, template=template)

    async def mutate_pullrequest_close(self, pullrequest_id):
        await self._mutate(query=query.MUTATE_PULLREQUEST_CLOSE,
                           pullRequestId=pullrequest_id)

    async def mutate_pullrequest_reopen(self, pullrequest_id):
        await self._mutate(query=query.MUTATE_PULLREQUEST_REOPEN,
                           pullRequestId=pullrequest_id)

    async def mutate_subscribable_update_subscription(self, subscribable_id, state):
        raise NotImplementedError

    async def mutate_user_update_status(self, message, emoji, limited_availability, expires_at, organization_id):
        return await self._mutate("changeUserStatus", "status",
                                  query=query.MUTATE_USER_UPDATE_STATUS,
                                  emoji=emoji, expiresAt=expires_at, limitedAvailability=limited_availability,
                                  message=message, organizationId=organization_id)
