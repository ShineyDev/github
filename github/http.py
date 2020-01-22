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
        
        self._uuid = uuid.uuid4()

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

    # primary queries,
    # these methods are invoked from the github.GitHub class

    async def fetch_all_codes_of_conduct(self):
        json = {
            "query": query.FETCH_ALL_CODES_OF_CONDUCT,
        }

        data = await self.request(json=json)
        return data["codesOfConduct"]

    async def fetch_all_licenses(self):
        json = {
            "query": query.FETCH_ALL_LICENSES,
        }

        data = await self.request(json=json)
        return data["licenses"]

    async def fetch_authenticated_user(self):
        json = {
            "query": query.FETCH_AUTHENTICATED_USER,
        }

        data = await self.request(json=json)
        return data["viewer"]

    async def fetch_code_of_conduct(self, key):
        variables = {
            "key": key,
        }

        json = {
            "query": query.FETCH_CODE_OF_CONDUCT,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["codeOfConduct"]

    async def fetch_license(self, key):
        variables = {
            "key": key,
        }

        json = {
            "query": query.FETCH_LICENSE,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["license"]

    async def fetch_metadata(self):
        json = {
            "query": query.FETCH_METADATA,
        }

        data = await self.request(json=json)
        return data["meta"]

    async def fetch_node(self, id):
        variables = {
            "id": id,
        }

        json = {
            "query": query.FETCH_NODE,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["node"]

    async def fetch_nodes(self, ids):
        variables = {
            "ids": ids,
        }

        json = {
            "query": query.FETCH_NODES,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["nodes"]

    async def fetch_organization(self, login):
        variables = {
            "login": login,
        }

        json = {
            "query": query.FETCH_ORGANIZATION,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["organization"]
    
    async def fetch_rate_limit(self):
        json = {
            "query": query.FETCH_RATE_LIMIT,
        }

        data = await self.request(json=json)
        return data["rateLimit"]

    async def fetch_repository(self, owner, name):
        variables = {
            "owner": owner,
            "name": name,
        }

        json = {
            "query": query.FETCH_REPOSITORY,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["repository"]

    async def fetch_scopes(self):
        headers = dict()
        headers.update({"Authorization": "bearer {0}".format(self._token)})
        headers.update({"User-Agent": self._user_agent})

        session = self._session
        async with context.SessionContext(session) as session:
            response = await self._request(method="GET", json=None, headers=headers, session=session)

        scopes = response.headers.get("X-OAuth-Scopes")
        return [s for s in scopes.split(", ") if s]

    async def fetch_topic(self, name):
        variables = {
            "name": name,
        }

        json = {
            "query": query.FETCH_TOPIC,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["topic"]

    async def fetch_user(self, login):
        variables = {
            "login": login,
        }

        json = {
            "query": query.FETCH_USER,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["user"]

    # secondary queries,
    # these methods are invoked from classes in the github.abc or
    # github.objects namespaces

    async def fetch_actor_avatar_url(self, actor_id, size):
        variables = {
            "actor_id": actor_id,
            "size": size,
        }

        json = {
            "query": query.FETCH_ACTOR_AVATAR_URL,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["node"]["avatarUrl"]

    async def fetch_assignable_assignees(self, assignable_id):
        raise NotImplementedError("this method is not yet implemented")

    async def fetch_commentable_comments(self, commentable_id):
        raise NotImplementedError("this method is not yet implemented")

    async def fetch_issue_participants(self, issue_id):
        raise NotImplementedError("this method is not yet implemented")

    async def fetch_label_issues(self, label_id):
        raise NotImplementedError("this method is not yet implemented")

    async def fetch_label_pull_requests(self, label_id):
        raise NotImplementedError("this method is not yet implemented")

    async def fetch_labelable_labels(self, labelable_id):
        raise NotImplementedError("this method is not yet implemented")

    async def fetch_profileowner_email(self, profileowner_id):
        variables = {
            "profileowner_id": profileowner_id,
        }

        json = {
            "query": query.FETCH_PROFILEOWNER_EMAIL,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["node"]["email"]

    async def fetch_pull_request_participants(self, pull_request_id):
        raise NotImplementedError("this method is not yet implemented")

    async def fetch_repository_assignable_users(self, repository_id):
        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "repository_id": repository_id,
                "cursor": cursor,
            }

            json = {
                "query": query.FETCH_REPOSITORY_ASSIGNABLE_USERS,
                "variables": variables,
            }

            data = await self.request(json=json)
            nodes.extend(data["node"]["assignableUsers"]["nodes"])

            cursor = data["node"]["assignableUsers"]["pageInfo"]["endCursor"]
            has_next_page = data["node"]["assignableUsers"]["pageInfo"]["hasNextPage"]

        return nodes

    async def fetch_repository_collaborators(self, repository_id):
        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "repository_id": repository_id,
                "cursor": cursor,
            }

            json = {
                "query": query.FETCH_REPOSITORY_COLLABORATORS,
                "variables": variables,
            }

            data = await self.request(json=json)
            nodes.extend(data["node"]["collaborators"]["nodes"])

            cursor = data["node"]["collaborators"]["pageInfo"]["endCursor"]
            has_next_page = data["node"]["collaborators"]["pageInfo"]["hasNextPage"]

        return nodes

    async def fetch_user_commit_comments(self, user_id):
        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "user_id": user_id,
                "cursor": cursor,
            }

            json = {
                "query": query.FETCH_USER_COMMIT_COMMENTS,
                "variables": variables,
            }

            data = await self.request(json=json)
            nodes.extend(data["node"]["commitComments"]["nodes"])

            cursor = data["node"]["commitComments"]["pageInfo"]["endCursor"]
            has_next_page = data["node"]["commitComments"]["pageInfo"]["hasNextPage"]

        return nodes

    # mutations

    async def add_assignees(self, assignable_id, assignee_ids):
        raise NotImplementedError("this method is not yet implemented")

    async def add_comment(self, commentable_id, body):
        raise NotImplementedError("this method is not yet implemented")

    async def add_labels(self, labelable_id, label_ids):
        raise NotImplementedError("this method is not yet implemented")

    async def clear_labels(self, labelable_id):
        raise NotImplementedError("this method is not yet implemented")

    async def close_issue(self, issue_id):
        raise NotImplementedError("this method is not yet implemented")

    async def close_pull_request(self, pull_request_id):
        raise NotImplementedError("this method is not yet implemented")

    async def lock(self, lockable_id, reason):
        raise NotImplementedError("this method is not yet implemented")

    async def remove_assignees(self, assignable_id, assignee_ids):
        raise NotImplementedError("this method is not yet implemented")

    async def remove_labels(self, labelable_id, label_ids):
        raise NotImplementedError("this method is not yet implemented")

    async def reopen_issue(self, issue_id):
        raise NotImplementedError("this method is not yet implemented")

    async def reopen_pull_request(self, pull_request_id):
        raise NotImplementedError("this method is not yet implemented")

    async def unlock(self, lockable_id):
        raise NotImplementedError("this method is not yet implemented")

    async def update_subscription(self, id, state):
        raise NotImplementedError("this method is not yet implemented")
