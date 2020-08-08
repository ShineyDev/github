from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class CodeOfConduct(Node, Type, UniformResourceLocatable):
    @property
    def body(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def name(self) -> str: ...
