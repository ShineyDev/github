from typing import Optional, Union

from github.enums import LockReason
from github.enums import RepositoryLockReason


class Lockable():
    @property
    def is_locked(self) -> bool: ...
    @property
    def lock_reason(self) -> Optional[Union[LockReason, RepositoryLockReason]]: ...

    async def lock(self, *, reason: LockReason=...) -> None: ...
    async def unlock(self) -> None: ...
