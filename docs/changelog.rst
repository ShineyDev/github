.. currentmodule:: github

Changelog
=========

v0.2.1
------

Bug Fixes
~~~~~~~~~

* Fix :attr:`github.Repository.license` AttributeError.
* Fix :meth:`github.query.Collection.build` IndexError.

v0.2.0
------

New Features
~~~~~~~~~~~~

* Add :mod:`github.enums`.
* Implement :class:`github.CommitComment`.
* Implement :class:`github.Reaction`.
* Implement :meth:`github.User.fetch_commit_comments`.
* Implement :class:`github.abc.Comment`.
* Implement :class:`github.abc.Deletable`.
* Implement :class:`github.abc.Reactable`.
* Implement :class:`github.abc.RepositoryNode`.
* Implement :class:`github.abc.Updatable`.
* Implement :class:`github.enums.CannotUpdateReason`.
* Implement :class:`github.enums.CommentAuthorAssociation`.
* Implement :class:`github.enums.Reaction`.

Removed Features
~~~~~~~~~~~~~~~~

* Remove ``cache`` kwarg from :meth:`github.abc.Actor.fetch_avatar_url`.

Updated Features
~~~~~~~~~~~~~~~~

* Move ``github/objects/abc/`` to ``github/abc/``.
* Move ``github/objects/repositorylockreason`` to ``github/enums/repositorylockreason``.
* Move ``github/objects/repositorypermissions`` to ``github/enums/repositorypermissions``.
* Move ``github/objects/repositorysubscription`` to ``github/enums/repositorysubscription``.

v0.1.3
------

Bug Fixes
~~~~~~~~~

* Add ``author`` and ``license`` metadata for pip. (:issue:`3`)

Removed Features
~~~~~~~~~~~~~~~~

* Remove ``github.User.email``.

Updated Features
~~~~~~~~~~~~~~~~

* Update exception system.

v0.1.2
------

Bug Fixes
~~~~~~~~~

* Make ``json`` kwarg required in :meth:`~github.http.HTTPClient.request`.

New Features
~~~~~~~~~~~~

* Add ``session`` kwarg to :class:`github.GitHub`.

Updated Features
~~~~~~~~~~~~~~~~

* Update exception system.

v0.1.1
------

Bug Fixes
~~~~~~~~~

* Fix ``python_requires``.

v0.1.0
------

The first official version of the wrapper.

Bug Fixes
~~~~~~~~~

* Add ``objects`` and ``abc`` to packages.
* Fix version regex.

New Features
~~~~~~~~~~~~

* Implement ``__main__`` for ``py -m github --version``.

< v0.1.0
--------

Features and bug fixes before v0.1.0 were not documented.
