from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    MannequinOrderData: TypeAlias = Literal["CREATED_AT", "LOGIN"]


class MannequinOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`mannequins <github.Mannequin>`.
    """

    #: The date and time at which the mannequin was created.
    created_at = "CREATED_AT"

    #: The login of the mannquin.
    login = "LOGIN"


__all__ = [
    "MannequinOrder",
]
