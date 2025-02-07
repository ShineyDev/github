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

    #: The issue is a duplicate.
    #:
    #: :meta hide-value:
    duplicate = "DUPLICATE"

    #: The issue is rejected.
    #:
    #: :meta hide-value:
    rejected = "NOT_PLANNED"

    #: The issue is resolved.
    #:
    #: :meta hide-value:
    resolved = "COMPLETED"


__all__ = [
    "IssueCloseReason",
]
