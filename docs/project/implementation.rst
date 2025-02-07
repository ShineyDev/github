Implementation Details
======================

This document details implementation details of the library.


:class:`~github.CodeOfConduct`
------------------------------

- :attr:`CodeOfConduct.body <github.CodeOfConduct.body>` is not nullable.


:class:`~github.License`
------------------------

- ``License.featured`` is renamed to :attr:`~github.License.is_featured`.
- ``License.hidden`` is renamed to :attr:`~github.License.is_hidden`.
- ``License.pseudoLicense`` is renamed to :attr:`~github.License.is_pseudo`.
- ``License.url`` is renamed to :attr:`~github.License.choosealicense_url`.


:class:`~github.Metadata`
-------------------------

- ``GitHubMetadata`` is renamed to :class:`~github.Metadata`
- ``GitHubMetadata.githubEnterpriseImporterIpAddresses`` is renamed to :attr:`~github.Metadata.enterprise_importer_ip_addresses`
- ``GitHubMetadata.hookIpAddresses`` is renamed to :attr:`~github.Metadata.webhook_ip_addresses`


:class:`~github.RateLimit`
--------------------------

- ``RateLimit.resetAt`` is renamed to :attr:`~github.RateLimit.resets_at`
