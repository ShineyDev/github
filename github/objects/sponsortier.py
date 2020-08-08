"""
/github/objects/sponsortier.py

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

from github import utils
from github.abc import Node
from github.abc import Type
from .sponsorship import Sponsorship


class SponsorTier(Node, Type):
    """
    Represents a GitHub Sponsors tier.

    https://developer.github.com/v4/object/sponsorstier/

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def created_at(self):
        """
        The date and time the sponsor tier was created.

        :type: :class:`~datetime.datetime`
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def description(self):
        """
        The description of the sponsor tier.

        :type: :class:`str`
        """

        return self.data["description"]

    @property
    def description_html(self):
        """
        The description of the sponsor tier in HTML.

        :type: :class:`str`
        """

        return self.data["descriptionHTML"]

    @property
    def name(self):
        """
        The name of the sponsor tier.

        :type: :class:`str`
        """

        return self.data["name"]

    @property
    def price(self):
        """
        How much this tier costs per month in dollars.

        :type: :class:`int`
        """

        return self.data["monthlyPriceInDollars"]

    @property
    def updated_at(self):
        """
        The date and time the sponsor tier was last updated.

        :type: :class:`~datetime.datetime`
        """

        return utils.iso_to_datetime(self.data["updatedAt"])

    async def fetch_sponsorships(self):
        """
        |coro|

        Fetches a list of sponsorships on the sponsor tier.

        Returns
        -------
        List[:class:`~github.objects.Sponsorship`]
            The list of sponsorships.
        """

        data = await self.http.fetch_sponsortier_sponsorships(self.id)
        return Sponsorship.from_data(data, self.http)
