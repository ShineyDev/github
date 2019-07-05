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
    def __init__(self, token=None, *, base_url=None, user_agent=None):
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
                if ("errors" in data.keys()):
                    message = data["errors"][0]["message"]
                    raise errors.GitHubError(message)

                return data

    async def request(self, *, json: dict=None, headers: dict=None, session: aiohttp.ClientSession=None):
        """

        """

        headers = headers or dict()
        headers.update({"Authorization": "Bearer {0}".format(self._token)})
        headers.update({"User-Agent": self._user_agent})

        async with context.SessionContext(session) as session:
            data = await self._request(json=json, headers=headers, session=session)

        return data["data"]

    async def fetch_authenticated_user(self):
        query = """
          query {
            viewer {
              location
              login
              name
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
          query ($login: String!) {
            user (login: $login) {
              location
              login
              name
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