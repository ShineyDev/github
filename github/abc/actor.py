"""
/github/abc/actor.py

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

class Actor():
    """
    Represents an object which can take actions on GitHub.

    https://developer.github.com/v4/interface/actor/

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def avatar_url(self) -> str:
        """
        A url pointing to the actor's public avatar.
        """

        return self.data["avatarUrl"]

    @property
    def identicon_url(self) -> str:
        """
        A url pointing to the actor's identicon.
        """

        return "https://identicons.github.com/{0}.png".format(self.data["login"])

    @property
    def login(self) -> str:
        """
        The actor's username.
        """

        return self.data["login"]

    async def fetch_avatar_url(self, *, size: int=None) -> str:
        """
        |coro|

        Fetches a url pointing to the actor's avatar.

        Parameters
        ----------
        size: Optional[:class:`int`]
            The size of the avatar.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The actor does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        :class:`str`
            The url pointing to the actor's avatar.
        """
        
        avatar_url = await self.http.fetch_actor_avatar_url(self.id, size)
        return avatar_url
