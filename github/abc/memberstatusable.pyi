from github.iterator import CollectionIterator
from github.objects import UserStatus


class MemberStatusable():
    def fetch_member_statuses(self, **kwargs) -> CollectionIterator[UserStatus]: ...
