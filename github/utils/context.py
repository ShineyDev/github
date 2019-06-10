"""
/utils/context.py

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

from . import (
    errors,
)


class SessionContext():
    def __init__(self, session):
        self.session = session
        self._callable = True if callable(session) else False

    async def __aenter__(self):
        if (self._callable):
            self.session = self.session()

        return self.session

    async def __aexit__(self, exc_type, exc_value, traceback):
        if (self._callable):
            await self.session.close()

        if (exc_value is not None):
            raise errors.GitHubError(str(exc_value)) from exc_value