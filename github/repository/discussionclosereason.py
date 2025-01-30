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
    duplicate = "DUPLICATE"

    #: The discussion is outdated.
    outdated = "OUTDATED"

    #: The discussion is resolved.
    resolved = "RESOLVED"


__all__ = [
    "DiscussionCloseReason",
]
