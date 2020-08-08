"""
/github/objects/licenserule.py

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

from github.abc import Type


class LicenseRule(Type):
    """
    Represents a license's conditions, permissions, or limitations.

    Implements:

    * :class:`~github.abc.Type`
    """

    # https://docs.github.com/en/graphql/reference/objects#licenserule

    __slots__ = ("data",)

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<{0.__class__.__name__} key='{0.key}'>".format(self)

    @property
    def description(self):
        """
        A description of the rule.

        :type: :class:`str`
        """

        return self.data["description"]

    @property
    def key(self):
        """
        The machine-readable rule key.

        :type: :class:`str`
        """

        return self.data["key"]

    @property
    def label(self):
        """
        The human-readable rule label.

        :type: :class:`str`
        """

        return self.data["label"]
