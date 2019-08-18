"""
/github/abc/actor.py

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

class Actor():
    """
    Represents an object which can take actions on GitHub.

    https://developer.github.com/v4/interface/actor/
    """

    __slots__ = ()

    @property
    def avatar_url(self) -> str:
        """
        A url pointing to this actor's public avatar.
        """

        return self.data["avatarUrl"]

    @property
    def login(self) -> str:
        """
        The username for this actor.
        """

        return self.data["login"]

    async def fetch_avatar_url(self, *, size: int=None) -> str:
        """
        Fetches a url pointing to this actor's public avatar.
        """
        
        if self.data["__typename"] == "Bot":
            # TODO: implement github.Bot
            ...
        elif self.data["__typename"] == "Mannequin":
            # TODO: implement github.Mannequin
            ...
        elif self.data["__typename"] == "Organization":
            avatar_url = await self.http.fetch_organization_avatar_url(self.login, size)
        elif self.data["__typename"] == "User":
            avatar_url = await self.http.fetch_user_avatar_url(self.login, size)

        return avatar_url
