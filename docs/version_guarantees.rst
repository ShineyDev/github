Version Guarantees
==================

This library closely follows a `semantic versioning principle <https://semver.org/>`_. However, due
to GitHub's breaking changes implementation this is quite the task to uphold.

Incompatible, or "breaking", changes apply only to non-preview documented APIs in a "final"
release.


.. note::

    The following examples are non-exhaustive.

Examples of breaking changes
----------------------------

- Renaming an API without providing an alias.
- Adding required parameters to an API.

Examples of non-breaking changes
--------------------------------

- **Changing or removing an API previously marked as changing or deprecated.**

  .. note::

      This applies only to APIs changing or deprecated due to a GitHub API breaking change.

      TL;DR. Marking an API as changing or deprecated is a PATCH version. Changing or removing the
      API is a MINOR version and will be explicitly placed at the top of the version's changelog
      entry.

      For users of this library who find this hard to follow:
      
      GitHub API v4 follows a `calendar versioning principle <https://calver.org/>`_ and produces a
      breaking changeset on the first day of each quarter, starting ``xxxx-01-01``. These are
      defined "at least" three months before the changeset is enacted.

      When GitHub generates an entry, the respective API(s) in this library are marked as changing
      or deprecated in a PATCH version. When an entry is set to be enacted, the respective API(s)
      in this library are changed or removed in a MINOR version.

      While my reasons for not using a calendar versioning principle in this library are personal,
      and handling this specific task will be a pain, I do believe that it will be easier for
      library users to follow explicit breaking changes.
      
      n.b. Whether I use CalVer or SemVer for this project, the API will still break on the same
      date and in the same way, thus nulling any real reason to use a versioning principal I do not
      like.

- Modifying an undocumented API in any way.
- Modifying a schema preview in any way.
- Adding or removing optional parameters to an API.
- Modifying the behaviour of an API to fix a bug.
