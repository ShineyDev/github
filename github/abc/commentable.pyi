from typing import List, Union

from github.iterator import CollectionIterator
from github.objects import CommitComment


class Commentable():
    def fetch_comments(self, **kwargs) -> CollectionIterator: ...
    async def add_comment(self, body: str) -> Union[CommitComment]: ...
