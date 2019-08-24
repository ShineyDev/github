.. currentmodule:: github.errors


Errors
======

.. autoexception:: GitHubError()

.. autoexception:: HTTPException()

.. autoexception:: Forbidden()

.. autoexception:: Internal()

.. autoexception:: NotFound()

.. autoexception:: Unauthorized()


Exception Hierarchy:

.. code::

    GitHubError
     +-- HTTPException
          +-- Forbidden
          +-- Internal
          +-- NotFound
          +-- Unauthorized
