from typing import List

from github.enums import CannotUpdateReason


class Updatable():
    @property
    def viewer_can_update(self) -> bool: ...
    @property
    def viewer_cannot_update_reasons(self) -> List[CannotUpdateReason]: ...
