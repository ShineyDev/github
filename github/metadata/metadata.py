from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing_extensions import Self

from github.interfaces import Type


if TYPE_CHECKING:
    from github.interfaces.type import TypeData


    class MetadataData(TypeData):
        git_ip_addresses: list[str]
        github_services_sha: str
        hook_ip_addresses: list[str]
        importer_ip_addresses: list[str]
        is_password_authentication_verifiable: bool
        pages_ip_addresses: list[str]


class Metadata(Type):
    """
    Represents GitHub instance metadata.
    """

    __slots__ = ()

    _data: MetadataData

    _graphql_type: str = "GitHubMetadata"

    _graphql_fields: dict[str, str] = {
        "git_ip_addresses": "gitIpAddresses",
        "github_services_sha": "gitHubServicesSha",
        "hook_ip_addresses": "hookIpAddresses",
        "importer_ip_addresses": "importerIpAddresses",
        "is_password_authentication_verifiable": "isPasswordAuthenticationVerifiable",
        "pages_ip_addresses": "pagesIpAddresses",
    }

    @property
    def git_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for Git operations.

        :type: List[:class:`str`]
        """

        return self._get_field("gitIpAddresses")  # type: ignore

    @property
    def github_services_sha(
        self: Self,
        /,
    ) -> str:
        """
        The SHA of ``github-services``.

        :type: :class:`str`
        """

        return self._get_field("gitHubServicesSha")  # type: ignore

    @property
    def hook_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for service hooks.

        :type: List[:class:`str`]
        """

        return self._get_field("hookIpAddresses")  # type: ignore

    @property
    def importer_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for the importer.

        :type: List[:class:`str`]
        """

        return self._get_field("importerIpAddresses")  # type: ignore

    @property
    def is_password_authentication_verifiable(
        self: Self,
        /,
    ) -> bool:
        """
        Whether users are verified.

        :type: :class:`bool`
        """

        return self._get_field("isPasswordAuthenticationVerifiable")  # type: ignore

    @property
    def pages_ip_addresses(
        self: Self,
        /,
    ) -> list[str]:
        """
        The IP addresses for GitHub Pages.

        :type: List[:class:`str`]
        """

        return self._get_field("pagesIpAddresses")  # type: ignore


__all__: list[str] = [
    "Metadata",
]
