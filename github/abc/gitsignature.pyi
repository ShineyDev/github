from typing import Optional

from github.enums import GitSignatureState
from github.objects import User


class GitSignature():
    @property
    def is_github(self) -> bool: ...
    @property
    def payload(self) -> str: ...
    @property
    def signature(self) -> str: ...
    @property
    def state(self) -> GitSignatureState: ...

    async def fetch_email(self) -> str: ...
    async def fetch_user(self) -> Optional[User]: ...
