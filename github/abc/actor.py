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
    Represents a GitHub actor.
    """

    __slots__ = ()

    @property
    def avatar_url(self):
        """
        A URL pointing to the actor's avatar.

        :type: :class:`str`
        """

        return self.data["avatarUrl"]

    @property
    def login(self):
        """
        The actor's login.

        :type: :class:`str`
        """

        return self.data["login"]

    async def fetch_avatar_url(self, *, size=None):
        """
        |coro|

        Fetches a URL pointing to the actor's avatar.

        Parameters
        ----------
        size: :class:`int`
            The uniform size of the image, in pixels.

        Returns
        -------
        :class:`str`
            A URL pointing to the actor's avatar.
        """

        return await self.http.fetch_actor_avatar_url(self.id, size)
