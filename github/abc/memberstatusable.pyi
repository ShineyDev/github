from github.iterator import CollectionIterator
from github.enums import UserStatusOrderField
from github.objects import UserStatus


class MemberStatusable():
    def fetch_member_statuses(self, order_by: UserStatusOrderField=..., **kwargs) -> CollectionIterator[UserStatus]: ...
