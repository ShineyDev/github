from datetime import datetime
from typing import List

from github.iterator import CollectionIterator
from github.abc import Node
from github.abc import Type
from .sponsorship import Sponsorship


class SponsorTier(Node, Type):
    @property
    def created_at(self) -> datetime: ...
    @property
    def description(self) -> str: ...
    @property
    def description_html(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def price(self) -> int: ...
    @property
    def updated_at(self) -> datetime: ...

    def fetch_sponsorships(self, **kwargs) -> CollectionIterator: ...
