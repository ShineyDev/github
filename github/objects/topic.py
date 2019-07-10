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

from github.objects import abc


class Topic(abc.Node):
    """
    Represents a GitHub topic.
    """

    __slots__ = ("data",)

    def __init__(self, data: dict):
        self.data = data

    def __repr__(self) -> str:
        return "<{0} name='{1}'>".format(self.__class__.__name__, self.name)

    @classmethod
    def from_data(cls, data: dict) -> typing.Union["Topic", typing.Iterable["Topic"]]:
        if "topic" in data.keys():
            return cls(data["topic"])
        elif "topics" in data.keys():
            topics = list()

            for (topic) in data["topics"]:
                topics.append(cls(topic))

            return topic

    @property
    def name(self) -> str:
        """
        The topic's name.
        """

        return self.data.get("name")

    @property
    def related_topics(self) -> typing.Iterable["PartialTopic"]:
        """
        A list of related topics.
        """

        return PartialTopic.from_data(self.data.get("relatedTopics"))

class PartialTopic(abc.Node):
    """
    Represents a GitHub topic.

    This partial-class doesn't implement the :attr:`Topic.related_topics` attribute.
    """

    __slots__ = ("data",)

    def __init__(self, data: dict):
        self.data = data

    def __repr__(self) -> str:
        return "<{0} name='{1}'>".format(self.__class__.__name__, self.name)

    @classmethod
    def from_data(cls, data: list) -> typing.Iterable["PartialTopic"]:
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
