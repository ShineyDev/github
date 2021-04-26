.. currentmodule:: github.errors


Errors
======

.. autoclass:: GitHubError
    :members:

.. autoclass:: HTTPError
    :members:

.. autoclass:: HTTPUnauthorizedError
    :members:

.. autoclass:: GraphQLError
    :members:

.. autoclass:: GraphQLForbiddenError
    :members:

.. autoclass:: GraphQLInternalError
    :members:

.. autoclass:: GraphQLNotFoundError
    :members:


.. code-block::

    Exception
     +-- GitHubError
          +-- HTTPError
               +-- HTTPUnauthorizedError
               +-- GraphQLError
                    +-- GraphQLForbiddenError
                    +-- GraphQLInternalError
                    +-- GraphQLNotFoundError
