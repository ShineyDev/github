"""
/request.py

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
import yarl

from .utils import (
    context,
    errors,
)


class Requester():
    def __init__(self, *, token: str, username: str, password: str,
                 base_url: str, status_url: str, timeout: int, client_id: str,
                 client_secret: str, user_agent: str, preview: bool):

        self._token = token
        self._username = username
        self._password = password

        self._base_url = base_url.rstrip("/")
        self._status_url = status_url
        self._timeout = timeout
        self._client_id = client_id
        self._client_secret = client_secret
        self._user_agent = user_agent
        self._preview = preview

    @property
    def base_url(self) -> str:
        return self._base_url

    @base_url.setter
    def base_url(self, value: str):
        self._base_url = value

    @property
    def status_url(self) -> str:
        return self._status_url

    @status_url.setter
    def status_url(self, value: str):
        self._status_url = value

    @property
    def timeout(self) -> int:
        return self._timeout

    @timeout.setter
    def timeout(self, value: int):
        self._timeout = value

    @property
    def client_id(self) -> str:
        return self._client_id

    @client_id.setter
    def client_id(self, value: str):
        self._client_id = value

    @property
    def client_secret(self) -> str:
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value: str):
        self._client_secret = value

    @property
    def user_agent(self) -> str:
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value: str):
        self._user_agent = value

    @property
    def preview(self) -> bool:
        return self._preview

    @preview.setter
    def preview(self, value: bool):
        self._preview = value

    def _get_authorization(self):
        if (self._token):
            return "token {0}".format(self._token)
        elif (self._username and self._password):
            return "".format(self._username, self._password)

    async def request(self, method: str, url: str, *, json: dict=None, headers: dict=None, session: aiohttp.ClientSession=aiohttp.ClientSession):
        headers_ = {"User-Agent": self._user_agent}

        authorization = self._get_authorization()
        if (authorization):
            headers_.update({"Authorization": authorization})

        if (headers):
            headers_.update(headers)

        url = yarl.URL(self._base_url) / url.lstrip("/")

        async with context.SessionContext(session) as session:
            return await self._actual_request(method, url, json=json, headers=headers_, session=session)

    async def _actual_request(self, method: str, url: str, *, json: dict, headers: dict, session: aiohttp.ClientSession):
        async with session.request(method, url, json=json, headers=headers) as response:
            if (response.status not in range(200, 300)):
                try:
                    json = await response.json()
                    raise errors.GitHubError("{0}: {1}".format(response.status, json["message"]))
                except (aiohttp.client_exceptions.ContentTypeError) as e:
                    raise errors.GitHubError("{0}: {1}".format(response.status, await response.text()))

            return await response.json()