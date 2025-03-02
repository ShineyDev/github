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

    #: The date and time at which the milestone was created, in
    #: ascending order. ie. earliest created first.
    #:
    #: :meta hide-value:
    created_at = {"direction": "ASC", "field": "CREATED_AT"}

    #: The date and time at which the milestone is due, in ascending
    #: order. ie. earliest due first.
    #:
    #: :meta hide-value:
    due_at = {"direction": "ASC", "field": "DUE_DATE"}

    #: The number of the milestone, in ascending order. ie. A-Z.
    #:
    #: :meta hide-value:
    number = {"direction": "ASC", "field": "NUMBER"}

    #: The date and time at which the milestone was last updated, in
    #: descending order. ie. most recently updated first.
    #:
    #: :meta hide-value:
    updated_at = {"direction": "DESC", "field": "UPDATED_AT"}


__all__ = [
    "MilestoneOrder",
]
