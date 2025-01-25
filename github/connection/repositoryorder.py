from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    RepositoryOrderData: TypeAlias = Literal["CREATED_AT", "NAME", "PUSHED_AT", "STARGAZERS", "UPDATED_AT"]


class RepositoryOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`repositories <github.Repository>`.
    """

    #: The date and time at which the repository was created.
    created_at = "CREATED_AT"

    #: The name of the repository.
    name = "NAME"

    #: The date and time at which the repository was last pushed.
    pushed_at = "PUSHED_AT"

    #: The number of stars on the repository.
    stargazer_count = "STARGAZERS"

    #: The date and time at which the repository was last updated.
    updated_at = "UPDATED_AT"


__all__ = [
    "RepositoryOrder",
]
