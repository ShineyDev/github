from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    ReferenceOrderData: TypeAlias = Literal["ALPHABETICAL", "TAG_COMMIT_DATE"]


class ReferenceOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`issues <github.Issue>`.
    """

    #: The date and time at which the reference was committed.
    committed_at = "TAG_COMMIT_DATE"

    #: The name of the reference.
    name = "ALPHABETICAL"


__all__ = [
    "ReferenceOrder",
]
