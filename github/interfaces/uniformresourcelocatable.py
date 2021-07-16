class UniformResourceLocatable:
    """
    Represents an object with a URL.
    """

    __slots__ = ()

    _fields = ("resourcePath", "url")

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


__all__ = [
    "UniformResourceLocatable",
]
