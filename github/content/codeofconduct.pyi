from typing import Optional

from github.interfaces import Node, Type


class CodeOfConduct(Node, Type):
    @property
    def body(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def name(self) -> str: ...

    # patch for UniformResourceLocatable inheritance
    @property
    def resource_path(self) -> Optional[str]: ...
    @property
    def url(self) -> Optional[str]: ...

    async def fetch_body(self) -> str: ...
