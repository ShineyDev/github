from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    AdvisoryClassificationData: TypeAlias = Literal["GENERAL", "MALWARE"]


class AdvisoryClassification(enum.Enum):
    """
    Represents the classification of an :class:`~github.Advisory`.
    """

    #: The advisory classification is general.
    general = "GENERAL"

    #: The advisory classification is malware.
    malware = "MALWARE"


__all__ = [
    "AdvisoryClassification",
]
