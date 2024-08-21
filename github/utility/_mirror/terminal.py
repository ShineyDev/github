from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import TextIO

import ctypes
import os
import sys

from .typing import MISSING


if sys.platform == "win32":
    from .windows import get_console_mode, ConsoleMode


def apply_ansi_sgr(
    string: str,
    sgr: str | tuple[str, str] | None,
    /,
    *,
    stream: TextIO = MISSING,
) -> str:
    """
    TODO
    """

    if sgr is None:
        return string

    if stream is not MISSING and not wants_ansi_sgr(stream):
        return string

    if isinstance(sgr, str):
        sgr_start, sgr_end = sgr, "0"
    else:
        sgr_start, sgr_end = sgr

    return f"\x1B[{sgr_start}m{string}\x1B[{sgr_end}m"


def supports_ansi(
    stream: TextIO = MISSING,
    /,
) -> bool:
    """
    TODO
    """

    if sys.platform == "win32":
        try:
            console_mode = get_console_mode(stream=stream)
        except ctypes.WinError:
            return False
        else:
            if isinstance(console_mode, ConsoleMode):
                return bool(console_mode & ConsoleMode.output_virtual_terminal_processing)
            else:
                return False

    if stream is MISSING:
        stream = sys.stdout

    return stream.isatty()


def wants_ansi_sgr(
    stream: TextIO = MISSING,
    /,
) -> bool:
    """
    Determines whether a stream advertises that it both wants and
    supports ANSI SGR escape sequences to be used in its output.

    Specifically, this function does the following, in this order:

    - If the stream advertises that it wants ANSI SGR escape sequences
      continue, otherwise return False.
        - On Python 3.13 and higher, if the environment variable
          |PYTHON_COLORS| is set to ``"0"`` return False.
        - If the environment variable |NO_COLOR| is set with any value
          return False.
        - If the environment variable |FORCE_COLOR| is set with any
          value return True.
        - If the environment variable "TERM" is set to ``"dumb"``
          return False.
    - If the stream advertises that it supports ANSI escape sequences
      return True, otherwise return False.


    Parameters
    ----------
    stream: :class:`~io.TextIO`
        A :class:`text <str>` stream.


    Returns
    -------
    :class:`bool`
        Whether the stream advertises that it both supports and wants
        ANSI SGR escape sequences to be used in its output.
    """

    if sys.version_info >= (3, 13):
        if os.environ.get("PYTHON_COLORS") == "0":
            return False

    if "NO_COLOR" in os.environ.keys():
        return False

    if "FORCE_COLOR" in os.environ.keys():
        return True

    if os.environ.get("TERM") == "dumb":
        return False

    return supports_ansi(stream)


__all__ = [
    "apply_ansi_sgr",
    "supports_ansi",
    "wants_ansi_sgr",
]
