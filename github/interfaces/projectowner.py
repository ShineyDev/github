from __future__ import annotations
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import TypedDict


    class ProjectOwnerData(TypedDict):
        # id: str  # NOTE: on Node
        # projectV2  # TODO
        # projectsV2  # TODO
        pass


class ProjectOwner:
    """
    Represents an object that can own a :class:`~github.Project`.
    """

    __slots__ = ()

    _data: ProjectOwnerData


__all__: list[str] = [
    "ProjectOwner",
]
