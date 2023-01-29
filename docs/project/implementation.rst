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
