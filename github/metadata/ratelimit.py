from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import cast
    from typing_extensions import Self

    from github.utilities.typing import DateTime

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
        resets_at: DateTime
        used: int


class RateLimit(Type):
    """
    Represents GitHub rate limit data.
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
            limit = self._get_field("limit")

            if TYPE_CHECKING:
                limit = cast(int, limit)
        except ClientObjectMissingFieldError as e:
            try:
                remaining = self._get_field("remaining")
                used = self._get_field("used")

                if TYPE_CHECKING:
                    remaining = cast(int, remaining)
                    used = cast(int, used)
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
            remaining = self._get_field("remaining")

            if TYPE_CHECKING:
                remaining = cast(int, remaining)
        except ClientObjectMissingFieldError as e:
            try:
                limit = self._get_field("limit")
                used = self._get_field("used")

                if TYPE_CHECKING:
                    limit = cast(int, limit)
                    used = cast(int, used)
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

        resets_at = self._get_field("resetAt")

        if TYPE_CHECKING:
            resets_at = cast(str, resets_at)

        return utilities.iso_to_datetime(resets_at)

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
            used = self._get_field("used")

            if TYPE_CHECKING:
                used = cast(int, used)
        except ClientObjectMissingFieldError as e:
            try:
                limit = self._get_field("limit")
                remaining = self._get_field("remaining")

                if TYPE_CHECKING:
                    limit = cast(int, limit)
                    remaining = cast(int, remaining)
            except ClientObjectMissingFieldError:
                raise e from None

            used = limit - remaining

        return used


__all__: list[str] = [
    "RateLimit",
]
