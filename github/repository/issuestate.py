from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    IssueStateData: TypeAlias = Literal["CLOSED", "OPEN"]


class IssueState(enum.Enum):
    """
    Represents the state of an :class:`~github.Issue`.
    """

    #: The issue is closed.
    closed = "CLOSED"

    #: The issue is open.
    open = "OPEN"


__all__ = [
    "IssueState"
]
