from github.enums import MinimizeReason


class Minimizable():
    @property
    def is_minimized(self) -> bool: ...
    @property
    def minimize_reason(self) -> MinimizeReason: ...
    @property
    def viewer_can_minimize(self) -> bool: ...
