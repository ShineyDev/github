from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

    from github.core.http import HTTPClient

from github.interfaces import Type


if TYPE_CHECKING:
    from typing import Literal

    from github.git.blob import BlobData
    from github.git.tree import TreeData
    from github.interfaces.type import TypeData
    from github.repository.repository import RepositoryData


    class TreeEntryData(TypeData):
        __typename: Literal["TreeEntry"]

        extension: str | None
        isGenerated: bool
        # language  # TODO
        lineCount: int | None
        mode: Literal[16384, 33188, 33261, 40960, 57344]
        name: str
        nameRaw: str
        object: BlobData | TreeData
        oid: str
        path: str
        pathRaw: str
        repository: RepositoryData
        size: int
        # submodule  # TODO
        type: Literal["blob", "tree"]


class TreeEntry(Type):
    """
    Represents a Git tree entry.
    """

    __slots__ = ()

    _data: TreeEntryData

    @staticmethod
    def _patch_data(
        data: TreeEntryData,
        /,
    ) -> TreeEntryData:
        if data.get("extension", False) == "":
            data["extension"] = None

        return data

    @classmethod
    def _from_data(
        cls: type[Self],
        data: TreeEntryData,
        /,
        *,
        http: HTTPClient,
    ) -> Self:
        return cls(cls._patch_data(data), http)

    _graphql_fields: dict[str, str] = {
        "extension": "extension",
        "is_generated": "isGenerated",
        # "__language_id": "language{id}",  # TODO: type
        "line_count": "lineCount",
        # "mode": "mode",  # TODO: type
        "name": "name",
        # "": "nameRaw",  # TODO: name
        # "__object_id": "object{id}",  # TODO: implement
        "object_id": "oid",
        "path": "path",
        # "": "pathRaw",  # TODO: name
        # "__repository_id": "repository{id}",  # TODO: implement
        "size": "size",
        # "submodule": "submodule{%s}",  # TODO: type
        # "type": "type",  # TODO: type
    }

    @property
    def extension(
        self: Self,
        /,
    ) -> str | None:
        """
        The extension of the tree entry. This is always ``None`` for
        trees.

        :type: :class:`str` | None
        """

        return self._data["extension"]

    @property
    def is_generated(
        self: Self,
        /,
    ) -> bool:
        """
        Whether the tree entry was generated.

        :type: :class:`bool`
        """

        return self._data["isGenerated"]

    @property
    def line_count(
        self: Self,
        /,
    ) -> int | None:
        """
        The number of lines in the blob. This is always ``None`` for
        trees, and never ``None`` for blobs.

        :type: :class:`int` | None
        """

        return self._data["lineCount"]

    @property
    def name(
        self: Self,
        /,
    ) -> str:
        """
        The name of the tree entry.

        :type: :class:`str`
        """

        return self._data["name"]

    @property
    def object_id(
        self: Self,
        /,
    ) -> str:
        """
        The Git object ID of the tree entry.

        :type: :class:`str`
        """

        return self._data["oid"]

    @property
    def path(
        self: Self,
        /,
    ) -> str:
        """
        The path of the tree entry.

        :type: :class:`str`
        """

        return self._data["path"]

    @property
    def size(
        self: Self,
        /,
    ) -> int:
        """
        The size of the tree entry in bytes. This is always ``0`` for
        trees.

        :type: :class:`int`
        """

        return self._data["size"]


__all__ = [
    "TreeEntry",
]
