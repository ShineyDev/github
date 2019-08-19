"""
/github/objects/topic.py

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

import typing

from github.abc import Node
from github.abc import Type


class Topic(Node, Type):
    """
    Represents a GitHub topic.

    https://developer.github.com/v4/object/topic/
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
            topics = list()

            for (topic) in data:
                topics.append(cls(topic))

            return topic

    @property
    def name(self) -> str:
        """
        The topic's name.
        """

        return self.data["name"]

    @property
    def related_topics(self) -> typing.List["PartialTopic"]:
        """
        A list of related topics.
        """

        return PartialTopic.from_data(self.data["relatedTopics"])

class PartialTopic(Node):
    """
    Represents a GitHub topic.

    This partial-class doesn't implement the :attr:`Topic.related_topics` attribute.
    """

    __slots__ = ("data",)

    def __init__(self, data: dict):
        self.data = data

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} name='{0.name}'>".format(self)

    @classmethod
    def from_data(cls, data: list) -> typing.List["PartialTopic"]:
        topics = list()

        for (topic) in data:
            topics.append(cls(topic))

        return topics

    @property
    def name(self) -> str:
        """
        The topic's name.
        """

        return self.data.get("name")
