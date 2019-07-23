"""
/github/http.py

    Copyright (c) 2019 ShineyDev
    
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

import aiohttp

from github import context
from github import errors


DEFAULT_BASE_URL = "https://api.github.com/graphql"
DEFAULT_USER_AGENT = "ShineyDev/github"


class HTTPClient():
    """
    Represents a GitHub 'connection' or client.

    This class contains the behind-the-scenes code for the
    :class:`~github.github.GitHub` class and should not be created by
    the user.

    This class is only exposed for
    :meth:`~github.http.HTTPClient.request <HTTPClient.request>`.
    """

    __slots__ = ("_token", "_base_url", "_user_agent", "_session", "_exceptions")

    def __init__(self, token: str, *, base_url: str=None, user_agent: str=None, session: aiohttp.ClientSession=None):
        self._token = token
        self._base_url = base_url or DEFAULT_BASE_URL
        self._user_agent = user_agent or DEFAULT_USER_AGENT
        self._session = session

        self._exceptions = {
            401: errors.Forbidden,
        }

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, value: str):
        self._base_url = value or DEFAULT_BASE_URL

    @property
    def user_agent(self) -> str:
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value: str):
        self._user_agent = value or DEFAULT_USER_AGENT

    async def _request(self, *, json: dict, headers: dict, session: aiohttp.ClientSession):
        async with session.post(self._base_url, json=json, headers=headers) as response:
            if response.status not in range(200, 300):
                try:
                    json = await response.json()
                    message = json["message"]
                except (aiohttp.client_exceptions.ContentTypeError, KeyError) as e:
                    message = "response failed with status-code: {0}".format(response.status)

                try:
                    exception = self._exceptions[response.status]
                except (KeyError) as e:
                    exception = errors.HTTPException

                raise exception(message)

            data = await response.json()

            if "errors" in data.keys():
                message = data["errors"][0]["message"]
                raise errors.GitHubError(message)

            return data

    async def request(self, *, json: dict, headers: dict=None, session: aiohttp.ClientSession=None):
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
                must use the :attr:`.user_agent` property instead.
        session: Optional[:class:`aiohttp.ClientSession`]
            The session to request the API with.
        """

        headers = headers or dict()
        headers.update({"Authorization": "bearer {0}".format(self._token)})
        headers.update({"User-Agent": self._user_agent})
        
        session = session or self._session
        async with context.SessionContext(session) as session:
            data = await self._request(json=json, headers=headers, session=session)

        return data["data"]

    async def fetch_authenticated_user(self) -> dict:
        # https://developer.github.com/v4/object/user/

        query = """
          query authenticated_user {
            viewer {
              __typename
              anyPinnableItems
              avatarUrl
              bio
              company
              createdAt
              databaseId
              id
              isBountyHunter
              isCampusExpert
              isDeveloperProgramMember
              isEmployee
              isHireable
              isSiteAdmin
              isViewer
              location
              login
              name
              updatedAt
              url
              websiteUrl
            }
          }
        """

        json = {
            "query": query,
        }

        data = await self.request(json=json)
        return data["viewer"]

    async def fetch_code_of_conduct(self, key: str) -> dict:
        # https://developer.github.com/v4/object/codeofconduct/

        query = """
          query code_of_conduct ($key: String!) {
            codeOfConduct (key: $key) {
              __typename
              body
              id
              key
              name
              url
            }
          }
        """

        variables = {
            "key": key,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["codeOfConduct"]

    async def fetch_codes_of_conduct(self, *keys: str) -> dict:
        # https://developer.github.com/v4/object/codeofconduct/

        raise NotImplementedError("this method hasn't been implemented yet")

    async def fetch_all_codes_of_conduct(self) -> dict:
        # https://developer.github.com/v4/object/codeofconduct/

        query = """
          query all_codes_of_conduct {
            codesOfConduct {
              __typename
              body
              id
              key
              name
              url
            }
          }
        """

        json = {
            "query": query,
        }

        data = await self.request(json=json)
        return data["codesOfConduct"]

    async def fetch_license(self, key: str) -> dict:
        # https://developer.github.com/v4/object/license/

        query = """
          query license ($key: String!) {
            license (key: $key) {
              __typename
              body
              conditions {
                description
                key
                label
              }
              description
              featured
              hidden
              id
              implementation
              key
              limitations {
                description
                key
                label
              }
              name
              nickname
              permissions {
                description
                key
                label
              }
              pseudoLicense
              spdxId
              url
            }
          }
        """

        variables = {
            "key": key,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["license"]

    async def fetch_licenses(self, *keys: str) -> dict:
        # https://developer.github.com/v4/object/license/

        raise NotImplementedError("this method hasn't been implemented yet")

    async def fetch_all_licenses(self) -> dict:
        # https://developer.github.com/v4/object/license/

        query = """
          query all_licenses {
            licenses {
              __typename
              body
              conditions {
                description
                key
                label
              }
              description
              featured
              hidden
              id
              implementation
              key
              limitations {
                description
                key
                label
              }
              name
              nickname
              permissions {
                description
                key
                label
              }
              pseudoLicense
              spdxId
              url
            }
          }
        """

        json = {
            "query": query,
        }

        data = await self.request(json=json)
        return data["licenses"]

    async def fetch_metadata(self) -> dict:
        # https://developer.github.com/v4/object/githubmetadata/

        query = """
          query metadata {
            meta {
              gitHubServicesSha
              gitIpAddresses
              hookIpAddresses
              importerIpAddresses
              isPasswordAuthenticationVerifiable
              pagesIpAddresses
            }
          }
        """

        json = {
            "query": query,
        }

        data = await self.request(json=json)
        return data["meta"]

    async def fetch_node(self, id) -> dict:
        # https://developer.github.com/v4/interface/node/

        query = """
          query node ($id: ID!) {
            node (id: $id) {
              __typename
              id
            }
          }
        """

        variables = {
            "id": id,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["node"]

    async def fetch_nodes(self, *ids: str) -> dict:
        # https://developer.github.com/v4/interface/node/

        query = """
          query nodes ($ids: [ID!]!) {
            nodes (ids: $ids) {
              __typename
              id
            }
          }
        """

        variables = {
            "ids": ids,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["nodes"]
    
    async def fetch_rate_limit(self) -> dict:
        # https://developer.github.com/v4/object/ratelimit/

        query = """
          query rate_limit {
            rateLimit {
              limit
              remaining
              resetAt
            }
          }
        """

        json = {
            "query": query,
        }

        data = await self.request(json=json)
        return data["rateLimit"]

    async def fetch_repository(self, owner: str, name: str) -> dict:
        # https://developer.github.com/v4/object/repository/

        query = """
          query repository ($owner: String!, $name: String!) {
            repository (owner: $owner, name: $name) {
              __typename
              codeOfConduct {
                __typename
                body
                id
                key
                name
                url
              }
              createdAt
              databaseId
              defaultBranchRef {
                name
              }
              description
              diskUsage
              forkCount
              hasIssuesEnabled
              hasWikiEnabled
              id
              isArchived
              isDisabled
              isFork
              isLocked
              isMirror
              isPrivate
              isTemplate
              licenseInfo {
                __typename
                body
                conditions {
                  description
                  key
                  label
                }
                description
                featured
                hidden
                id
                implementation
                key
                limitations {
                  description
                  key
                  label
                }
                name
                nickname
                permissions {
                  description
                  key
                  label
                }
                pseudoLicense
                spdxId
                url
              }
              lockReason
              mergeCommitAllowed
              name
              owner {
                ... on User {
                  __typename
                  anyPinnableItems
                  avatarUrl
                  bio
                  company
                  createdAt
                  databaseId
                  id
                  isBountyHunter
                  isCampusExpert
                  isDeveloperProgramMember
                  isEmployee
                  isHireable
                  isSiteAdmin
                  isViewer
                  location
                  login
                  name
                  updatedAt
                  url
                  websiteUrl
                }
                ... on Organization {
                  __typename
                  id
                }
              }
              parent {
                __typename
                codeOfConduct {
                  __typename
                  body
                  id
                  key
                  name
                  url
                }
                createdAt
                databaseId
                defaultBranchRef {
                  name
                }
                description
                diskUsage
                forkCount
                hasIssuesEnabled
                hasWikiEnabled
                id
                isArchived
                isDisabled
                isFork
                isLocked
                isMirror
                isPrivate
                isTemplate
                licenseInfo {
                  __typename
                  body
                  conditions {
                    description
                    key
                    label
                  }
                  description
                  featured
                  hidden
                  id
                  implementation
                  key
                  limitations {
                    description
                    key
                    label
                  }
                  name
                  nickname
                  permissions {
                    description
                    key
                    label
                  }
                  pseudoLicense
                  spdxId
                  url
                }
                lockReason
                mergeCommitAllowed
                name
                owner {
                  ... on User {
                    __typename
                    anyPinnableItems
                    avatarUrl
                    bio
                    company
                    createdAt
                    databaseId
                    id
                    isBountyHunter
                    isCampusExpert
                    isDeveloperProgramMember
                    isEmployee
                    isHireable
                    isSiteAdmin
                    isViewer
                    location
                    login
                    name
                    updatedAt
                    url
                    websiteUrl
                  }
                  ... on Organization {
                    __typename
                    id
                  }
                }
                primaryLanguage {
                  __typename
                  color
                  id
                  name
                }
                pushedAt
                rebaseMergeAllowed
                squashMergeAllowed
                updatedAt
                url
                viewerCanAdminister
                viewerCanCreateProjects
                viewerCanSubscribe
                viewerCanUpdateTopics
                viewerPermission
                viewerSubscription
              }
              primaryLanguage {
                __typename
                color
                id
                name
              }
              pushedAt
              rebaseMergeAllowed
              squashMergeAllowed
              templateRepository {
                __typename
                codeOfConduct {
                  __typename
                  body
                  id
                  key
                  name
                  url
                }
                createdAt
                databaseId
                defaultBranchRef {
                  name
                }
                description
                diskUsage
                forkCount
                hasIssuesEnabled
                hasWikiEnabled
                id
                isArchived
                isDisabled
                isFork
                isLocked
                isMirror
                isPrivate
                isTemplate
                licenseInfo {
                  __typename
                  body
                  conditions {
                    description
                    key
                    label
                  }
                  description
                  featured
                  hidden
                  id
                  implementation
                  key
                  limitations {
                    description
                    key
                    label
                  }
                  name
                  nickname
                  permissions {
                    description
                    key
                    label
                  }
                  pseudoLicense
                  spdxId
                  url
                }
                lockReason
                mergeCommitAllowed
                name
                owner {
                  ... on User {
                    __typename
                    anyPinnableItems
                    avatarUrl
                    bio
                    company
                    createdAt
                    databaseId
                    id
                    isBountyHunter
                    isCampusExpert
                    isDeveloperProgramMember
                    isEmployee
                    isHireable
                    isSiteAdmin
                    isViewer
                    location
                    login
                    name
                    updatedAt
                    url
                    websiteUrl
                  }
                  ... on Organization {
                    __typename
                    id
                  }
                }
                primaryLanguage {
                  __typename
                  color
                  id
                  name
                }
                pushedAt
                rebaseMergeAllowed
                squashMergeAllowed
                updatedAt
                url
                viewerCanAdminister
                viewerCanCreateProjects
                viewerCanSubscribe
                viewerCanUpdateTopics
                viewerPermission
                viewerSubscription
              }
              updatedAt
              url
              viewerCanAdminister
              viewerCanCreateProjects
              viewerCanSubscribe
              viewerCanUpdateTopics
              viewerPermission
              viewerSubscription
            }
          }
        """

        variables = {
            "owner": owner,
            "name": name,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["repository"]

    async def fetch_repository_assignable_users(self, owner: str, name: str):
        # https://developer.github.com/v4/object/user/

        query = """
          query repository_assignable_users ($owner: String!, $name: String!, $cursor: String!) {
            repository (owner: $owner, name: $name) {
              assignableUsers (first: 10, after: $cursor) {
                nodes {
                  __typename
                  anyPinnableItems
                  avatarUrl
                  bio
                  company
                  createdAt
                  databaseId
                  id
                  isBountyHunter
                  isCampusExpert
                  isDeveloperProgramMember
                  isEmployee
                  isHireable
                  isSiteAdmin
                  isViewer
                  location
                  login
                  name
                  updatedAt
                  url
                  websiteUrl
                }
                pageInfo {
                  endCursor
                  hasNextPage
                }
              }
            }
          }
        """

        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "owner": owner,
                "name": name,
                "cursor": cursor,
            }

            json = {
                "query": query,
                "variables": variables,
            }

            data = await self.request(json=json)
            nodes.extend(data["repository"]["assignableUsers"]["nodes"])

            cursor = data["repository"]["assignableUsers"]["pageInfo"]["endCursor"]
            has_next_page = data["repository"]["assignableUsers"]["pageInfo"]["hasNextPage"]

        return nodes

    async def fetch_repository_collaborators(self, owner: str, name: str):
        # https://developer.github.com/v4/object/user/

        query = """
          query repository_collaborators ($owner: String!, $name: String!, $cursor: String!) {
            repository (owner: $owner, name: $name) {
              collaborators (first: 10, after: $cursor) {
                nodes {
                  __typename
                  anyPinnableItems
                  avatarUrl
                  bio
                  company
                  createdAt
                  databaseId
                  id
                  isBountyHunter
                  isCampusExpert
                  isDeveloperProgramMember
                  isEmployee
                  isHireable
                  isSiteAdmin
                  isViewer
                  location
                  login
                  name
                  updatedAt
                  url
                  websiteUrl
                }
                pageInfo {
                  endCursor
                  hasNextPage
                }
              }
            }
          }
        """

        nodes = list()
        
        cursor = "Y3Vyc29yOnYyOjA="
        has_next_page = True

        while has_next_page:
            variables = {
                "owner": owner,
                "name": name,
                "cursor": cursor,
            }

            json = {
                "query": query,
                "variables": variables,
            }

            data = await self.request(json=json)
            nodes.extend(data["repository"]["collaborators"]["nodes"])

            cursor = data["repository"]["collaborators"]["pageInfo"]["endCursor"]
            has_next_page = data["repository"]["collaborators"]["pageInfo"]["hasNextPage"]

        return nodes

    async def fetch_topic(self, name: str) -> dict:
        # https://developer.github.com/v4/object/topic/

        query = """
          query topic ($name: String!) {
            topic (name: $name) {
              __typename
              id
              name
              relatedTopics (first: 10) {
                __typename
                id
                name
              }
            }
          }
        """

        variables = {
            "name": name,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["topic"]

    async def fetch_topics(self, *names: str) -> dict:
        # https://developer.github.com/v4/object/topic/

        raise NotImplementedError("this method hasn't been implemented yet")

    async def fetch_user(self, login: str) -> dict:
        # https://developer.github.com/v4/object/user/

        query = """
          query user ($login: String!) {
            user (login: $login) {
              __typename
              anyPinnableItems
              avatarUrl
              bio
              company
              createdAt
              databaseId
              id
              isBountyHunter
              isCampusExpert
              isDeveloperProgramMember
              isEmployee
              isHireable
              isSiteAdmin
              isViewer
              location
              login
              name
              updatedAt
              url
              websiteUrl
            }
          }
        """

        variables = {
            "login": login,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["user"]

    async def fetch_users(self, *logins: str) -> dict:
        # https://developer.github.com/v4/object/user/

        raise NotImplementedError("this method hasn't been implemented yet")

    async def fetch_user_avatar_url(self, login: str, size: int=None) -> dict:
        if size is not None:
            query = """
              query user_avatar_url ($login: String!,
                                     $size: Int!) {
                user (login: $login) {
                  avatarUrl (size: $size)
                }
              }
            """

            variables = {
                "login": login,
                "size": size,
            }
        else:
            query = """
              query user_avatar_url ($login: String!) {
                user (login: $login) {
                  avatarUrl
                }
              }
            """

            variables = {
                "login": login,
            }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["user"]["avatarUrl"]

    async def fetch_user_email(self, login: str) -> dict:
        query = """
          query user_email ($login: String!) {
            user (login: $login) {
              email
            }
          }
        """

        variables = {
            "login": login,
        }

        json = {
            "query": query,
            "variables": variables,
        }

        data = await self.request(json=json)
        return data["user"]["email"]
