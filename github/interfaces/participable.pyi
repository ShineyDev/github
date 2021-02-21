from github.iterator import CollectionIterator
from github.objects import User


class Participable():
    def fetch_participants(self, **kwargs) -> CollectionIterator[User]: ...
