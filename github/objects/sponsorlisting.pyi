from typing import List

from datetime import datetime

from github.iterator import CollectionIterator
from github.abc import Node
from github.abc import Type
from github.objects import SponsorTier


class SponsorListing(Node, Type):
    @property
    def created_at(self) -> datetime: ...
    @property
    def long_description(self) -> str: ...
    @property
    def long_description_html(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def short_description(self) -> str: ...
    @property
    def slug(self) -> str: ...

    def fetch_tiers(self, **kwargs) -> CollectionIterator: ...
