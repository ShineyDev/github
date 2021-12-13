from datetime import datetime

from github.interfaces import Type


class RateLimit(Type):
    @property
    def limit(self) -> int: ...
    @property
    def remaining(self) -> int: ...
    @property
    def resets_at(self) -> datetime: ...
    @property
    def used(self) -> int: ...
