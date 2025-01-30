from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    LockReasonData: TypeAlias = Literal["OFF_TOPIC", "RESOLVED", "SPAM", "TOO_HEATED"]


class LockReason(enum.Enum):
    """
    Represents the reason a :class:`~github.Lockable` was locked.
    """

    #: The conversation was too heated.
    heated = "TOO_HEATED"

    #: The conversation was resolved.
    resolved = "RESOLVED"

    #: The conversation was spam.
    spam = "SPAM"

    #: The conversation was off-topic.
    topic = "OFF_TOPIC"


__all__ = [
    "LockReason",
]
