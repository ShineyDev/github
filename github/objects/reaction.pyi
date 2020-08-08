from datetime import datetime

from github.abc import Type
from github.enums import Reaction as enums_Reaction


class Reaction(Type):
    @property
    def content(self) -> enums_Reaction: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def viewer_has_reacted(self) -> bool: ...
