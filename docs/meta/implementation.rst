.. currentmodule:: github


Implementation Details
======================

This document details implementation details of the library.


General
-------

- All "stupidCase" fields were renamed to "snake_case" following Python standards.


:class:`CodeOfConduct`
----------------------

- :attr:`CodeOfConduct.body` is not nullable.


:class:`License`
----------------

- ``License.featured`` is renamed to :attr:`License.is_featured`.
- ``License.hidden`` is renamed to :attr:`License.is_hidden`.
- ``License.pseudoLicense`` is renamed to :attr:`License.is_pseudo`.
- ``License.url`` is renamed to :attr:`License.choosealicense_url`.
