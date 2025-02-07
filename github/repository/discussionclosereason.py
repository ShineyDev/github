from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    DiscussionCloseReasonData: TypeAlias = Literal["DUPLICATE", "OUTDATED", "REOPENED", "RESOLVED"]


class DiscussionCloseReason(enum.Enum):
    """
    Represents the reason a :class:`~github.Discussion` was closed.
    """

    #: The discussion is a duplicate.
    #:
    #: :meta hide-value:
    duplicate = "DUPLICATE"

    #: The discussion is outdated.
    #:
    #: :meta hide-value:
    outdated = "OUTDATED"

    #: The discussion is resolved.
    #:
    #: :meta hide-value:
    resolved = "RESOLVED"


__all__ = [
    "DiscussionCloseReason",
]
