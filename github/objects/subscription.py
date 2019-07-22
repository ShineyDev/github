"""
/github/objects/subscription.py

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

class RepositorySubscription():
    """
    Represents a user's subscription state for a repository.
    """

    __slots__ = ("_subscription",)

    def __init__(self, subscription: str):
        self._subscription = subscription

    def __repr__(self) -> str:
        return "<{0.__class__.__name__} subscription='{0._subscription}'>".format(self)

    @classmethod
    def from_data(cls, subscription: str) -> "RepositorySubscription":
        return cls(subscription)

    @property
    def subscription(self) -> str:
        """
        The user's subscription state as a string.
        """

        return self._subscription

    @property
    def subscribed(self) -> bool:
        """
        The user is notified of all conversations.
        """

        return self._subscription == "SUBSCRIBED"

    @property
    def unsubscribed(self) -> bool:
        """
        The user is only notified when participating or mentioned.
        """

        return self._subscription == "UNSUBSCRIBED"

    @property
    def ignored(self) -> bool:
        """
        The user is never notified.
        """

        return self._subscription == "IGNORED"