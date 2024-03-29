Versioning
==========

This document outlines the version guarantees of the library.


Guaruntees
----------

This library follows the modified |semver_link|_ principle described below.

Given a version number PRIME.MAJOR.MINOR.MICRO, increment the:

- PRIME version when you make incompatible API changes,
- MAJOR version when you make incompatible API changes due to an incompatible GitHub API change,
- MINOR version when you add functionality in a compatible manner, and;
- MICRO version when you make compatible bug fixes.

.. important::

    Incompatible changes apply only to non-preview documented APIs in a final release.

.. note::

    Due to the nature of the Python typing ecosystem, there are a few things that are outright
    detatched from the guarantees that this document provides.

    - The type hints provided by this library are NOT guaranteed to be made compatible within a
      MAJOR or PRIME version.
    - The type hints provided by this library are designed to be compatible with the |pyright_link|
      type checker and are NOT guaranteed to work with other type checkers.

    Additionally, the presence of type hints is NOT necessarily an indication of the publicness of
    an API.


Explanation
-----------

GitHub's GraphQL API follows a |calver_link|_ principle.

An incompatible changeset is (supposed to be) enacted on the first day of each quarter. The
changeset is (usually) publicized at least three months in advance.

When a changeset is created, the affected APIs in this library are marked as deprecated in a MICRO
version. When a changeset is enacted, the affected APIs in this library are updated in a MAJOR
version.

It's worth noting that whether I use |calver_link|_ or |semver_link|_, the API will break on the
same date, and in the same way. This changeset process is designed to minimize disruption to users,
while allowing me to clearly communicate the nature and severity of changes to this library and
GitHub's GraphQL API.


Examples
--------

Examples of incompatible changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Removing an API.
- Renaming an API without providing an alias.


Examples of compatible changes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Modifying an undocumented API.
- Modifying the behavior of an API to fix a bug.


.. |calver_link| replace:: calendar versioning
.. _calver_link: https://calver.org/

.. |pyright_link| replace:: pyright
.. _pyright_link: https://github.com/microsoft/pyright

.. |semver_link| replace:: semantic versioning
.. _semver_link: https://semver.org/
