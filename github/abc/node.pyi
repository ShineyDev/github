from github.abc import Type


class Node(Type):
    @property
    def id(self) -> str: ...
