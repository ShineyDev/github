from github.objects import Repository


class RepositoryOwner():
    async def fetch_repository(self, name: str) -> Repository: ...
