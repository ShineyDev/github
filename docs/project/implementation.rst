.. currentmodule:: github


Implementation Details
======================

This document details implementation details of the library.


:class:`CodeOfConduct`
----------------------

- :attr:`CodeOfConduct.body` is not nullable.


:class:`License`
----------------

- ``License.featured`` is renamed to :attr:`License.is_featured`.
- ``License.hidden`` is renamed to :attr:`License.is_hidden`.
- ``License.pseudoLicense`` is renamed to :attr:`License.is_pseudo`.
- ``License.url`` is renamed to :attr:`License.choosealicense_url`.


:class:`Metadata`
-----------------

- ``GitHubMetadata`` is renamed to :class:`Metadata`
- ``GitHubMetadata.githubEnterpriseImporterIpAddresses`` is renamed to :attr:`Metadata.enterprise_importer_ip_addresses`
- ``GitHubMetadata.hookIpAddresses`` is renamed to :attr:`Metadata.webhook_ip_addresses`


:class:`RateLimit`
------------------

- ``RateLimit.resetAt`` is renamed to :attr:`RateLimit.resets_at`
