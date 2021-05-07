from typing import Optional


class UniformResourceLocatable:
    @property
    def resource_path(self) -> Optional[str]: ...
    @property
    def url(self) -> Optional[str]: ...
