from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.core.http import HTTPClient
    from github.interfaces import Node
    from github.repository import SubscriptionState

import github


if TYPE_CHECKING:
    from typing import TypedDict


    class OptionalSubscribableData(TypedDict, total=False):
        pass


    class SubscribableData(OptionalSubscribableData):
        # NOTE: id: str (on Node)
        viewerCanSubscribe: bool
        viewerSubscription: str


class Subscribable:
    """
    Represents an object that can be subscribed to.
    """

    __slots__ = ()

    _data: SubscribableData
    _http: HTTPClient

    _graphql_fields: dict[str, str] = {
        "viewer_can_update_subscription": "viewerCanSubscribe",
        "viewer_subscription": "viewerSubscription",
    }

    @property
    def viewer_can_update_subscription(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the authenticated user can update its subscription to
        the subscribable.

        :type: :class:`bool`
        """

        return self._data["viewerCanSubscribe"]

    @property
    def viewer_subscription(
        self: Self,
        /,
    ) -> SubscriptionState:
        """
        The authenticated user's subscription to the subscribable.

        :type: :class:`~github.SubscriptionState`
        """

        return github.SubscriptionState(self._data["viewerSubscription"])

    async def fetch_viewer_can_update_subscription(
        self: Self,
        /,
    ) -> bool:
        """
        |coro|

        Fetches whether the authenticated user can update its
        subscription to the subscribable.

        :rtype: :class:`bool`
        """

        return await self._fetch_field("viewerCanSubscribe")  # type: ignore

    async def fetch_viewer_subscription(
        self: Self,
        /,
    ) -> SubscriptionState:
        """
        |coro|

        Fetches the authenticated user's subscription to the
        subscribable.

        :rtype: :class:`~github.SubscriptionState`
        """

        subscription = await self._fetch_field("viewerSubscription")  # type: ignore

        return github.SubscriptionState(self._data["viewerSubscription"])

    async def ignore(
        self: Self,
        /,
    ) -> None:
        """
        |coro|

        Ignores the subscribable.

        This is a helper function which calls
        :attr:`~.update_subscription` with
        `state=SubscriptionState.ignored`.
        """

        await self.update_subscription(github.SubscriptionState.ignored)

    async def subscribe(
        self: Self,
        /,
    ) -> None:
        """
        |coro|

        Subscribes to the subscribable.

        This is a helper function which calls
        :attr:`~.update_subscription` with
        `state=SubscriptionState.subscribed`.
        """

        await self.update_subscription(github.SubscriptionState.subscribed)

    async def unsubscribe(
        self: Self,
        /,
    ) -> None:
        """
        |coro|

        Unsubscribes from the subscribable.

        This is a helper function which calls
        :attr:`~.update_subscription` with
        `state=SubscriptionState.unsubscribed`.
        """

        await self.update_subscription(github.SubscriptionState.unsubscribed)

    async def update_subscription(
        self: Self,
        /,
        state: SubscriptionState,
    ) -> None:
        """
        |coro|

        Updates the authenticated user's subscription to the
        subscribable.

        Use of this mutation will also update the following fields:

        - :attr:`~.viewer_subscription`
        """

        if TYPE_CHECKING and not isinstance(self, Node):
            raise NotImplementedError

        data = await self._http.mutate_subscribable_update_subscription(self.id, state.value, fields=["viewerSubscription"])

        self._data["viewerSubscription"] = data["viewerSubscription"]


__all__: list[str] = [
    "Subscribable",
]
