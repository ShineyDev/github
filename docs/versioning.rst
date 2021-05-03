Version Guarantees
==================

This library closely follows a |semver_link|_ principle.


.. important::

    Incompatible changes apply only to non-preview documented APIs in a final release.


Given a version number PRIME.MAJOR.MINOR.MICRO, increment the:

- PRIME version when you make incompatible API changes,
- MAJOR version when you make incompatible API changes due to an incompatible GitHub API change,
- MINOR version when you add functionality in a compatible manner, and;
- MICRO version when you make compatible bug fixes.


..  Why?
    ----

    GitHub's GraphQL API follows a |calver_link|_ principle.

    An incompatible changeset is enacted on the first day of each quarter, starting 01-01. The
    changeset is publicized at least three months in advance.

    When GitHub creates an entry, the respective APIs in this library are marked as deprecated in a
    PATCH version. When the changeset is enacted, the respective APIs in this library are modified
    in a MAJOR version.

    .. TODO: also GitHubbers are humans too.

    Something I angrily noted when I was drafting this document is that whether I use
    |calver_link|_ or |semver_link|_ for this library, the outcome is identical. The API will break
    on the same date, in the same way.


Examples
--------

.. note::

    The following examples are non-exhaustive.


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

.. |semver_link| replace:: semantic versioning
.. _semver_link: https://semver.org/
