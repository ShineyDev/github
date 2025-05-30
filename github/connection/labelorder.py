from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    LabelOrderData: TypeAlias = Literal["CREATED_AT", "ISSUE_COUNT", "NAME"]


class LabelOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`labels <github.Label>`.
    """

    #: The date and time at which the label was created, in ascending
    #: order. ie. earliest created first.
    #:
    #: :meta hide-value:
    created_at = {"direction": "ASC", "field": "CREATED_AT"}

    #: The number of issues with the label, in descending order. ie.
    #: most labels first.
    #:
    #: :meta hide-value:
    issue_count = {"direction": "DESC", "field": "ISSUE_COUNT"}

    #: The name of the label, in ascending order. ie. A-Z.
    #:
    #: :meta hide-value:
    name = {"direction": "ASC", "field": "NAME"}


__all__ = [
    "LabelOrder",
]
