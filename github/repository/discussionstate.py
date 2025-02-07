from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    DiscussionStateData: TypeAlias = Literal["CLOSED", "OPEN"]


class DiscussionState(enum.Enum):
    """
    Represents the state of a :class:`discussion <github.Discussion>`.
    """

    #: The discussion is closed.
    #:
    #: :meta hide-value:
    closed = "CLOSED"

    #: The discussion is open.
    #:
    #: :meta hide-value:
    open = "OPEN"


__all__ = [
    "DiscussionState",
]
