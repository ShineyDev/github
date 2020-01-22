"""
/github/abc/profileowner.py

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

import typing


class ProfileOwner():
    """
    Represents the owner of a GitHub profile.

    https://developer.github.com/v4/interface/profileowner/

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    __slots__ = ()

    @property
    def has_pinnable_items(self) -> bool:
        """
        Whether or not the profile owner has any items that can be pinned to the profile.
        """

        return self.data["anyPinnableItems"]

    @property
    def location(self) -> typing.Optional[str]:
        """
        The profile owner's location.
        """

        return self.data["location"]

    @property
    def name(self) -> typing.Optional[str]:
        """
        The profile owner's name.
        """

        return self.data["name"]

    @property
    def pinned_items_remaining(self) -> int:
        """
        The number of items the profile owner can pin to the profile.
        """

        return self.data["pinnedItemsRemaining"]

    @property
    def viewer_can_change_pinned_items(self) -> bool:
        """
        Whether or not the authenticated user can change the pinned items on the profile.
        """

        return self.data["viewerCanCreateProjects"]

    @property
    def website(self) -> typing.Optional[str]:
        """
        The profile owner's website.
        """

        return self.data["websiteUrl"]
    
    async def fetch_email(self) -> typing.Optional[str]:
        """
        |coro|

        Fetches the profile owner's email.

        Requires the ``user:email`` scope.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The profile owner does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        Optional[:class:`str`]
            The profile owner's email.
        """

        email = await self.http.fetch_profileowner_email(self.id)
        return email
