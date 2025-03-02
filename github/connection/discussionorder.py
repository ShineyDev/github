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

    #: The date and time at which the discussion was created, in
    #: ascending order. ie. earliest created first.
    #:
    #: :meta hide-value:
    created_at = {"direction": "ASC", "field": "CREATED_AT"}

    #: The date and time at which the discussion was last updated, in
    #: descending order. ie. most recently updated first.
    #:
    #: :meta hide-value:
    updated_at = {"direction": "DESC", "field": "UPDATED_AT"}


__all__ = [
    "DiscussionOrder",
]
