from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import cast

    from github.core import Client
    from github.core.http import HTTPClient
    from github.interfaces import Type

import github
from github.utility import MISSING


if TYPE_CHECKING:
    from typing import Any
else:
    Any = object


class Dummy(Any):
    """
    A lightweight stand-in for GitHub objects.


    Parameters
    ----------
    client: :class:`~github.Client`
        Your client. Provide this only when the dummy is acting as a
        stand-in for the "self" parameter of an unbound method.
    id: :class:`str`
        An :attr:`object identifier <github.Node.id>`.
    type: :class:`~github.Type`
        An object type. This doesn't have a use yet.


    Example
    -------

    .. code-block:: python

        label = github.Dummy(id="LA_kwCqcmVwb3NpdG9yeaVsYWJlbA")
        pull = github.Dummy(client=client, id="PR_kwCqcmVwb3NpdG9yeaRwdWxs")

        await github.Pull.remove_labels(pull, label)
    """

    def __init__(
        self,
        /,
        *,
        client: Client = MISSING,
        id: str = MISSING,
        type: Type = MISSING,
    ) -> None:
        self._client: Client = client
        self._id: str = id
        self._type: Type = type

    @property
    def _data(self, /) -> dict[Any, Any]:
        return DummyData()

    @property
    def _graphql_fields(self, /) -> dict[str, str] | list[str]:
        if self._type is MISSING:
            raise AttributeError

        return self._type._graphql_fields

    @property
    def _graphql_type(self, /) -> str:
        if self._type is MISSING:
            raise AttributeError

        return self._type._graphql_type

    @property
    def _http(self, /) -> HTTPClient:
        if self._client is MISSING:
            raise AttributeError

        return self._client._http

    @property
    def _node_prefix(self, /) -> str:
        if self._type is MISSING:
            raise AttributeError

        if not isinstance(self._type, github.Node):
            raise AttributeError

        return self._type._node_prefix

    @property
    def _repr_fields(self, /) -> list[str]:
        if self._type is MISSING:
            raise AttributeError

        return self._type._repr_fields

    @property
    def id(self, /) -> str:
        if self._id is MISSING:
            raise AttributeError

        return self._id


class DummyData(dict):
    def __getitem__(self, key: Any, /) -> Any:
        return self

    def __setitem__(self, key: Any, Value: Any, /) -> None:
        return


__all__ = [
    "Dummy",
]
