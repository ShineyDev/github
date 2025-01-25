from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    LabelOrderData: TypeAlias = Literal["CREATED_AT", "NAME"]


class LabelOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`labels <github.Label>`.
    """

    #: The date and time at which the label was created.
    created_at = "CREATED_AT"

    #: The name of the label.
    name = "NAME"


__all__ = [
    "LabelOrder",
]
