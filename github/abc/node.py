"""
/github/abc/node.py

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

class Node():
    """
    Represents an object with an ID.

    https://developer.github.com/v4/interface/node/

    Implemented by:
    
    * :class:`~github.AuthenticatedUser`
    * :class:`~github.Bot`
    * :class:`~github.CodeOfConduct`
    * :class:`~github.CommitComment`
    * :class:`~github.Issue`
    * :class:`~github.Label`
    * :class:`~github.Language`
    * :class:`~github.License`
    * :class:`~github.Mannequin`
    * :class:`~github.Organization`
    * :class:`~github.PullRequest`
    * :class:`~github.Repository`
    * :class:`~github.Topic`
    * :class:`~github.User`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __eq__(self, other) -> bool:
        if type(self) != type(other):
            if not issubclass(type(self), type(other)):
                return False

        if self.id != other.id:
            return False

        return True

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} id='{0.id}'>".format(self)

    @classmethod
    def from_data(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            nodes = list()

            for (node) in data:
                nodes.append(cls(node))

            return nodes
        
    @property
    def id(self) -> str:
        """
        The node's ID.
        """

        return self.data["id"]
