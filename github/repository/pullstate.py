from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    PullStateData: TypeAlias = Literal["CLOSED", "MERGED", "OPEN"]


class PullState(enum.Enum):
    """
    Represents the state of a :class:`pull request <github.Pull>`.
    """

    #: The pull request is closed.
    closed = "CLOSED"

    #: The pull request is merged.
    merged = "MERGED"

    #: The pull request is open.
    open = "OPEN"


__all__ = [
    "PullState",
]
