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

from github.iterator import CollectionIterator


class ProfileOwner():
    """
    Represents the owner of a GitHub profile.
    """

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
    def has_pinned_items(self):
        """
        Whether the profile owner has any items pinned to their profile
        manually.

        :type: :class:`bool`
        """

        return self.data["itemShowcase"]["hasPinnedItems"]

    @property
    def has_showcase_items(self):
        """
        Whether the profile owner has any items pinned to their profile
        manually or due to popularity.

        :type: :class:`~bool`
        """

        return self.data["itemShowcase"]["items"]["totalCount"] > 0

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
    def pinned_items_remaining_count(self):
        """
        The number of additional items the profile owner can pin to
        their profile.

        :type: :class:`int`
        """

        return self.data["pinnedItemsRemaining"]

    @property
    def twitter_username(self):
        """
        The profile owner's twitter username.

        :type: Optional[:class:`str`]
        """

        return self.data["twitterUsername"]

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

        Fetches the profile owner's e-mail.

        Returns
        -------
        Optional[:class:`str`]
            The profile owner's e-mail.
        """

        return await self.http.fetch_profileowner_email(self.id)

    def fetch_pinnable_items(self, *, types=None, **kwargs):
        """
        |aiter|

        Fetches the profile owner's pinnable items.

        Parameters
        ----------
        types: List[:class:`~github.enums.PinnableItemType`]
            The pinnable item types to filter to.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of Union[:class:`~github.Gist`, \
                                 :class:`~github.Repository`]
        """

        types = types and [t.value for t in types]

        from github import objects

        def map_func(data):
            return objects._TYPE_MAP[data["__typename"]].from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_profileowner_pinnable_items,
            self.id,
            types,
            map_func=map_func,
            **kwargs
        )

    def fetch_pinned_items(self, *, types=None, **kwargs):
        """
        |aiter|

        Fetches the profile owner's pinned items.

        Parameters
        ----------
        types: List[:class:`~github.enums.PinnableItemType`]
            The pinnable item types to filter to.
        **kwargs
            Additional keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of Union[:class:`~github.Gist`, \
                                 :class:`~github.Repository`]
        """

        types = types and [t.value for t in types]

        from github import objects

        def map_func(data):
            return objects._TYPE_MAP[data["__typename"]].from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_profileowner_pinned_items,
            self.id,
            types,
            map_func=map_func,
            **kwargs
        )

    def fetch_showcase_items(self, **kwargs):
        """
        |aiter|

        Fetches the profile owner's showcase items.

        Parameters
        ----------
        **kwargs
            Keyword arguments are passed to
            :class:`~github.iterator.CollectionIterator`.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of Union[:class:`~github.Gist`, \
                                 :class:`~github.Repository`]
        """

        from github import objects

        def map_func(data):
            return objects._TYPE_MAP[data["__typename"]].from_data(data, self.http)

        return CollectionIterator(
            self.http.fetch_profileowner_showcase_items,
            self.id,
            map_func=map_func,
            **kwargs
        )
