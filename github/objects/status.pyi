from typing import Optional

from datetime import datetime

from github.abc import Node
from github.abc import Type


class Status(Node, Type):
    @property
    def created_at(self) -> datetime: ...
    @property
    def emoji(self) -> Optional[str]: ...
    @property
    def emoji_html(self) -> Optional[str]: ...
    @property
    def expires_at(self) -> Optional[datetime]: ...
    @property
    def is_busy(self) -> bool: ...
    @property
    def message(self) -> Optional[str]: ...
    @property
    def updated_at(self) -> datetime: ...
