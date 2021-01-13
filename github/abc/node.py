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

    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares the :attr:`ID <.id>` of ``x`` and ``y``.
    """

    __slots__ = ()

    def __eq__(self, other):
        if issubclass(type(self), type(other)):
            return self.id == other.id

        return NotImplemented

    def __repr__(self):
        return "<{0.__class__.__name__} id='{0.id}'>".format(self)

    @property
    def id(self):
        """
        The node's ID.

        :type: :class:`str`
        """

        return self.data["id"]
