from typing import List

from github.objects import User


class Participable():
    async def fetch_participants(self) -> List[User]: ...
