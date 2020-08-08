from github.objects import Repository


class RepositoryNode():
    async def fetch_repository(self) -> Repository: ...
