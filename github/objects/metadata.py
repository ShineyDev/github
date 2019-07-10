"""
/github/objects/metadata.py

    Copyright (c) 2019 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import typing


class Metadata():
    """
    Represents information about the GitHub instance.

    https://developer.github.com/v4/object/githubmetadata/
    """

    __slots__ = ("data",)

    def __init__(self, data: dict):
        self.data = data

    @classmethod
    def from_data(cls, data: dict) -> "Metadata":
        return cls(data["meta"])

    @property
    def git_ip_addresses(self) -> typing.Iterable[str]:
        """
        IP addresses that users connect to for git operations.
        """

        return self.data.get("gitIpAddresses")

    @property
    def github_services_sha(self) -> str:
        """
        SHA of github-services.
        """

        return self.data.get("gitHubServicesSha")

    @property
    def hook_ip_addresses(self) -> typing.Iterable[str]:
        """
        IP addresses that service hooks are sent from.
        """

        return self.data.get("hookIpAddresses")

    @property
    def importer_ip_addresses(self) -> typing.Iterable[str]:
        """
        IP addresses that the importer connects from.
        """

        return self.data.get("importerIpAddresses")

    @property
    def is_authentication_verifiable(self) -> bool:
        """
        Whether or not users are verified.
        """

        return self.data.get("isPasswordAuthenticationVerifiable")

    @property
    def pages_ip_addresses(self) -> typing.Iterable[str]:
        """
        IP addresses for GitHub Pages' A records.
        """

        return self.data.get("pagesIpAddresses")
