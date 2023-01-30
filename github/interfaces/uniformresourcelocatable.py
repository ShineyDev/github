from github.client.errors import ClientObjectMissingFieldError


class UniformResourceLocatable:
    """
    Represents an object with a URL.
    """

    __slots__ = ()

    _graphql_fields = {
        "resource_path": "resourcePath",
        "url": "url",
    }

    @property
    def resource_path(self):
        """
        An HTTP path to the resource.

        :type: :class:`str`
        """

        return self._get_field("resourcePath")

    @property
    def url(self):
        """
        An HTTP URL to the resource.

        :type: :class:`str`
        """

        return self._get_field("url")

    async def _fetch_field(self, field, *, save=True):
        try:
            url = self.url
        except ClientObjectMissingFieldError:
            url = False

        if url is False:
            raise ClientObjectMissingFieldError("url") from None

        data = await self._http.fetch_query_resource(self.__class__, url, fields=(field,))

        value = data[field]

        if save:
            self._data[field] = value

        return value

    async def fetch_resource_path(self):
        """
        |coro|

        Fetches an HTTP path to the resource.

        Raises
        ------
        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`url` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("resourcePath")

    async def fetch_url(self):
        """
        |coro|

        Fetches an HTTP URL to the resource.

        Raises
        ------
        ~github.client.errors.ClientObjectMissingFieldError
            The :attr:`url` attribute is missing.


        :rtype: :class:`str`
        """

        return await self._fetch_field("url")


__all__ = [
    "UniformResourceLocatable",
]
