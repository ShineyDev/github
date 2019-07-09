"""
/github/github.py

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

from github import http
from github.objects import codeofconduct
from github.objects import license
from github.objects import ratelimit
from github.objects import topic
from github.objects import user
from github.objects.abc import node


class GitHub():
    """

    """

    __slots__ = ("http",)

    def __init__(self, token: str, *, base_url: str=None, user_agent: str=None):
        self.http = http.HTTPClient(token, base_url=base_url, user_agent=user_agent)

    @property
    def base_url(self) -> str:
        """
        The base url used by this wrapper.

        This can be changed to allow support for GitHub Enterprise.
        """

        return self.http.base_url

    @base_url.setter
    def base_url(self, value: str=None):
        self.http.base_url = value

    @property
    def user_agent(self) -> str:
        """
        The user-agent sent by this wrapper.

        This can be changed to allow GitHub to contact you in case of issues.
        """

        return self.http.user_agent

    @user_agent.setter
    def user_agent(self, value: str=None):
        self.http.user_agent = value

    async def fetch_authenticated_user(self):
        """

        """

        data = await self.http.fetch_authenticated_user()
        return user.AuthenticatedUser.from_data(data, self.http)

    async def fetch_code_of_conduct(self, key: str):
        """

        """

        data = await self.http.fetch_code_of_conduct(key)
        return codeofconduct.CodeOfConduct.from_data(data)

    async def fetch_codes_of_conduct(self, *keys: str):
        """

        """

        data = await self.http.fetch_codes_of_conduct(*keys)
        return codeofconduct.CodeOfConduct.from_data(data)

    async def fetch_all_codes_of_conduct(self):
        """

        """

        data = await self.http.fetch_all_codes_of_conduct()
        return codeofconduct.CodeOfConduct.from_data(data)

    async def fetch_license(self, key: str):
        """

        """

        data = await self.http.fetch_license(key)
        return license.License.from_data(data)

    async def fetch_licenses(self, *keys: str):
        """

        """

        data = await self.http.fetch_licenses(*keys)
        return license.License.from_data(data)

    async def fetch_all_licenses(self):
        """

        """

        data = await self.http.fetch_all_licenses()
        return license.License.from_data(data)

    async def fetch_metadata(self):
        """

        """

        data = await self.http.fetch_metadata()
        return metadata.Metadata.from_data(data)

    async def fetch_node(self, id: str):
        """

        """

        data = await self.http.fetch_node(id)
        return node.Node.from_data(data)

    async def fetch_nodes(self, *ids: str):
        """

        """

        data = await self.http.fetch_nodes(*ids)
        return node.Node.from_data(data)

    async def fetch_rate_limit(self, *, dry: bool=None):
        """

        """

        data = await self.http.fetch_rate_limit(dry=dry)
        return ratelimit.RateLimit.from_data(data)

    async def fetch_topic(self, name: str):
        """

        """

        data = await self.http.fetch_topic(name)
        return topic.Topic.from_data(data)

    async def fetch_topics(self, *names: str):
        """

        """

        data = await self.http.fetch_topics(*names)
        return topic.Topic.from_data(data)

    async def fetch_user(self, login: str):
        """

        """

        data = await self.http.fetch_user(login)
        return user.User.from_data(data, self.http)

    async def fetch_users(self, *logins: str):
        """

        """

        data = await self.http.fetch_users(*logins)
        return user.User.from_data(data, self.http)
    