from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    AdvisoryOrderData: TypeAlias = Literal["EPSS_PERCENTAGE", "EPSS_PERCENTILE", "PUBLISHED_AT", "UPDATED_AT"]


class AdvisoryOrder(enum.Enum):
    """
    Represents fields by which you can order
    :class:`advisories <github.Advisory>`.
    """

    # TODO: EPSS_PERCENTAGE
    # TODO: EPSS_PERCENTILE

    #: The date and time at which the advisory was published, in
    #: ascending order. ie. earliest published first.
    #:
    #: :meta hide-value:
    published_at = {"direction": "ASC", "field": "PUBLISHED_AT"}

    #: The date and time at which the advisory was last updated, in
    #: descending order. ie. most recently updated first.
    #:
    #: :meta hide-value:
    updated_at = {"direction": "DESC", "field": "UPDATED_AT"}


__all__ = [
    "AdvisoryOrder",
]
