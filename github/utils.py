_empty_list = list()

def _get_fields(type):
    try:
        fields = list(type._fields)
    except AttributeError:
        return _empty_list

    for type in type.__bases__:
        fields.extend(_get_fields(type))

    return fields


__all__ = []
