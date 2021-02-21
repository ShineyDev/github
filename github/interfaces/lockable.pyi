from typing import Optional

from github.enums import LockReason


class Lockable():
    @property
    def is_locked(self) -> bool: ...
    @property
    def lock_reason(self) -> Optional[LockReason]: ...
