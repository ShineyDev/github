import functools
import operator


def follow(data, path):
    return functools.reduce(operator.getitem, path, data)


def get_graphql_type(type):
    try:
        name = type._graphql_type
    except AttributeError:
        name = type.__name__

    return name


def get_defined_graphql_fields(type):
    try:
        d_fields = type._graphql_fields
    except AttributeError:
        d_fields = dict()
    else:
        if isinstance(d_fields, dict):
            d_fields = d_fields.copy()
        else:
            d_fields = {f: f for f in d_fields}

    for type in type.__bases__:
        for (key, value) in get_defined_graphql_fields(type).items():
            if key not in d_fields.keys():
                d_fields[key] = value

    return d_fields


def get_merged_graphql_fields(type, r_fields=None):
    d_fields = get_defined_graphql_fields(type)

    if r_fields is None:
        return list(d_fields.values())

    if "__typename" not in r_fields:
        r_fields += ("__typename",)

    r_fields = list(r_fields)
    for (i, r_field) in enumerate(r_fields):
        try:
            r_field = d_fields[r_field]
        except KeyError:
            pass
        else:
            r_fields[i] = r_field

    return r_fields


def get_defined_repr_fields(type):
    try:
        d_fields = type._repr_fields.copy()
    except AttributeError:
        d_fields = list()

    for type in type.__bases__:
        for element in get_defined_repr_fields(type):
            if element not in d_fields:
                d_fields.append(element)

    return sorted(d_fields)


def wrap(wrapped):
    def decorator(wrapper):
        wrapper.__doc__ = wrapped.__doc__
        wrapper.__name__ = wrapped.__name__
        wrapper.__qualname__ = wrapped.__qualname__

        return wrapper

    return decorator


__all__ = [
    "follow",
    "get_graphql_type",
    "get_defined_graphql_fields",
    "get_merged_graphql_fields",
    "get_defined_repr_fields",
    "wrap",
]
