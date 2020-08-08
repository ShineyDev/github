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

class ProfileOwner():
    """
    Represents the owner of a GitHub profile.

    Implemented by:

    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Organization`
    * :class:`~github.User`
    """

    # https://docs.github.com/en/graphql/reference/interfaces#profileowner

    __slots__ = ()

    @property
    def has_pinnable_items(self):
        """
        Whether the profile owner has any items that can be pinned to
        their profile.

        :type: :class:`bool`
        """

        return self.data["anyPinnableItems"]

    @property
    def location(self):
        """
        The profile owner's location.

        :type: Optional[:class:`str`]
        """

        return self.data["location"]

    @property
    def name(self):
        """
        The profile owner's name.

        :type: Optional[:class:`str`]
        """

        return self.data["name"]

    @property
    def pinned_items_remaining(self):
        """
        The number of additional items the profile owner can pin to
        their profile.

        :type: :class:`int`
        """

        return self.data["pinnedItemsRemaining"]

    @property
    def viewer_can_change_pinned_items(self):
        """
        Whether the authenticated user can change the pinned items on
        the profile.

        :type: :class:`bool`
        """

        return self.data["viewerCanChangePinnedItems"]

    @property
    def website(self):
        """
        The profile owner's website.

        :type: Optional[:class:`str`]
        """

        return self.data["websiteUrl"]

    async def fetch_email(self):
        """
        |coro|

        Fetches the profile owner's email.

        Requires the ``user:email`` scope.

        Returns
        -------
        Optional[:class:`str`]
            The email.
        """

        return await self.http.fetch_profileowner_email(self.id)
