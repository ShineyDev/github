from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    DiscussionOrderData: TypeAlias = Literal["CREATED_AT", "UPDATED_AT"]


class DiscussionOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`discussions <github.Discussion>`.
    """

    #: The date and time at which the discussion was created.
    #:
    #: :meta hide-value:
    created_at = "CREATED_AT"

    #: The date and time at which the discussion was last updated.
    #:
    #: :meta hide-value:
    updated_at = "UPDATED_AT"


__all__ = [
    "DiscussionOrder",
]
