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
    #:
    #: :meta hide-value:
    confused = "CONFUSED"

    #: The ``:eyes:`` emoji.
    #:
    #: :meta hide-value:
    eyes = "EYES"

    #: The ``:heart:`` emoji.
    #:
    #: :meta hide-value:
    heart = "HEART"

    #: The ``:hooray:`` emoji.
    #:
    #: :meta hide-value:
    hooray = "HOORAY"

    #: The ``:laugh:`` emoji.
    #:
    #: :meta hide-value:
    laugh = "LAUGH"

    #: The ``:rocket:`` emoji.
    #:
    #: :meta hide-value:
    rocket = "ROCKET"

    #: The ``:-1:`` emoji.
    #:
    #: :meta hide-value:
    thumb_down = "THUMBS_DOWN"

    #: The ``:+1:`` emoji.
    #:
    #: :meta hide-value:
    thumb_up = "THUMBS_UP"


__all__ = [
    "ReactionContent",
]
