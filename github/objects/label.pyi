from typing import List, Optional

from datetime import datetime

from github.abc import Node
from github.abc import RepositoryNode
from github.abc import Type
from github.abc import UniformResourceLocatable
from .issue import Issue
from .pullrequest import PullRequest


class Label(Node, RepositoryNode, Type, UniformResourceLocatable):
    @property
    def color(self) -> str: ...
    colour = color
    @property
    def created_at(self) -> datetime: ...
    @property
    def description(self) -> str: ...
    @property
    def is_default(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def updated_at(self) -> Optional[datetime]: ...

    async def fetch_issues(self) -> List[Issue]: ...
    async def fetch_pull_requests(self) -> List[PullRequest]: ...
