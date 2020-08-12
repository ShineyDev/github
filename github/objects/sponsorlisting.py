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

from github import utils
from github.iterator import CollectionIterator
from github.abc import Node
from github.abc import Type
from .sponsortier import SponsorTier


class SponsorListing(Node, Type):
    """
    Represents a GitHub Sponsors listing.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    """

    # https://docs.github.com/en/graphql/reference/objects#sponsorslisting

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @property
    def created_at(self):
        """
        The date and time the sponsor listing was created.

        :type: :class:`~datetime.datetime`
        """

        return utils.iso_to_datetime(self.data["createdAt"])

    @property
    def long_description(self):
        """
        The long description of the sponsor listing.

        :type: :class:`str`
        """

        return self.data["fullDescription"]

    @property
    def long_description_html(self):
        """
        The long description of the sponsor listing as HTML.

        :type: :class:`str`
        """

        return self.data["fullDescriptionHTML"]

    @property
    def name(self):
        """
        The name of the sponsor listing.

        :type: :class:`str`
        """

        return self.data["name"]

    @property
    def short_description(self):
        """
        The short description of the sponsor listing.

        :type: :class:`str`
        """

        return self.data["shortDescription"]

    @property
    def slug(self):
        """
        The slug of the sponsor listing.

        :type: :class:`str`
        """

        return self.data["slug"]

    def fetch_tiers(self, **kwargs):
        """
        |aiter|

        Fetches tiers for the sponsor listing.

        Returns
        -------
        :class:`~github.iterator.CollectionIterator`
            An iterator of :class:`~github.SponsorTier`.
        """

        def map_func(data):
            return SponsorTier.from_data(data, self.http)

        return CollectionIterator(self.http.fetch_sponsorlisting_tiers,
                                  self.id, map_func=map_func, **kwargs)
