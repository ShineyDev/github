from github.abc import Comment
from github.abc import Deletable
from github.abc import Node
from github.abc import Reactable
from github.abc import RepositoryNode
from github.abc import Type
from github.abc import Updatable


class CommitComment(Comment, Deletable, Node, Reactable, RepositoryNode, Type, Updatable):
    ...
