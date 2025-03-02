from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    PullOrderData: TypeAlias = Literal["COMMENTS", "CREATED_AT", "UPDATED_AT"]


class PullOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`pull requests <github.Pull>`.
    """

    #: The number of comments on the pull request, in descending order.
    #: ie. most comments first.
    #:
    #: :meta hide-value:
    comment_count = {"direction": "DESC", "field": "COMMENTS"}

    #: The date and time at which the pull request was created, in
    #: ascending order. ie. earliest created first.
    #:
    #: :meta hide-value:
    created_at = {"direction": "ASC", "field": "CREATED_AT"}

    #: The date and time at which the pull request was last updated, in
    #: descending order. ie. most recently updated first.
    #:
    #: :meta hide-value:
    updated_at = {"direction": "DESC", "field": "UPDATED_AT"}


__all__ = [
    "PullOrder",
]
