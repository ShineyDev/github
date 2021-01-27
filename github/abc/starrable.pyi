from github.iterator import CollectionIterator
from github.enums import StargazerOrderField
from github.objects import User


class Starrable():
    @property
    def stargazer_count(self) -> int: ...
    @property
    def viewer_has_starred(self) -> bool: ...

    def fetch_stargazers(self, *, order_by: StargazerOrderField=..., **kwargs) -> CollectionIterator[User]: ...
