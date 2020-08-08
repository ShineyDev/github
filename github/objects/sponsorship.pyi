from datetime import datetime

from github.abc import Node
from github.abc import Type
from github.enums import SponsorshipPrivacy


class Sponsorship(Node, Type):
    @property
    def created_at(self) -> datetime: ...
    @property
    def privacy(self) -> SponsorshipPrivacy: ...
