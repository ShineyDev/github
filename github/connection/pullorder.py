from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    PullOrderData: TypeAlias = Literal["COMMENTS", "CREATED_AT", "UPDATED_AT"]


class PullOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`pull requests <github.Pull>`.
    """

    #: The number of comments on the pull request.
    comment_count = "COMMENTS"

    #: The date and time at which the pull request was created.
    created_at = "CREATED_AT"

    #: The date and time at which the pull request was last updated.
    updated_at = "UPDATED_AT"


__all__ = [
    "PullOrder"
]
