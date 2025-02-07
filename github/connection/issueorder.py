from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    IssueOrderData: TypeAlias = Literal["COMMENTS", "CREATED_AT", "UPDATED_AT"]


class IssueOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`issues <github.Issue>`.
    """

    #: The number of comments on the issue.
    #:
    #: :meta hide-value:
    comment_count = "COMMENTS"

    #: The date and time at which the issue was created.
    #:
    #: :meta hide-value:
    created_at = "CREATED_AT"

    #: The date and time at which the issue was last updated.
    #:
    #: :meta hide-value:
    updated_at = "UPDATED_AT"


__all__ = [
    "IssueOrder",
]
