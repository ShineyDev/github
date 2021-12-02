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

    _graphql_type = "Node"

    _graphql_fields = [
        "id",
    ]

    @property
    def id(self):
        """
        The ID of the node.

        :type: :class:`str`
        """

        return self._try_get("id")

    async def _fetch_field(self, field):
        try:
            id = self.id
        except ClientObjectMissingFieldError:
            id = False

        if id is False:
            raise ClientObjectMissingFieldError("id") from None

        data = await self._http.fetch_query_node(self.__class__, id, fields=(field,))

        value = data[field]

        self._data[field] = value
        return value


__all__ = [
    "Node",
]
