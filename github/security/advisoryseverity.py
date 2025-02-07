from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    AdvisorySeverityData: TypeAlias = Literal["CRITICAL", "HIGH", "LOW", "MODERATE"]


class AdvisorySeverity(enum.Enum):
    """
    Represents the severity of an :class:`~github.Advisory`.
    """

    #: The advisory severity is critical.
    #:
    #: :meta hide-value:
    critical = "CRITICAL"

    #: The advisory severity is high.
    #:
    #: :meta hide-value:
    high = "HIGH"

    #: The advisory severity is moderate.
    #:
    #: :meta hide-value:
    moderate = "MODERATE"

    #: The advisory severity is low.
    #:
    #: :meta hide-value:
    low = "LOW"


__all__ = [
    "AdvisorySeverity",
]
