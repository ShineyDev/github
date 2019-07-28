"""
/github/objects/commitcomment.py

    Copyright (c) 2019 ShineyDev
    
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
from github.abc import Updatable


class CommitComment(Comment, Deletable, Node, Reactable, RepositoryNode, Updatable):
    """
    Represents a comment on a :class:`~github.Commit`.

    https://developer.github.com/v4/object/commitcomment/
    """

    ...
