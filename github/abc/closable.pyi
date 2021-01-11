from typing import Optional

from datetime import datetime


class Closable():
    @property
    def closed_at(self) -> Optional[datetime]: ...
    @property
    def is_closed(self) -> bool: ...
