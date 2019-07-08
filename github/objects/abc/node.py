"""
/github/objects/abc/node.py

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

class Node():
    """
    Represents an object with an ID.

    https://developer.github.com/v4/interface/node/
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if type(self) != type(other):
            return False

        if self.id != other.id:
            return False

        return True

    def __repr__(self):
        return "<{0} id='{1}'>".format(self.__class__.__name__, self.id)

    @classmethod
    def from_data(cls, data):
        if "node" in data:
            return cls(data["node"])
        else:
            nodes = list()

            for (node) in data["nodes"]:
                nodes.append(cls(node))

            return nodes
        
    @property
    def id(self) -> str:
        """
        ID of the object.
        """

        return self.data.get("id")

    @property
    def type(self) -> str:
        """
        The name of the current object type.
        """

        return self.data.get("__typename")
