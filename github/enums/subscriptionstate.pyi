from enum import Enum


class SubscriptionState(Enum):
    ignored: str
    subscribed: str
    unsubscribed: str
