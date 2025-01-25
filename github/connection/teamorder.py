from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    TeamOrderData: TypeAlias = Literal["NAME"]


class TeamOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`teams <github.Team>`.
    """

    #: The name of the team.
    name = "NAME"


__all__ = [
    "TeamOrder",
]
