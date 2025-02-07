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

    #: The date and time at which the release was created.
    #:
    #: :meta hide-value:
    created_at = "CREATED_AT"

    #: The title of the release.
    #:
    #: :meta hide-value:
    title = "NAME"


__all__ = [
    "ReleaseOrder",
]
