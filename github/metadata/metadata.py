from github.interfaces import Type


class Metadata(Type):
    """
    Represents GitHub instance metadata.
    """

    __slots__ = ()

    _graphql_type = "GitHubMetadata"

    _graphql_fields = {
        "git_ip_addresses": "gitIpAddresses",
        "github_services_sha": "gitHubServicesSha",
        "hook_ip_addresses": "hookIpAddresses",
        "importer_ip_addresses": "importerIpAddresses",
        "is_password_authentication_verifiable": "isPasswordAuthenticationVerifiable",
        "pages_ip_addresses": "pagesIpAddresses",
    }

    @property
    def git_ip_addresses(self):
        """
        The IP addresses for Git operations.

        :type: List[:class:`str`]
        """

        return self._get_field("gitIpAddresses")

    @property
    def github_services_sha(self):
        """
        The SHA of ``github-services``.

        :type: :class:`str`
        """

        return self._get_field("gitHubServicesSha")

    @property
    def hook_ip_addresses(self):
        """
        The IP addresses for service hooks.

        :type: List[:class:`str`]
        """

        return self._get_field("hookIpAddresses")

    @property
    def importer_ip_addresses(self):
        """
        The IP addresses for the importer.

        :type: List[:class:`str`]
        """

        return self._get_field("importerIpAddresses")

    @property
    def is_password_authentication_verifiable(self):
        """
        Whether users are verified.

        :type: :class:`bool`
        """

        return self._get_field("isPasswordAuthenticationVerifiable")

    @property
    def pages_ip_addresses(self):
        """
        The IP addresses for GitHub Pages.

        :type: List[:class:`str`]
        """

        return self._get_field("pagesIpAddresses")


__all__ = [
    "Metadata",
]
