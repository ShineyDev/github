.. currentmodule:: github


Setting Up Logging
==================

github.py logs all errors and debug information via the built-in :mod:`logging` module.

Configuration can be as simple as:

.. code:: py

    import logging
    import sys

    logger = logging.getLogger("github.http")
    logger.addHandler(logging.StreamHandler(sys.stdout))

Placed at the start of the application.

My personal configuration of the logging module for most libraries is:

.. code:: py

    import logging
    import logging.handlers

    logger = logging.getLogger("github.http")
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler("github.log", maxBytes=10**7, backupCount=5)
    formatter = logging.Formatter("[%(asctime)s,%(msecs)d] %(levelname)s: %(message)s", "%m/%d/%Y %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

For more information, see the :mod:`logging` module.
