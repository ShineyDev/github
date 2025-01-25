from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    MilestoneOrderData: TypeAlias = Literal["CREATED_AT", "DUE_DATE", "NUMBER", "UPDATED_AT"]


class MilestoneOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`milestones <github.Milestone>`.
    """

    #: The date and time at which the milestone was created.
    created_at = "CREATED_AT"

    #: The date and time at which the milestone is due.
    due_at = "DUE_DATE"

    #: The number of the milestone.
    number = "NUMBER"

    #: The date and time at which the milestone was last updated.
    updated_at = "UPDATED_AT"


__all__ = [
    "MilestoneOrder",
]
