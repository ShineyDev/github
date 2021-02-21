"""
/github/abc/sponsorable.py

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

class Sponsorable():
    """
    Represents an entity that can be sponsored.
    """

    __slots__ = ()

    @property
    def has_sponsorship_listing(self):
        """
        Whether the entity has a sponsorship listing.

        :type: :class:`bool`
        """

        return self.data["hasSponsorsListing"]

    @property
    def is_sponsoring_viewer(self):
        """
        Whether the entity is sponsoring the authenticated user.

        :type: :class:`bool`
        """

        return self.data["isSponsoringViewer"]

    @property
    def viewer_can_sponsor(self):
        """
        Whether the authenticated user can sponsor the entity.

        :type: :class:`bool`
        """

        return self.data["viewerCanSponsor"]

    @property
    def viewer_is_sponsoring(self):
        """
        Whether the authenticated user is sponsoring the entity.

        :type: :class:`bool`
        """

        return self.data["viewerIsSponsoring"]

    async def fetch_sponsorship_listing(self):
        """
        |coro|

        Fetches the sponsorable's sponsorship listing.

        Returns
        -------
        Optional[:class:`~github.objects.SponsorshipListing`]
            The sponsorable's sponsorship listing.
        """

        from github.objects import SponsorshipListing

        data = await self.http.fetch_sponsorable_sponsorship_listing(self.id)
        return SponsorshipListing.from_data(data, self.http)
