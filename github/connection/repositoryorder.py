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
    #:
    #: :meta hide-value:
    created_at = "CREATED_AT"

    #: The name of the repository.
    #:
    #: :meta hide-value:
    name = "NAME"

    #: The date and time at which the repository was last pushed.
    #:
    #: :meta hide-value:
    pushed_at = "PUSHED_AT"

    #: The number of stars on the repository.
    stargazer_count = "STARGAZERS"

    #: The date and time at which the repository was last updated.
    #:
    #: :meta hide-value:
    updated_at = "UPDATED_AT"


__all__ = [
    "RepositoryOrder",
]
