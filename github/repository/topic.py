from github.interfaces import Starrable, Type


class Topic(Starrable, Type):
    """
    Represents a repository topic.

    .. container:: operations

        .. describe:: x == y
        .. describe:: x != y

            Compares two objects by their :attr:`ID <.id>`.

        .. describe:: hash(x)

            Returns the hash of the object's :attr:`ID <.id>`.
    """

    __slots__ = ()

    _repr_fields = [
        "name",
    ]

    _graphql_type = "Topic"

    _graphql_fields = [
        "name",
    ]

    _node_prefix = "TO"

    @property
    def name(self):
        """
        The name of the topic.

        :type: :class:`str`
        """

        return self._get_field("name")

    async def fetch_name(self):
        """
        |coro|

        Fetches the name of the topic.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("name")

    async def fetch_related_topics(self, *, limit=None, **kwargs):
        """
        |coro|

        Fetches topics related to the topic.

        Parameters
        ----------
        limit: :class:`int`
            The number of related topics to fetch. Defaults to 3.

        Raises
        ------
        ~github.errors.ClientObjectMissingFieldError
            The :attr:`id` attribute is missing.


        :rtype: List[:class:`~github.Topic`]
        """

        data = await self._http.fetch_topic_related_topics(self.id, limit, **kwargs)
        return Topic(data)


__all__ = [
    "Topic",
]
