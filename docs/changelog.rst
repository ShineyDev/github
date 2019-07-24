.. currentmodule:: github

Changelog
=========

v0.1.3
------

Bug Fixes
~~~~~~~~~

* Added ``author`` and ``license`` metadata for pip. (:issue:`3`)

New Features
~~~~~~~~~~~~

* Update exception system.

v0.1.2
------

Bug Fixes
~~~~~~~~~

* Make ``json`` kwarg required in :meth:`~github.http.HTTPClient.request`.

New Features
~~~~~~~~~~~~

* Add ``session`` kwarg to :class:`github.GitHub`.
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

* Fix version regex.
* Add ``objects`` and ``abc`` to packages.

New Features
~~~~~~~~~~~~

* Add ``__main__`` for ``py -m github --version``.

< v0.1.0
--------

Features and bug fixes before v0.1.0 were not documented.
