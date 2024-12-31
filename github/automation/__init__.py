from github.automation.bot import *
from github.automation.bot import __all__ as _bot__all__
from github.automation.mannequin import *
from github.automation.mannequin import __all__ as _mannequin__all__


__all__: list[str] = [  # type: ignore[reportUnsupportedDunderAll]
    *_bot__all__,
    *_mannequin__all__,
]
