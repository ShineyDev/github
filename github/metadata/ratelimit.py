from github import utils
from github.errors import ClientObjectMissingFieldError
from github.interfaces import Type


class RateLimit(Type):
    """
    Represents GitHub rate limit data.
    """

    __slots__ = ()

    _graphql_type = "RateLimit"

    _graphql_fields = {
        "limit": "limit",
        "remaining": "remaining",
        "resets_at": "resetAt",
        "used": "used",
    }

    @property
    def limit(self):
        """
        The maximum number of points the client is permitted to consume
        in a rate limit window.

        :type: :class:`int`
        """

        try:
            limit = self._get_field("limit")
        except ClientObjectMissingFieldError as e:
            try:
                remaining = self._get_field("remaining")
                used = self._get_field("used")
            except ClientObjectMissingFieldError:
                raise e from None

            limit = remaining + used

        return limit

    @property
    def remaining(self):
        """
        The number of points remaining in the current rate limit
        window.

        :type: :class:`int`
        """

        try:
            remaining = self._get_field("remaining")
        except ClientObjectMissingFieldError as e:
            try:
                limit = self._get_field("limit")
                used = self._get_field("used")
            except ClientObjectMissingFieldError:
                raise e from None

            remaining = limit - used

        return remaining

    @property
    def resets_at(self):
        """
        When the current rate limit window will reset.

        :type: :class:`~datetime.datetime`
        """

        return utils.iso_to_datetime(self._get_field("resetAt"))

    @property
    def used(self):
        """
        The number of points used in the current rate limit window.

        :type: :class:`int`
        """

        try:
            used = self._get_field("used")
        except ClientObjectMissingFieldError as e:
            try:
                limit = self._get_field("limit")
                remaining = self._get_field("remaining")
            except ClientObjectMissingFieldError:
                raise e from None

            used = limit - remaining

        return used


__all__ = [
    "RateLimit",
]
