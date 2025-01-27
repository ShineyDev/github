from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    PullCloseReasonData: TypeAlias = Literal["COMPLETED"]


class PullCloseReason(enum.Enum):
    """
    Represents the reason a :class:`~github.Pull` was closed.
    """

    #: The pull request is completed.
    completed = "COMPLETED"

    #: The pull request is rejected.
    rejected = "__REJECTED"


__all__ = [
    "PullCloseReason",
]
