def _get_fields(type):
    try:
        fields = list(type._fields)
    except AttributeError:
        return []

    for type in type.__bases__:
        fields.extend(_get_fields(type))

    return fields


__all__ = []
