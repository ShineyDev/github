import enum


class LabelOrder(enum.Enum):
    """
    Represents fields by which you can order :class:`labels <github.Label>`.
    """

    #: The date and time at which the label was created.
    created_at = "CREATED_AT"

    #: The name of the label.
    name = "NAME"


__all__ = [
    "LabelOrder"
]
