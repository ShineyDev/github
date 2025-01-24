from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    ReactionOrderData: TypeAlias = Literal["CREATED_AT"]


class ReactionOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`reactions <github.Reaction>`.
    """

    #: The date and time at which the reaction was created.
    created_at = "CREATED_AT"


__all__ = [
    "ReactionOrder",
]
