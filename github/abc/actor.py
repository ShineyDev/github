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

    Implemented by:

    * :class:`~github.Organization`
    * :class:`~github.User`
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
        |coro|

        Fetches a url pointing to the actor's avatar.

        Parameters
        ----------
        size: :class:`int`
            The size of the avatar.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`str`
            The url pointing to the actor's avatar.
        """
        
        if self.data["__typename"] == "Bot":
            avatar_url = await self.http.fetch_bot_avatar_url(self.login, size)
        elif self.data["__typename"] == "Mannequin":
            avatar_url = await self.http.fetch_mannequin_avatar_url(self.login, size)
        elif self.data["__typename"] == "Organization":
            avatar_url = await self.http.fetch_organization_avatar_url(self.login, size)
        elif self.data["__typename"] == "User":
            avatar_url = await self.http.fetch_user_avatar_url(self.login, size)

        return avatar_url
