from .type import Type


class Node(Type):
    @property
    def id(self) -> str: ...
