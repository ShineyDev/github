"""
/github.py

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

from . import (
    cache,
    license,
    ratelimit,
    request,
)


_DEFAULT_BASE_URL = "https://api.github.com"
_DEFAULT_STATUS_URL = "https://status.github.com"
_DEFAULT_TIMEOUT = 15
_DEFAULT_USER_AGENT = "ShineyDev/github"


class GitHub():
    def __init__(self, token_or_username: str=None, password: str=None,
                 *, base_url: str=None, status_url: str=None,
                 timeout: int=None, client_id: str=None,
                 client_secret: str=None, user_agent: str=None,
                 preview: bool=False):
        if (not password):
            self.token = token_or_username
            self.username = None
            self.password = None
        else:
            self.token = None
            self.username = token_or_username
            self.password = password

        base_url = base_url or _DEFAULT_BASE_URL
        status_url = status_url or _DEFAULT_STATUS_URL
        timeout = timeout or _DEFAULT_TIMEOUT
        user_agent = user_agent or _DEFAULT_USER_AGENT

        self._cache = cache.Cache()

        self._requester = request.Requester(
            token=self.token,
            username=self.username,
            password=self.password,
            base_url=base_url,
            status_url=status_url,
            timeout=timeout,
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
            preview=preview,
        )

    @property
    def base_url(self) -> str:
        return self._requester._base_url

    @base_url.setter
    def base_url(self, value: str):
        self._requester._base_url = value

    @property
    def status_url(self) -> str:
        return self._requester._status_url

    @status_url.setter
    def status_url(self, value: str):
        self._requester._status_url = value

    @property
    def timeout(self) -> int:
        return self._requester._timeout

    @timeout.setter
    def timeout(self, value: int):
        self._requester._timeout = value

    @property
    def client_id(self) -> str:
        return self._requester._client_id

    @client_id.setter
    def client_id(self, value: str):
        self._requester._client_id = value

    @property
    def client_secret(self) -> str:
        return self._requester._client_secret

    @client_secret.setter
    def client_secret(self, value: str):
        self._requester._client_secret = value

    @property
    def user_agent(self) -> str:
        return self._requester._user_agent

    @user_agent.setter
    def user_agent(self, value: str):
        self._requester._user_agent = value

    @property
    def preview(self) -> bool:
        return self._requester._preview

    @preview.setter
    def preview(self, value: bool):
        self._requester._preview = value

    async def fetch_license(self, key: str):
        # https://developer.github.com/v3/licenses/#get-an-individual-license

        method = "GET"
        url = "/licenses/{0}".format(key)

        data = await self._requester.request(method, url)
        return license.License.from_data(data)

    async def fetch_licenses(self):
        # https://developer.github.com/v3/licenses/#list-commonly-used-licenses

        method = "GET"
        url = "/licenses"

        data = await self._requester.request(method, url)
        return license.PartialLicense.from_data(data)

    async def fetch_rate_limit(self):
        # https://developer.github.com/v3/rate_limit/#get-your-current-rate-limit-status

        method = "GET"
        url = "/rate_limit"

        data = await self._requester.request(method, url)
        return ratelimit.RateLimit.from_data(data)
    
    def get_rate_limit(self):
        return self._cache.rate_limit