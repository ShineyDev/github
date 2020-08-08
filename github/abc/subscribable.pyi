from github.enums import SubscriptionState


class Subscribable():
    @property
    def viewer_can_subscribe(self) -> bool: ...
    @property
    def viewer_subscription(self) -> SubscriptionState: ...

    async def update_subscription(self, state: SubscriptionState) -> None: ...
