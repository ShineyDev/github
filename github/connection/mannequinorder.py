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

    #: The date and time at which the mannequin was created, in
    #: ascending order. ie. earliest created first.
    #:
    #: :meta hide-value:
    created_at = {"direction": "ASC", "field": "CREATED_AT"}

    #: The login of the mannquin, in ascending order. ie. A-Z.
    #:
    #: :meta hide-value:
    login = {"direction": "ASC", "field": "LOGIN"}


__all__ = [
    "MannequinOrder",
]
