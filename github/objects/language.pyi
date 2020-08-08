from github.abc import Node
from github.abc import Type


class Language(Node, Type):
    @property
    def color(self) -> str: ...
    colour = color
    @property
    def name(self) -> str: ...
