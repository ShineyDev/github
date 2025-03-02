from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    ReleaseOrderData: TypeAlias = Literal["CREATED_AT", "NAME"]


class ReleaseOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`releases <github.Release>`.
    """

    #: The date and time at which the release was created, in ascending
    #: order. ie. least earliest first.
    #:
    #: :meta hide-value:
    created_at = {"direction": "ASC", "field": "CREATED_AT"}

    #: The title of the release, in ascending order. ie. A-Z.
    #:
    #: :meta hide-value:
    title = {"direction": "ASC", "field": "NAME"}


__all__ = [
    "ReleaseOrder",
]
