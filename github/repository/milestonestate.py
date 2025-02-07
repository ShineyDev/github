from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    MilestoneStateData: TypeAlias = Literal["CLOSED", "OPEN"]


class MilestoneState(enum.Enum):
    """
    Represents the state of an :class:`~github.Milestone`.
    """

    #: The milestone is closed.
    #:
    #: :meta hide-value:
    closed = "CLOSED"

    #: The milestone is open.
    #:
    #: :meta hide-value:
    open = "OPEN"


__all__ = [
    "MilestoneState",
]
