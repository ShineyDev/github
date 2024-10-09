from __future__ import annotations

import enum


class SubscriptionState(enum.Enum):
    """
    Represents a user's subscription to a
    :class:`~github.Subscribable`.
    """

    #: The user is never notified.
    ignored = "IGNORED"

    #: The user is notified of all conversation.
    subscribed = "SUBSCRIBED"

    #: The user is notified when participating or mentioned.
    unsubscribed = "UNSUBSCRIBED"


__all__ = [
    "SubscriptionState"
]
