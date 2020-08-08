from typing import List, Union

from github.objects import CommitComment


class Commentable():
    async def fetch_comments(self) -> List[Union[CommitComment]]: ...
    async def add_comment(self, body: str) -> Union[CommitComment]: ...
