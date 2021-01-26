from github.enums import MinimizedReason


class Minimizable():
    @property
    def is_minimized(self) -> bool: ...
    @property
    def minimized_reason(self) -> MinimizedReason: ...
    @property
    def viewer_can_minimize(self) -> bool: ...
