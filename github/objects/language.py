"""
/github/objects/language.py

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

from github import utils
from github.abc import Node
from github.abc import Type


class Language(Node, Type):
    """
    Represents a programming language found in repositories.

    https://developer.github.com/v4/object/language/

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    """

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} name='{0.name}'>".format(self)

    @classmethod
    def from_data(cls, data):
        if isinstance(data, dict):
            return cls(data)
        elif isinstance(data, list):
            return [cls(language) for language in data]

    @property
    def color(self) -> str:
        """
        The color of the language in the GitHub UI.
        """

        return self.data["color"]

    @property
    def colour(self) -> str:
        """
        An alias for :attr:`~Language.color`.
        """

        return self.color

    @property
    def name(self) -> str:
        """
        The name of the language.
        """

        return self.data["name"]
