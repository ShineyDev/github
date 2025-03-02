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

    #: The date and time at which the repository was created, in
    #: ascending order. ie. earliest created first.
    #:
    #: :meta hide-value:
    created_at = {"direction": "ASC", "field": "CREATED_AT"}

    #: The name of the repository, in ascending order. ie. A-Z.
    #:
    #: :meta hide-value:
    name = {"direction": "ASC", "field": "NAME"}

    #: The date and time at which the repository was last pushed, in
    #: descending order. ie. most recently pushed first.
    #:
    #: :meta hide-value:
    pushed_at = {"direction": "DESC", "field": "PUSHED_AT"}

    #: The number of stars on the repository, in descending first. ie.
    #: most stargazers first.
    stargazer_count = {"direction": "DESC", "field": "STARGAZERS"}

    #: The date and time at which the repository was last updated, in
    #: descending order. ie. most recently updated first.
    #:
    #: :meta hide-value:
    updated_at = {"direction": "DESC", "field": "UPDATED_AT"}


__all__ = [
    "RepositoryOrder",
]
