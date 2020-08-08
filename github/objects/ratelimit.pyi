from datetime import datetime

from github.abc import Type


class RateLimit(Type):
    @property
    def limit(self) -> int: ...
    @property
    def remaining(self) -> int: ...
    @property
    def reset_at(self) -> datetime: ...
