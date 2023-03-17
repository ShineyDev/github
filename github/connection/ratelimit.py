from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.utilities.types import DateTime

from github import utilities
from github.client.errors import ClientObjectMissingFieldError
from github.interfaces import Type


if TYPE_CHECKING:
    from github.interfaces.type import TypeData


    class OptionalRateLimitData(TypedDict, total=False):
        cost: int
        nodeCount: int


    class RateLimitData(OptionalRateLimitData, TypeData):
        limit: int
        remaining: int
        resetAt: str
        used: int


class RateLimit(Type):
    """
    Represents GitHub rate limit state.
    """

    __slots__ = ()

    _data: RateLimitData

    _graphql_fields: dict[str, str] = {
        "limit": "limit",
        "remaining": "remaining",
        "resets_at": "resetAt",
        "used": "used",
    }

    @property
    def limit(
        self: Self,
        /,
    ) -> int:
        """
        The maximum number of points the client is permitted to consume
        in a rate limit window.

        :type: :class:`int`
        """

        try:
            limit = self._data["limit"]
        except ClientObjectMissingFieldError as e:
            try:
                remaining = self._data["remaining"]
                used = self._data["used"]
            except ClientObjectMissingFieldError:
                raise e from None

            limit = remaining + used

        return limit

    @property
    def remaining(
        self: Self,
        /,
    ) -> int:
        """
        The number of points remaining in the current rate limit
        window.

        :type: :class:`int`
        """

        try:
            remaining = self._data["remaining"]
        except ClientObjectMissingFieldError as e:
            try:
                limit = self._data["limit"]
                used = self._data["used"]
            except ClientObjectMissingFieldError:
                raise e from None

            remaining = limit - used

        return remaining

    @property
    def resets_at(
        self: Self,
        /,
    ) -> DateTime:
        """
        When the current rate limit window will reset.

        :type: :class:`~datetime.datetime`
        """

        return utilities.iso_to_datetime(self._data["resetAt"])

    @property
    def used(
        self: Self,
        /,
    ) -> int:
        """
        The number of points used in the current rate limit window.

        :type: :class:`int`
        """

        try:
            used = self._data["used"]
        except ClientObjectMissingFieldError as e:
            try:
                limit = self._data["limit"]
                remaining = self._data["remaining"]
            except ClientObjectMissingFieldError:
                raise e from None

            used = limit - remaining

        return used


__all__: list[str] = [
    "RateLimit",
]
