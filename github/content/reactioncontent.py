from __future__ import annotations
from typing import TYPE_CHECKING

import enum


if TYPE_CHECKING:
    from typing import Literal
    from typing_extensions import TypeAlias


    ReactionContentData: TypeAlias = Literal["CONFUSED", "EYES", "HEART", "HOORAY", "LAUGH", "ROCKET", "THUMBS_DOWN", "THUMBS_UP"]


class ReactionContent(enum.Enum):
    """
    Represents the content of a :class:`~github.Reaction`.
    """

    #: The ``:confused:`` emoji.
    confused = "CONFUSED"

    #: The ``:eyes:`` emoji.
    eyes = "EYES"

    #: The ``:heart:`` emoji.
    heart = "HEART"

    #: The ``:hooray:`` emoji.
    hooray = "HOORAY"

    #: The ``:laugh:`` emoji.
    laugh = "LAUGH"

    #: The ``:rocket:`` emoji.
    rocket = "ROCKET"

    #: The ``:-1:`` emoji.
    thumb_down = "THUMBS_DOWN"

    #: The ``:+1:`` emoji.
    thumb_up = "THUMBS_UP"


__all__ = [
    "ReactionContent",
]
