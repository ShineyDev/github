class Node:
    """
    Represents an object with an ID.

    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    def __hash__(self):
        return hash(self.id)

    _repr_fields = [
        "id",
    ]

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.id == other.id

    _graphql_fields = {
        "id": "id",
    }

    @property
    def id(self):
        """
        The ID of the node.

        :type: :class:`str`
        """

        return self._try_get("id")


__all__ = [
    "Node",
]
