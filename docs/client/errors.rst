.. currentmodule:: github.errors


Errors
======

.. autoclass:: ClientError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientObjectMissingFieldError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseGraphQLError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseGraphQLForbiddenError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseGraphQLInsufficientScopesError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseGraphQLInternalError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseGraphQLNotFoundError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseGraphQLUnprocessableError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseHTTPError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientResponseHTTPUnauthorizedError()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ClientDeprecationWarning()
    :inherited-members:
    :exclude-members: with_traceback

.. autoclass:: ServerDeprecationWarning()
    :inherited-members:
    :exclude-members: with_traceback


Hierarchy
---------

.. code-block::

    Exception
     +-- ClientError
          +-- ClientObjectMissingFieldError
          +-- ClientResponseError
               +-- ClientResponseGraphQLError
               |    +-- ClientResponseGraphQLForbiddenError
               |    +-- ClientResponseGraphQLInsufficientScopesError
               |    +-- ClientResponseGraphQLInternalError
               |    +-- ClientResponseGraphQLNotFoundError
               |    +-- ClientResponseGraphQLUnprocessableError
               +-- ClientResponseHTTPError
                    +-- ClientResponseHTTPUnauthorizedError

    DeprecationWarning
     +-- ClientDeprecationWarning
     +-- ServerDeprecationWarning
