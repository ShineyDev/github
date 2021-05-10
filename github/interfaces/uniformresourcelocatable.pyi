from typing import Optional


class UniformResourceLocatable:
    @property
    def resource_path(self) -> str: ...
    @property
    def url(self) -> str: ...
