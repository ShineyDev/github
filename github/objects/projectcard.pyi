from typing import Optional

from datetime import datetime

from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.enums import ProjectCardState
from github.objects import ProjectColumn


class ProjectCard(Node, Type, UniformResourceLocatable):
    @property
    def body(self) -> Optional[str]: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def database_id(self) -> int: ...
    @property
    def is_archived(self) -> bool: ...
    @property
    def state(self) -> ProjectCardState: ...
    @property
    def updated_at(self) -> datetime: ...

    async def move_to(self, column: ProjectColumn, *, after: ProjectCard=...) -> None: ...
