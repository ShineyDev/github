from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    RepositoryLockReasonData: TypeAlias = Literal["BILLING", "MIGRATING", "MOVING", "RENAME", "TRADE_RESTRICTION", "TRANSFERRING_OWNERSHIP"]


class RepositoryLockReason(enum.Enum):
    """
    Represents the reason an :class:`~github.Repository` was locked.
    """

    #: The repository is locked for a billing-related reason.
    #:
    #: :meta hide-value:
    billing = "BILLING"

    #: The repository is locked due to a migration.
    #:
    #: :meta hide-value:
    migrating = "MIGRATING"

    #: The repository is locked due to a move.
    #:
    #: :meta hide-value:
    moving = "MOVING"

    #: The repository is locked due to a rename.
    #:
    #: :meta hide-value:
    rename = "RENAME"

    #: The repository is locked by trade control.
    #:
    #: :meta hide-value:
    trade = "TRADE_RESTRICTION"

    #: The repository is locked due to a transfer.
    #:
    #: :meta hide-value:
    transfer = "TRANSFERRING_OWNERSHIP"


__all__ = [
    "RepositoryLockReason",
]
