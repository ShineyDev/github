from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    SubscriptionStateData: TypeAlias = Literal["IGNORED", "SUBSCRIBED", "UNSUBSCRIBED"]


class SubscriptionState(enum.Enum):
    """
    Represents a user's subscription to a
    :class:`~github.Subscribable`.
    """

    #: The user is never notified.
    #:
    #: :meta hide-value:
    ignored = "IGNORED"

    #: The user is notified of all conversation.
    #:
    #: :meta hide-value:
    subscribed = "SUBSCRIBED"

    #: The user is notified when participating or mentioned.
    #:
    #: :meta hide-value:
    unsubscribed = "UNSUBSCRIBED"


__all__ = [
    "SubscriptionState",
]
