from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Final

import importlib.util
import sys


try:
    from typing_extensions import __all__ as _typing_extensions__all__
except ImportError:
    _typing_extensions__all__ = ()


PY_39: Final[bool] = sys.version_info >= (3, 9, 0)

SUPPORTS_ANNOTATED = PY_39 or ("Annotated" in _typing_extensions__all__)  # typing.Annotated
SUPPORTS_GENERICBUILTINS = PY_39  # list[int], collections.abc.Sequence[int]
SUPPORTS_ZONEINFO = PY_39 or (importlib.util.find_spec("backports") and importlib.util.find_spec("backports.zoneinfo")) is not None  # zoneinfo

PY_310: Final[bool] = sys.version_info >= (3, 10, 0)

SUPPORTS_FLATLITERAL = PY_310  # Literal[1, Literal[2]] -> Literal[1, 2] in Literal.__new__
SUPPORTS_ISTYPEDDICT = PY_310  # typing.is_typeddict
SUPPORTS_UNIONTYPE = PY_310  # types.UnionType

PY_311: Final[bool] = sys.version_info >= (3, 11, 0)

SUPPORTS_EXCEPTIONGROUP = PY_311  # ExceptionGroup
SUPPORTS_EXCEPTIONNOTES = PY_311  # BaseException.__notes__
SUPPORTS_NEVER = PY_311 or ("Never" in _typing_extensions__all__)  # typing.Never
SUPPORTS_SELF = PY_311 or ("Self" in _typing_extensions__all__)  # typing.Self
SUPPORTS_TOMLLIB = PY_311  # tomllib
SUPPORTS_TYPEDDICTREQUIREDNESS = PY_311 or ("NotRequired" in _typing_extensions__all__ and "Required" in _typing_extensions__all__)  # NotRequired[T], Required[T]

PY_312: Final[bool] = sys.version_info >= (3, 12, 0)

SUPPORTS_MOREORIGBASES = PY_312  # python/cpython@0056701
SUPPORTS_SYSLASTEXC = PY_312  # sys.last_exc
SUPPORTS_SYSMONITORING = PY_312  # sys.monitoring
SUPPORTS_TYPEKEYWORD = PY_312  # type T
SUPPORTS_WARNINGSKIPS = PY_312


__all__ = [
    "PY_39",
    "SUPPORTS_ANNOTATED",
    "SUPPORTS_GENERICBUILTINS",
    "SUPPORTS_ZONEINFO",
    "PY_310",
    "SUPPORTS_FLATLITERAL",
    "SUPPORTS_ISTYPEDDICT",
    "SUPPORTS_UNIONTYPE",
    "PY_311",
    "SUPPORTS_EXCEPTIONGROUP",
    "SUPPORTS_EXCEPTIONNOTES",
    "SUPPORTS_NEVER",
    "SUPPORTS_SELF",
    "SUPPORTS_TOMLLIB",
    "SUPPORTS_TYPEDDICTREQUIREDNESS",
    "PY_312",
    "SUPPORTS_MOREORIGBASES",
    "SUPPORTS_SYSLASTEXC",
    "SUPPORTS_SYSMONITORING",
    "SUPPORTS_TYPEKEYWORD",
    "SUPPORTS_WARNINGSKIPS",
]
