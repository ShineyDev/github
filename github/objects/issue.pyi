from github.abc import Assignable
from github.abc import Closable
from github.abc import Comment
from github.abc import Commentable
from github.abc import Labelable
from github.abc import Lockable
from github.abc import Node
from github.abc import Participable
from github.abc import Reactable
from github.abc import RepositoryNode
from github.abc import Subscribable
from github.abc import Type
from github.abc import UniformResourceLocatable
from github.abc import Updatable
from github.enums import IssueState


class Issue(Assignable, Closable, Comment, Commentable, Labelable, Lockable, Node, Participable,
            Reactable, RepositoryNode, Subscribable, Type, UniformResourceLocatable, Updatable):
    @property
    def database_id(self) -> int: ...
    @property
    def number(self) -> int: ...
    @property
    def state(self) -> IssueState: ...
    @property
    def title(self) -> str: ...
