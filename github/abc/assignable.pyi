from typing import List

from github.iterator import CollectionIterator
from github.objects import User


class Assignable():
    def fetch_assignees(self, **kwargs) -> CollectionIterator: ...
    async def add_assignees(self, *users: User) -> None: ...
    async def remove_assignees(self, *users: User) -> None: ...
