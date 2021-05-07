from github.interfaces import Node, Type, UniformResourceLocatable


class CodeOfConduct(Node, Type, UniformResourceLocatable):
    @property
    def body(self) -> str: ...
    @property
    def key(self) -> str: ...
    @property
    def name(self) -> str: ...
