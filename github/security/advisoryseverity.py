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
    critical = "CRITICAL"

    #: The advisory severity is high.
    high = "HIGH"

    #: The advisory severity is moderate.
    moderate = "MODERATE"

    #: The advisory severity is low.
    low = "LOW"


__all__ = [
    "AdvisorySeverity",
]
