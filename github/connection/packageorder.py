from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    PackageOrderData: TypeAlias = Literal["CREATED_AT"]


class PackageOrder(enum.Enum):
    """
    Represents fields by which you can order
    :class:`packages <github.Package>`.
    """

    #: The date and time at which the package was created.
    #:
    #: :meta hide-value:
    created_at = "CREATED_AT"


__all__ = [
    "PackageOrder",
]
