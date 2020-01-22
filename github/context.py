"""
/github/context.py

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

import aiohttp
import typing

from github import errors


class SessionContext():
    def __init__(self, session: typing.Optional[aiohttp.ClientSession]=None):
        self.session = session
        self._has_session = session is not None

    async def __aenter__(self):
        if not self._has_session:
            self.session = aiohttp.ClientSession()

        return self.session

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        if not self._has_session:
            await self.session.close()

        if exc_value is not None:
            if not issubclass(exc_type, errors.GitHubError):
                raise errors.HTTPException(exc_value) from exc_value
