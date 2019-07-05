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
from github.objects import ratelimit
from github.objects import user


class GitHub():
    def __init__(self, token: str=None, *, base_url: str=None, user_agent: str=None):
        self.http = http.HTTPClient(token, base_url=base_url, user_agent=user_agent)

    @property
    def base_url(self) -> str:
        """
        Get or set the base url used by the wrapper.

        This can be changed to allow support for GitHub Enterprise.
        """

        return self.http.base_url

    @base_url.setter
    def base_url(self, value: str=None):
        self.http.base_url = value

    @property
    def user_agent(self) -> str:
        """
        Get or set the user-agent sent by the wrapper.

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
        return user.AuthenticatedUser.from_data(self.http, data)

    async def fetch_rate_limit(self):
        """

        """

        data = await self.http.fetch_rate_limit()
        return ratelimit.RateLimit.from_data(data)

    async def fetch_user(self, login: str):
        """

        """

        data = await self.http.fetch_user(login)
        return user.User.from_data(self.http, data)
