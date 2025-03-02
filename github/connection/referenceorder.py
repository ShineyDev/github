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

    #: The date and time at which the reference was committed, in
    #: descending order. ie. most recently committed first.
    #:
    #: :meta hide-value:
    committed_at = {"direction": "DESC", "field": "TAG_COMMIT_DATE"}

    #: The name of the reference, in ascending order. ie. A-Z.
    #:
    #: :meta hide-value:
    name = {"direction": "ASC", "field": "ALPHABETICAL"}


__all__ = [
    "ReferenceOrder",
]
