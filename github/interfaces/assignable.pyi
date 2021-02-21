from github.iterator import CollectionIterator
from github.objects import User


class Assignable():
    def fetch_assignees(self, **kwargs) -> CollectionIterator[User]: ...
