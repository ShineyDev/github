"""
/github/objects/codeofconduct.py

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

from github.abc import Node
from github.abc import Type
from github.abc import UniformResourceLocatable


class CodeOfConduct(Node, Type, UniformResourceLocatable):
    """
    Represents a Code of Conduct.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    * :class:`~github.abc.UniformResourceLocatable`
    """

    # https://developer.github.com/v4/object/codeofconduct

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0.__class__.__name__} key='{0.key}'>".format(self)

    @property
    def body(self):
        """
        The body of the code of conduct.

        :type: :class:`str`
        """

        return self.data["body"]

    @property
    def key(self):
        """
        The key of the code of conduct.

        :type: :class:`str`
        """

        return self.data["key"]

    @property
    def name(self):
        """
        The name of the code of conduct.

        :type: :class:`str`
        """

        return self.data["name"]
