from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    CheckStatusData: TypeAlias = Literal["COMPLETED", "IN_PROGRESS", "PENDING", "QUEUED", "REQUESTED", "WAITING"]


class CheckStatus(enum.Enum):
    """
    Represents the status of a :class:`~github.Check`.
    """

    #: The check is completed.
    #:
    #: :meta hide-value:
    completed = "COMPLETED"

    #: The check is pending.
    #:
    #: :meta hide-value:
    pending = "PENDING"

    #: The check is queued.
    #:
    #: :meta hide-value:
    queued = "QUEUED"

    #: The check is requested.
    #:
    #: :meta hide-value:
    requested = "REQUESTED"

    #: The check is running.
    #:
    #: :meta hide-value:
    running = "IN_PROGRESS"

    #: The check is waiting.
    #:
    #: :meta hide-value:
    waiting = "WAITING"


__all__ = [
    "CheckStatus",
]
