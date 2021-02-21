from typing import List

from github.iterator import CollectionIterator
from github.enums import RepositoryAffiliation
from github.enums import RepositoryOrderField
from github.enums import RepositoryPrivacy
from github.objects import Repository


class RepositoryOwner():
    async def fetch_repository(self, name: str) -> Repository: ...

    def fetch_repositories(self, *, is_fork: bool=..., is_locked: bool=..., order_by: RepositoryOrderField=..., owner_affiliations: List[RepositoryAffiliation]=..., privacy: RepositoryPrivacy=..., viewer_affiliations: List[RepositoryAffiliation]=..., **kwargs) -> CollectionIterator[Repository]: ...
