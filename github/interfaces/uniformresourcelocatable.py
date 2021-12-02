class UniformResourceLocatable:
    """
    Represents an object with a URL.
    """

    __slots__ = ()

    _graphql_type = "UniformResourceLocatable"

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

        return self._try_get("resourcePath")

    @property
    def url(self):
        """
        An HTTP URL to the resource.

        :type: :class:`str`
        """

        return self._try_get("url")

    async def _fetch_field(self, field):
        try:
            url = self.url
        except ClientObjectMissingFieldError:
            url = False

        if url is False:
            raise ClientObjectMissingFieldError("url") from None

        data = await self._http.fetch_query_resource(self.__class__, url, fields=(field,))

        value = data[field]

        self._data[field] = value
        return value


__all__ = [
    "UniformResourceLocatable",
]
