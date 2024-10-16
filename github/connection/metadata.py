from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

from github.interfaces import Type


if TYPE_CHECKING:
    from github.interfaces.type import TypeData


    class MetadataData(TypeData):
        gitIpAddresses: list[str]
        githubEnterpriseImporterIpAddresses: list[str]
        gitHubServicesSha: str
        hookIpAddresses: list[str]
        importerIpAddresses: list[str]
        isPasswordAuthenticationVerifiable: bool
        pagesIpAddresses: list[str]


class Metadata(Type):
    """
    Represents GitHub instance metadata.
    """

    __slots__ = ()

    _data: MetadataData

    _graphql_type: str = "GitHubMetadata"

    _graphql_fields: dict[str, str] = {
        "enterprise_importer_ip_addresses": "githubEnterpriseImporterIpAddresses",
        "git_ip_addresses": "gitIpAddresses",
        "github_services_sha": "gitHubServicesSha",
        "webhook_ip_addresses": "hookIpAddresses",
        "importer_ip_addresses": "importerIpAddresses",
        # "is_password_authentication_verifiable": "isPasswordAuthenticationVerifiable",  # NOTE: see Metadata.is_password_authentication_verifiable
        "pages_ip_addresses": "pagesIpAddresses",
    }

    @property
    def enterprise_importer_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses that GitHub Enterprise Importer uses for
        outbound connections.

        :type: List[:class:`str`]
        """

        return self._data["githubEnterpriseImporterIpAddresses"]

    @property
    def git_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for Git operations.

        :type: List[:class:`str`]
        """

        return self._data["gitIpAddresses"]

    @property
    def github_services_sha(
        self: Self,
        /,
    ) -> str:
        """
        The SHA of ``github-services``.

        :type: :class:`str`
        """

        return self._data["gitHubServicesSha"]

    @property
    def webhook_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for webhooks.

        :type: List[:class:`str`]
        """

        return self._data["hookIpAddresses"]

    @property
    def importer_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for the importer.

        :type: List[:class:`str`]
        """

        return self._data["importerIpAddresses"]

    @property
    def is_password_authentication_verifiable(
        self: Self,
        /,
    ) -> bool:
        """
        Whether users are verified.

        .. note::

            This field is not requested by default. It will always be
            ``False`` on this branch. See TODO.

        :type: :class:`bool`
        """

        return self._data["isPasswordAuthenticationVerifiable"]

    @property
    def pages_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for GitHub Pages.

        :type: List[:class:`str`]
        """

        return self._data["pagesIpAddresses"]


__all__: list[str] = [
    "Metadata",
]
