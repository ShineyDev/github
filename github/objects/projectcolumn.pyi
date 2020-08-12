from datetime import datetime
from typing import List, Union, overload

from github.iterator import CollectionIterator
from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.enums import ProjectColumnPurpose
from .issue import Issue
from .projectcard import ProjectCard
from .pullrequest import PullRequest


class ProjectColumn(Node, Type, UniformResourceLocatable):
    @property
    def created_at(self) -> datetime: ...
    @property
    def database_id(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def purpose(self) -> ProjectColumnPurpose: ...
    @property
    def updated_at(self) -> datetime: ...

    def fetch_cards(self, **kwargs) -> CollectionIterator: ...

    @overload
    async def create_card(self, *, body: str) -> ProjectCard: ...
    @overload
    async def create_card(self, *, content: Union[Issue, PullRequest]) -> ProjectCard: ...
    async def move_to(self, *, after: ProjectColumn) -> None: ...
