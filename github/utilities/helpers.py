from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Iterable

    from github import Type
    from github.utilities.types import T_json_key, T_json_object, T_json_value

import functools


def follow(
    data: T_json_object,
    path: Iterable[T_json_key],
    /,
) -> T_json_value:
    def __getitem__(
        object: T_json_object,
        key: T_json_key,
        /,
    ) -> T_json_object:
        return object[key]  # type: ignore

    return functools.reduce(__getitem__, path, data)


def get_graphql_type(
    type: type[Type],
    /,
) -> str:
    try:
        name = type._graphql_type
    except AttributeError:
        name = type.__name__

    return name


def get_defined_graphql_fields(
    type: type[Type],
    /,
) -> dict[str, str]:
    try:
        if isinstance(type._graphql_fields, dict):
            defined_fields = type._graphql_fields.copy()
        else:
            defined_fields = {f: f for f in type._graphql_fields}
    except AttributeError:
        defined_fields = dict()

    for type in type.__bases__:
        for (key, value) in get_defined_graphql_fields(type).items():
            if key not in defined_fields.keys():
                defined_fields[key] = value

    return defined_fields


def get_merged_graphql_fields(
    type: type[Type],
    requested_fields: Iterable[str] | None = None,
    /,
) -> list[str]:
    defined_fields = get_defined_graphql_fields(type)

    if requested_fields is None:
        return list(defined_fields.values())

    merged_fields = list(requested_fields)

    for (i, r_field) in enumerate(merged_fields):
        try:
            r_field = defined_fields[r_field]
        except KeyError:
            pass
        else:
            merged_fields[i] = r_field

    if "__typename" not in merged_fields:
        merged_fields.append("__typename")

    return merged_fields


def get_defined_repr_fields(
    type: type[Type],
    /,
) -> list[str]:
    try:
        repr_fields = type._repr_fields.copy()
    except AttributeError:
        repr_fields = list()

    for type in type.__bases__:
        for element in get_defined_repr_fields(type):
            if element not in repr_fields:
                repr_fields.append(element)

    return sorted(repr_fields)


__all__: list[str] = [
    "follow",
    "get_graphql_type",
    "get_defined_graphql_fields",
    "get_merged_graphql_fields",
    "get_defined_repr_fields",
]
