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

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    # https://developer.github.com/v4/interface/actor/

    __slots__ = ()

    @property
    def avatar_url(self) -> str:
        """
        A url pointing to the actor's avatar.

        :type: :class:`str`
        """

        return self.data["avatarUrl"]

    @property
    def identicon_url(self) -> str:
        """
        A url pointing to the actor's identicon avatar.

        :type: :class:`str`
        """

        return "https://identicons.github.com/{0}.png".format(self.data["login"])

    @property
    def login(self) -> str:
        """
        The actor's username.

        :type: :class:`str`
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

        Returns
        -------
        :class:`str`
            A url.
        """
        
        avatar_url = await self.http.fetch_actor_avatar_url(self.id, size)
        return avatar_url
