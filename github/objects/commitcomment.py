"""
/github/objects/commitcomment.py

    Copyright (c) 2019-2020 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from github.abc import Comment
from github.abc import Deletable
from github.abc import Node
from github.abc import Reactable
from github.abc import RepositoryNode
from github.abc import Type
from github.abc import Updatable


class CommitComment(Comment, Deletable, Node, Reactable, RepositoryNode, Type, Updatable):
    """
    Represents a comment on a :class:`~github.Commit`.

    https://developer.github.com/v4/object/commitcomment/

    Implements:

    * :class:`~github.abc.Comment`
    * :class:`~github.abc.Deletable`
    * :class:`~github.abc.Node`
    * :class:`~github.abc.Reactable`
    * :class:`~github.abc.RepositoryNode`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.Updatable`
    """

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    @classmethod
    def from_data(cls, data, http):
        if isinstance(data, dict):
            return cls(data, http)
        elif isinstance(data, list):
            return [cls(comment, http) for comment in data]
