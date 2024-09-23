from github.connections.connection import *
from github.connections.connection import __all__ as _connection__all__
from github.connections.stargazerorder import *
from github.connections.stargazerorder import __all__ as _stargazerorder__all__


__all__: list[str] = [  # type: ignore[reportUnsupportedDunderAll]
    *_connection__all__,
    *_stargazerorder__all__,
]
