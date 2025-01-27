from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    IssueCloseReasonData: TypeAlias = Literal["COMPLETED", "DUPLICATE", "NOT_PLANNED", "REOPENED"]


class IssueCloseReason(enum.Enum):
    """
    Represents the reason an :class:`~github.Issue` was closed.
    """

    #: The issue is completed.
    completed = "COMPLETED"

    #: The issue is a duplicate.
    duplicate = "DUPLICATE"

    #: The issue is rejected.
    rejected = "NOT_PLANNED"


__all__ = [
    "IssueCloseReason",
]
