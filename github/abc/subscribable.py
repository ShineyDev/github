"""
/github/abc/subscribable.py

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

from github.enums import SubscriptionState


class Subscribable():
    """
    Represents an object which can be subscribed to.

    Implemented by:

    * :class:`~github.Issue`
    * :class:`~github.PullRequest`
    * :class:`~github.Repository`
    """

    # https://docs.github.com/en/graphql/reference/interfaces#subscribable

    __slots__ = ()

    @property
    def viewer_can_subscribe(self):
        """
        Whether the authenticated user can subscribe to the
        subscribable.

        :type: :class:`bool`
        """

        return self.data["viewerCanSubscribe"]

    @property
    def viewer_subscription(self):
        """
        The authenticated user's subscription state to the
        subscribable.

        :type: :class:`~github.enums.SubscriptionState`
        """

        subscription = self.data["viewerSubscription"]
        return SubscriptionState.try_value(subscription)

    async def update_subscription(self, state):
        """
        |coro|

        Updates the authenticated user's subscription state to the
        subscribable.

        Parameters
        ----------
        :class:`~github.enums.SubscriptionState`
            The new subscription state.
        """

        await self.http.mutate_subscribable_update_subscription(self.id, state.value)
