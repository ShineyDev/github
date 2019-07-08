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
    __slots__ = ("_token", "_base_url", "_user_agent")

    def __init__(self, token, *, base_url, user_agent):
        self._token = token
        self._base_url = base_url or DEFAULT_BASE_URL
        self._user_agent = user_agent or DEFAULT_USER_AGENT

    @property
    def base_url(self):
        return self._base_url

    @base_url.setter
    def base_url(self, value):
        self._base_url = value or DEFAULT_BASE_URL

    @property
    def user_agent(self):
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value):
        self._user_agent = value or DEFAULT_USER_AGENT

    async def _request(self, *, json, headers, session):
        async with session.post(self._base_url, json=json, headers=headers) as response:
            try:
                data = await response.json()
            except (aiohttp.client_exceptions.ContentTypeError) as e:
                text = await response.text()
                raise errors.GitHubError("{0}: {1}".format(response.status, text)) from e
            else:
                if "errors" in data.keys():
                    message = data["errors"][0]["message"]
                    raise errors.GitHubError(message)

                return data

    async def request(self, *, json: dict=None, headers: dict=None, session: aiohttp.ClientSession=None):
        """

        """

        headers = headers or dict()
        headers.update({"Authorization": "bearer {0}".format(self._token)})
        headers.update({"User-Agent": self._user_agent})

        async with context.SessionContext(session) as session:
            data = await self._request(json=json, headers=headers, session=session)

        return data.get("data")

    async def fetch_authenticated_user(self):
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
        return data

    async def fetch_code_of_conduct(self, key):
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
        return data

    async def fetch_codes_of_conduct(self):
        query = """
          query codes_of_conduct {
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
        return data

    async def fetch_license(self, key):
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
        return data

    async def fetch_licenses(self):
        query = """
          query licenses {
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
        return data

    async def fetch_metadata(self):
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
        return data

    async def fetch_node(self, id):
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
        return data

    async def fetch_nodes(self, *ids):
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
        return data
    
    async def fetch_rate_limit(self, *, dry):
        if dry is not None:
            query = """
              query rate_limit ($dry: Boolean!) {
                rateLimit (dryRun: $dry) {
                  cost
                  limit
                  remaining
                  resetAt
                }
              }
            """

            variables = {
                "dry": dry,
            }

            json = {
                "query": query,
                "variables": variables,
            }
        else:
            query = """
              query rate_limit {
                rateLimit {
                  cost
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
        return data

    async def fetch_user(self, login):
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
        return data

    async def fetch_user_avatar_url(self, login, size):
        if size is not None:
            query = """
              query user_avatar_url ($login: String!, $size: Int!) {
                user (login: $login) {
                  avatarUrl (size: $size)
                }
              }
            """

            variables = {
                "login": login,
                "size": size,
            }

            json = {
                "query": query,
                "variables": variables,
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
        return data

    async def fetch_user_email(self, login):
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
        return data
