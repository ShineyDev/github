from typing import Optional

from datetime import datetime

from github.abc import Actor
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class Bot(Actor, Node, Type, UniformResourceLocatable):
    @property
    def created_at(self) -> datetime: ...
    @property
    def database_id(self) -> int: ...
    @property
    def updated_at(self) -> Optional[datetime]: ...
