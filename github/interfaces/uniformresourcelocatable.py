class UniformResourceLocatable:
    """
    Represents an object with a URL.
    """

    __slots__ = ()

    @property
    def resource_path(self):
        """
        An HTTP path to the resource.

        :type: :class:`str`
        """

        return self._data["resourcePath"]

    @property
    def url(self):
        """
        An HTTP URL to the resource.

        :type: :class:`str`
        """

        return self._data["url"]


__all__ = [
    "UniformResourceLocatable",
]
