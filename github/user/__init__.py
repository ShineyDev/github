from github.user.user import *
from github.user.user import __all__ as _user__all__
from github.user.userstatus import *
from github.user.userstatus import __all__ as _userstatus__all__


__all__: list[str] = [  # type: ignore[reportUnsupportedDunderAll]
    *_user__all__,
    *_userstatus__all__,
]
