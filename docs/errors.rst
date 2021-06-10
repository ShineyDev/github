.. currentmodule:: github.errors


Errors
======

.. autoclass:: ClientError()
    :inherited-members:

.. autoclass:: ClientResponseError()
    :inherited-members:

.. autoclass:: ClientResponseHTTPError()
    :inherited-members:

.. autoclass:: ClientResponseHTTPUnauthorizedError()
    :inherited-members:

.. autoclass:: ClientResponseGraphQLError()
    :inherited-members:

.. autoclass:: ClientResponseGraphQLForbiddenError()
    :inherited-members:

.. autoclass:: ClientResponseGraphQLInternalError()
    :inherited-members:

.. autoclass:: ClientResponseGraphQLNotFoundError()
    :inherited-members:


Hierarchy
---------

.. code-block::

    Exception
     +-- ClientError
          +-- ClientResponseError
               +-- ClientResponseHTTPError
               |    +-- ClientResponseHTTPUnauthorizedError
               +-- ClientResponseGraphQLError
                    +-- ClientResponseGraphQLForbiddenError
                    +-- ClientResponseGraphQLInternalError
                    +-- ClientResponseGraphQLNotFoundError
