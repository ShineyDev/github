"""
/github/objects/sponsorlisting.py

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
from .sponsortier import SponsorTier


class SponsorListing(Node, Type):
    """
    Represents a GitHub Sponsors listing.

    https://developer.github.com/v4/object/sponsorslisting/

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
        The date and time the sponsor listing was created.
        """

        return utils.iso_to_datetime(self.data["createdAt"])
    
    @property
    def long_description(self) -> str:
        """
        The long description of the sponsor listing.
        """

        return self.data["fullDescription"]
    
    @property
    def long_description_html(self) -> str:
        """
        The long description of the sponsor listing as HTML.
        """

        return self.data["fullDescriptionHTML"]
    
    @property
    def name(self) -> str:
        """
        The name of the sponsor listing.
        """

        return self.data["name"]
    
    @property
    def short_description(self) -> str:
        """
        The short description of the sponsor listing.
        """

        return self.data["shortDescription"]
    
    @property
    def slug(self) -> str:
        """
        The slug of the sponsor listing.
        """

        return self.data["slug"]

    async def fetch_tiers(self) -> typing.List[SponsorTier]:
        """
        |coro|

        Fetches a list of tiers for the sponsor listing.

        Raises
        ------
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The sponsor listing does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.

        Returns
        -------
        List[:class:`~github.objects.SponsorTier`]
            The list of tiers.
        """

        data = await self.http.fetch_sponsorlisting_tiers(self.id)
        return SponsorTier.from_data(data, self.http)
