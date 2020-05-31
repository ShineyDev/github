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

import datetime
import typing

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
    def created_at(self) -> datetime.datetime:
        """
        The date and time the sponsor tier was created.
        """

        return utils.iso_to_datetime(self.data["createdAt"])
    
    @property
    def description(self) -> str:
        """
        The description of the sponsor tier.
        """

        return self.data["description"]
    
    @property
    def description_html(self) -> str:
        """
        The description of the sponsor tier in HTML.
        """

        return self.data["descriptionHTML"]
    
    @property
    def name(self) -> str:
        """
        The name of the sponsor tier.
        """

        return self.data["name"]
    
    @property
    def price(self) -> str:
        """
        How much this tier costs per month in dollars.
        """

        return self.data["monthlyPriceInDollars"]
    
    @property
    def updated_at(self) -> datetime.datetime:
        """
        The date and time the sponsor tier was last updated.
        """

        return utils.iso_to_datetime(self.data["updatedAt"])

    async def fetch_sponsorships(self) -> typing.List[Sponsorship]:
        """
        |coro|

        Fetches a list of sponsorships on the sponsor tier.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The sponsor tier does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.objects.Sponsorship`]
            The list of sponsorships.
        """

        data = await self.http.fetch_sponsortier_sponsorships(self.id)
        return Sponsorship.from_data(data, self.http)
