from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable, Generator
    from typing import TextIO
    from typing_extensions import Self

import ctypes
import enum
import subprocess
import sys

from .typing import MISSING


assert sys.platform == "win32"


import ctypes.wintypes
import msvcrt


def _get_console_mode(
    handle: int,
    /,
) -> int:
    """
    |internal|

    TODO
    """

    handle_c = ctypes.wintypes.HANDLE(handle)
    mode_c = ctypes.wintypes.DWORD()

    if ctypes.windll.kernel32.GetConsoleMode(handle_c, ctypes.byref(mode_c)) == 0:
        raise ctypes.WinError(ctypes.get_last_error())

    return mode_c.value


def get_console_mode(
    *,
    stream: TextIO = MISSING,
) -> ConsoleMode:
    """
    TODO
    """

    if stream is MISSING:
        mode = 0b00000100000000001

        input_handle: int = ctypes.windll.kernel32.GetStdHandle(subprocess.STD_INPUT_HANDLE)
        input_mode = _get_console_mode(input_handle)

        mode &= input_mode << 1

        output_handle: int = ctypes.windll.kernel32.GetStdHandle(subprocess.STD_OUTPUT_HANDLE)
        output_mode = _get_console_mode(output_handle)

        mode &= output_mode << 12
    else:
        if stream.writable():
            mode = 0b1 << 11
        else:
            mode = 0b1 << 0

        stream_handle = msvcrt.get_osfhandle(stream.fileno())
        stream_mode = _get_console_mode(stream_handle)

        if stream.writable():  # TODO(console-writable): is this as accurate as it needs to be?
            mode &= stream_mode << 12
        else:
            mode &= stream_mode << 1

    # NOTE: DISABLE_NEWLINE_AUTO_RETURN is normalized to ENABLE_* here.
    mode ^= 0b01000 << 12

    return ConsoleMode(mode)


def _read_console_input(
    handle: int,
    /,
    *,
    buffer_size: int,
) -> Iterable[_S_INPUT_RECORD]:
    """
    |internal|

    TODO
    """

    handle_c = ctypes.wintypes.HANDLE(handle)
    buffer_c = (_S_INPUT_RECORD * buffer_size)()
    buffer_size_c = ctypes.wintypes.DWORD(buffer_size)
    count_c = ctypes.wintypes.DWORD()

    if ctypes.windll.kernel32.ReadConsoleInputW(handle_c, ctypes.byref(buffer_c), buffer_size_c, ctypes.byref(count_c)) == 0:
        raise ctypes.WinError(ctypes.get_last_error())

    return buffer_c[:count_c.value]  # fmt: skip


def read_console_input(
    *,
    buffer_size: int = MISSING,
    stream: TextIO = MISSING,
) -> Generator[ConsoleInputEvent, None, None]:
    """
    TODO
    """

    if buffer_size is MISSING:
        buffer_size = 1

    if stream is MISSING:
        handle = ctypes.windll.kernel32.GetStdHandle(subprocess.STD_INPUT_HANDLE)
    else:
        handle = msvcrt.get_osfhandle(stream.fileno())

    while True:
        for c_record in _read_console_input(handle, buffer_size=buffer_size):
            if c_record.EventType == ConsoleInputEventType.focus:
                yield ConsoleInputFocusEvent(c_record.Event.FocusEvent)
            elif c_record.EventType == ConsoleInputEventType.key:
                yield ConsoleInputKeyEvent(c_record.Event.KeyEvent)
            elif c_record.EventType == ConsoleInputEventType.menu:
                yield ConsoleInputMenuEvent(c_record.Event.MenuEvent)
            elif c_record.EventType == ConsoleInputEventType.mouse:
                yield ConsoleInputMouseEvent(c_record.Event.MouseEvent)
            elif c_record.EventType == ConsoleInputEventType.resize:
                yield ConsoleInputResizeEvent(c_record.Event.WindowBufferSizeEvent)
            else:
                # TODO: warn?
                continue


def _set_console_mode(
    handle: int,
    mode: int,
    /,
) -> None:
    """
    |internal|

    TODO
    """

    handle_c = ctypes.wintypes.HANDLE(handle)
    mode_c = ctypes.wintypes.DWORD(mode)

    if ctypes.windll.kernel32.SetConsoleMode(handle_c, mode_c) == 0:
        raise ctypes.WinError(ctypes.get_last_error())

    return None


def set_console_mode(
    mode: ConsoleMode,
    /,
    *,
    stream: TextIO,
) -> None:
    """
    TODO
    """

    mode_i = int(mode)

    # NOTE: output_newline_auto_return is inverted to DISABLE_* here
    mode_i ^= 0b01000 << 12

    if stream is MISSING:
        input_handle: int = ctypes.windll.kernel32.GetStdHandle(subprocess.STD_INPUT_HANDLE)
        input_mode = mode_i >> 1 & 0b11111

        _set_console_mode(input_handle, input_mode)

        output_handle: int = ctypes.windll.kernel32.GetStdHandle(subprocess.STD_OUTPUT_HANDLE)
        output_mode = mode_i >> 12 & 0b1111111111

        _set_console_mode(output_handle, output_mode)
    else:
        stream_handle = msvcrt.get_osfhandle(stream.fileno())

        if stream.writable():  # TODO(console-writable): is this as accurate as it needs to be?
            stream_mode = mode_i >> 12 & 0b1111111111
        else:
            stream_mode = mode_i >> 1 & 0b11111

        _set_console_mode(stream_handle, stream_mode)


class _S_COORD(ctypes.Structure):
    _fields_ = [
        ("X", ctypes.wintypes.SHORT),
        ("Y", ctypes.wintypes.SHORT),
    ]


class _S_FOCUS_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ("bSetFocus", ctypes.wintypes.BOOL),
    ]


class _S_KEY_EVENT_RECORD(ctypes.Structure):
    class _U_CHAR(ctypes.Union):
        _fields_ = [
            ("UnicodeChar", ctypes.wintypes.WCHAR),
            ("AsciiChar", ctypes.wintypes.CHAR),
        ]

    _fields_ = [
        ("bKeyDown", ctypes.wintypes.BOOL),
        ("wRepeatCount", ctypes.wintypes.WORD),
        ("wVirtualKeyCode", ctypes.wintypes.WORD),
        ("wVirtualScanCode", ctypes.wintypes.WORD),
        ("uChar", _U_CHAR),
        ("dwControlKeyState", ctypes.wintypes.DWORD),
    ]


class _S_MENU_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        # NOTE: menu_init = 278
        #       menu_select = 287 (also implies and on menu close)
        ("dwCommandId", ctypes.wintypes.DWORD),
    ]


class _S_MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [
        ("dwMousePosition", _S_COORD),
        #
        # NOTE: we split dwButtonState into two words here. the high
        #       word of dwButtonState is a signed int which determines
        #       scroll delta, which was 120 (prior to Windows 10.22000,
        #       "11"?) and is now 128. the value shouldn't matter to
        #       users since windows implements mouse scrolling and key
        #       repeating outside of this api now.
        ("wButtonState", ctypes.wintypes.WORD),
        ("wScrollDelta", ctypes.wintypes.SHORT),
        #
        ("dwControlKeyState", ctypes.wintypes.DWORD),
        ("dwEventFlags", ctypes.wintypes.DWORD),
    ]


class _S_WINDOW_BUFFER_SIZE_RECORD(ctypes.Structure):
    _fields_ = [
        ("dwSize", _S_COORD),
    ]


class _S_INPUT_RECORD(ctypes.Structure):
    class _U_EVENT(ctypes.Union):
        _fields_ = [
            ("FocusEvent", _S_FOCUS_EVENT_RECORD),
            ("KeyEvent", _S_KEY_EVENT_RECORD),
            ("MenuEvent", _S_MENU_EVENT_RECORD),
            ("MouseEvent", _S_MOUSE_EVENT_RECORD),
            ("WindowBufferSizeEvent", _S_WINDOW_BUFFER_SIZE_RECORD),
        ]

    _fields_ = [
        ("EventType", ctypes.wintypes.WORD),
        ("Event", _U_EVENT),
    ]


class Coordinate:
    """
    TODO
    """

    def __init__(
        self: Self,
        /,
        x: int,
        y: int,
    ) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(
        self: Self,
        /,
    ) -> str:
        return f"<{self.__class__.__name__} x={self.x!r} y={self.y!r}>"


class ConsoleInputEvent:
    """
    TODO
    """

    pass


class ConsoleInputFocusEvent(ConsoleInputEvent):
    """
    TODO
    """

    def __init__(
        self: Self,
        c_event: _S_FOCUS_EVENT_RECORD,
        /,
    ) -> None:
        """
        TODO
        """

        self.is_focused: bool = c_event.bSetFocus

    def __repr__(
        self: Self,
        /,
    ) -> str:
        """
        TODO
        """

        ...


class ConsoleInputKeyEvent(ConsoleInputEvent):
    """
    TODO
    """

    def __init__(
        self: Self,
        c_event: _S_KEY_EVENT_RECORD,
        /,
    ) -> None:
        """
        TODO
        """

        self.is_key_down: bool = bool(c_event.bKeyDown)
        self.repeat_count: int = c_event.wRepeatCount
        self.virtual_key_code: int = c_event.wVirtualKeyCode
        self.virtual_scan_code: int = c_event.wVirtualScanCode
        self.unicode_char: str = c_event.uChar.UnicodeChar
        self.ascii_char: str = c_event.uChar.AsciiChar
        self.control_key_state: ControlKeyState = ControlKeyState(c_event.dwControlKeyState)

    def __repr__(
        self: Self,
        /,
    ) -> str:
        """
        TODO
        """

        ...


class ConsoleInputMenuEvent(ConsoleInputEvent):
    """
    TODO
    """

    def __init__(
        self: Self,
        c_event: _S_MENU_EVENT_RECORD,
        /,
    ) -> None:
        """
        TODO
        """

        self.command_id: int = c_event.dwCommandId

    def __repr__(
        self: Self,
        /,
    ) -> str:
        """
        TODO
        """

        ...


class ConsoleInputMouseEvent(ConsoleInputEvent):
    """
    TODO
    """

    def __init__(
        self: Self,
        c_event: _S_MOUSE_EVENT_RECORD,
        /,
    ) -> None:
        """
        TODO
        """

        self.mouse_position: tuple[int, int] = (c_event.dwMousePosition.X, c_event.dwMousePosition.Y)
        self.scroll_delta: int = c_event.wScrollDelta

        scroll_direction = None
        if c_event.dwEventFlags == ConsoleInputMouseEventType.wheel_vertical:
            if c_event.wScrollDelta > 0:
                scroll_direction = ConsoleInputMouseScrollDirection.forward
            elif c_event.wScrollDelta < 0:
                scroll_direction = ConsoleInputMouseScrollDirection.backward
        elif c_event.dwEventFlags == ConsoleInputMouseEventType.wheel_horizontal:
            if c_event.wScrollDelta > 0:
                scroll_direction = ConsoleInputMouseScrollDirection.right
            elif c_event.wScrollDelta < 0:
                scroll_direction = ConsoleInputMouseScrollDirection.left

        self.scroll_direction: ConsoleInputMouseScrollDirection | None = scroll_direction

        self.button_state: ConsoleInputMouseButtonState = ConsoleInputMouseButtonState(c_event.wButtonState)
        self.control_key_state: ControlKeyState = ControlKeyState(c_event.dwControlKeyState)
        self.event_flags: ConsoleInputMouseEventType = ConsoleInputMouseEventType(c_event.dwEventFlags)

    def __repr__(
        self: Self,
        /,
    ) -> str:
        """
        TODO
        """

        ...


class ConsoleInputResizeEvent(ConsoleInputEvent):
    """
    TODO
    """

    def __init__(
        self: Self,
        c_event: _S_WINDOW_BUFFER_SIZE_RECORD,
        /,
    ) -> None:
        """
        TODO
        """

        self.size: tuple[int, int] = (c_event.dwSize.X, c_event.dwSize.Y)

    def __repr__(
        self: Self,
        /,
    ) -> str:
        """
        TODO
        """

        ...


class _E_EventType(enum.IntEnum):
    # fmt: off
    KEY_EVENT                = 0b00001
    MOUSE_EVENT              = 0b00010
    WINDOW_BUFFER_SIZE_EVENT = 0b00100
    MENU_EVENT               = 0b01000
    FOCUS_EVENT              = 0b10000
    # fmt: on


class ConsoleInputEventType(enum.IntEnum):
    """
    TODO
    """

    focus = _E_EventType.FOCUS_EVENT
    """
    TODO
    """

    key = _E_EventType.KEY_EVENT
    """
    TODO
    """

    menu = _E_EventType.MENU_EVENT
    """
    TODO
    """

    mouse = _E_EventType.MOUSE_EVENT
    """
    TODO
    """

    resize = _E_EventType.WINDOW_BUFFER_SIZE_EVENT
    """
    TODO
    """


class _F_ControlKeyState(enum.IntFlag):
    # fmt: off
    RIGHT_ALT_PRESSED  = 0b000000001
    LEFT_ALT_PRESSED   = 0b000000010
    RIGHT_CTRL_PRESSED = 0b000000100
    LEFT_CTRL_PRESSED  = 0b000001000
    SHIFT_PRESSED      = 0b000010000
    NUMLOCK_ON         = 0b000100000
    SCROLLLOCK_ON      = 0b001000000
    CAPSLOCK_ON        = 0b010000000
    ENHANCED_KEY       = 0b100000000
    # fmt: on


class ControlKeyState(enum.IntFlag):
    """
    TODO
    """

    right_alt = _F_ControlKeyState.RIGHT_ALT_PRESSED
    """
    TODO
    """

    left_alt = _F_ControlKeyState.LEFT_ALT_PRESSED
    """
    TODO
    """

    right_ctrl = _F_ControlKeyState.RIGHT_CTRL_PRESSED
    """
    TODO
    """

    left_ctrl = _F_ControlKeyState.LEFT_CTRL_PRESSED
    """
    TODO
    """

    shift = _F_ControlKeyState.SHIFT_PRESSED
    """
    TODO
    """

    numlock = _F_ControlKeyState.NUMLOCK_ON
    """
    TODO
    """

    scrolllock = _F_ControlKeyState.SCROLLLOCK_ON
    """
    TODO
    """

    capslock = _F_ControlKeyState.CAPSLOCK_ON
    """
    TODO
    """

    enhanced_key = _F_ControlKeyState.ENHANCED_KEY
    """
    TODO
    """


class _F_MouseButtonState(enum.IntFlag):
    # fmt: off
    FROM_LEFT_1ST_BUTTON_PRESSED = 0b00001
    RIGHTMOST_BUTTON_PRESSED     = 0b00010
    FROM_LEFT_2ND_BUTTON_PRESSED = 0b00100
    FROM_LEFT_3RD_BUTTON_PRESSED = 0b01000
    FROM_LEFT_4TH_BUTTON_PRESSED = 0b10000
    # fmt: on


class ConsoleInputMouseButtonState(enum.IntFlag):
    """
    TODO
    """

    left = _F_MouseButtonState.FROM_LEFT_1ST_BUTTON_PRESSED
    """
    TODO
    """

    right = _F_MouseButtonState.RIGHTMOST_BUTTON_PRESSED
    """
    TODO
    """

    middle = _F_MouseButtonState.FROM_LEFT_2ND_BUTTON_PRESSED
    """
    TODO
    """

    x1 = _F_MouseButtonState.FROM_LEFT_3RD_BUTTON_PRESSED
    """
    TODO
    """

    x2 = _F_MouseButtonState.FROM_LEFT_4TH_BUTTON_PRESSED
    """
    TODO
    """


class _E_MouseEventFlags(enum.IntEnum):
    # fmt: off
    MOUSE_MOVED    = 0b0001
    DOUBLE_CLICK   = 0b0010
    MOUSE_WHEELED  = 0b0100
    MOUSE_HWHEELED = 0b1000
    # fmt: on


class ConsoleInputMouseEventType(enum.IntEnum):
    """
    TODO
    """

    none = 0
    """
    TODO
    """

    move = _E_MouseEventFlags.MOUSE_MOVED
    """
    TODO
    """

    double_click = _E_MouseEventFlags.DOUBLE_CLICK
    """
    TODO
    """

    wheel_vertical = _E_MouseEventFlags.MOUSE_WHEELED
    """
    TODO
    """

    wheel_horizontal = _E_MouseEventFlags.MOUSE_HWHEELED
    """
    TODO
    """


class ConsoleInputMouseScrollDirection(enum.IntEnum):
    """
    TODO
    """

    forward = 1
    """
    TODO
    """

    backward = 2
    """
    TODO
    """

    left = 3
    """
    TODO
    """

    right = 4
    """
    TODO
    """


class _F_ConsoleModeInput(enum.IntFlag):
    # fmt: off
    ENABLE_PROCESSED_INPUT        = 0b0000000001
    ENABLE_LINE_INPUT             = 0b0000000010
    ENABLE_ECHO_INPUT             = 0b0000000100
    ENABLE_WINDOW_INPUT           = 0b0000001000
    ENABLE_MOUSE_INPUT            = 0b0000010000
    ENABLE_INSERT_MODE            = 0b0000100000
    ENABLE_QUICK_EDIT_MODE        = 0b0001000000
    ENABLE_EXTENDED_FLAGS         = 0b0010000000  # NOTE: undocumented
    ENABLE_AUTO_POSITION          = 0b0100000000  # NOTE: undocumented
    ENABLE_VIRTUAL_TERMINAL_INPUT = 0b1000000000
    # fmt: on


class _F_ConsoleModeOutput(enum.IntFlag):
    # fmt: off
    ENABLE_PROCESSED_OUTPUT            = 0b00001
    ENABLE_WRAP_AT_EOL_OUTPUT          = 0b00010
    ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0b00100
    DISABLE_NEWLINE_AUTO_RETURN        = 0b01000
    ENABLE_LVB_GRID_WORLDWIDE          = 0b10000
    # fmt: on


class ConsoleMode(enum.IntFlag):
    """
    TODO
    """

    input = 0b1 << 0
    """
    TODO
    """

    input_processed = _F_ConsoleModeInput.ENABLE_PROCESSED_INPUT << 1
    """
    TODO
    """

    input_line = _F_ConsoleModeInput.ENABLE_LINE_INPUT << 1
    """
    TODO
    """

    input_echo = _F_ConsoleModeInput.ENABLE_ECHO_INPUT << 1
    """
    TODO
    """

    input_window_events = _F_ConsoleModeInput.ENABLE_WINDOW_INPUT << 1
    """
    TODO
    """

    input_mouse_events = _F_ConsoleModeInput.ENABLE_MOUSE_INPUT << 1
    """
    TODO
    """

    input_insert = _F_ConsoleModeInput.ENABLE_INSERT_MODE << 1
    """
    TODO
    """

    input_edit = _F_ConsoleModeInput.ENABLE_QUICK_EDIT_MODE << 1
    """
    TODO
    """

    input_extended_flags = _F_ConsoleModeInput.ENABLE_EXTENDED_FLAGS << 1
    """
    TODO
    """

    input_auto_position = _F_ConsoleModeInput.ENABLE_AUTO_POSITION << 1
    """
    TODO
    """

    input_virtual_terminal_processing = _F_ConsoleModeInput.ENABLE_VIRTUAL_TERMINAL_INPUT << 1
    """
    TODO
    """

    output = 0b1 << 11
    """
    TODO
    """

    output_processed = _F_ConsoleModeOutput.ENABLE_PROCESSED_OUTPUT << 12
    """
    TODO
    """

    output_wrap_at_eol = _F_ConsoleModeOutput.ENABLE_WRAP_AT_EOL_OUTPUT << 12
    """
    TODO
    """

    output_virtual_terminal_processing = _F_ConsoleModeOutput.ENABLE_VIRTUAL_TERMINAL_PROCESSING << 12
    """
    TODO
    """

    output_newline_auto_return = _F_ConsoleModeOutput.DISABLE_NEWLINE_AUTO_RETURN << 12
    """
    TODO
    """

    output_lvb_grid_worldwide = _F_ConsoleModeOutput.ENABLE_LVB_GRID_WORLDWIDE << 12
    """
    TODO
    """


class _E_VirtualKeyCode(enum.Enum):
    # unknown
    LBUTTON = 0x01
    RBUTTON = 0x02
    CANCEL = 0x03
    MBUTTON = 0x04
    XBUTTON1 = 0x05
    XBUTTON2 = 0x06
    # reserved
    BACK = 0x08
    TAB = 0x09
    # reserved
    # reserved
    CLEAR = 0x0C
    RETURN = 0x0D
    # unassigned
    # unassigned
    SHIFT = 0x10
    CONTROL = 0x11
    MENU = 0x12
    PAUSE = 0x13  # TODO: continue from here
    CAPITAL = 0x14
    KANA = HANGUL = 0x15  # TODO: what?
    IME_ON = 0x16  # TODO
    JUNJA = 0x17
    FINAL = 0x18
    HANJA = KANJI = 0x19  # TODO: what?
    IME_OFF = 0x1A  # TODO
    ESCAPE = 0x1B
    CONVERT = 0x1C
    NONCONVERT = 0x1D
    ACCEPT = 0x1E
    MODECHANGE = 0x1F
    SPACE = 0x20
    PRIOR = 0x21
    NEXT = 0x22
    END = 0x23
    HOME = 0x24
    LEFT = 0x25
    UP = 0x26
    RIGHT = 0x27
    DOWN = 0x28
    SELECT = 0x29
    PRINT = 0x2A
    EXECUTE = 0x2B
    SNAPSHOT = 0x2C
    INSERT = 0x2D
    DELETE = 0x2E
    HELP = 0x2F
    ZERO = 0x30  # TODO: consider putting back the VK_ prefix and using VK_0
    ONE = 0x31
    TWO = 0x32
    THREE = 0x33
    FOUR = 0x34
    FIVE = 0x35
    SIX = 0x36
    SEVEN = 0x37
    EIGHT = 0x38
    NINE = 0x39
    # undefined
    # undefined
    # undefined
    # undefined
    # undefined
    # undefined
    # undefined
    A = 0x41
    B = 0x42
    C = 0x43
    D = 0x44
    E = 0x45
    F = 0x46
    G = 0x47
    H = 0x48
    I = 0x49
    J = 0x4A
    K = 0x4B
    L = 0x4C
    M = 0x4D
    N = 0x4E
    O = 0x4F
    P = 0x50
    Q = 0x51
    R = 0x52
    S = 0x53
    T = 0x54
    U = 0x55
    V = 0x56
    W = 0x57
    X = 0x58
    Y = 0x59
    Z = 0x5A
    LWIN = 0x5B
    RWIN = 0x5C
    APPS = 0x5D
    # reserved
    SLEEP = 0x5F
    NUMPAD0 = 0x60
    NUMPAD1 = 0x61
    NUMPAD2 = 0x62
    NUMPAD3 = 0x63
    NUMPAD4 = 0x64
    NUMPAD5 = 0x65
    NUMPAD6 = 0x66
    NUMPAD7 = 0x67
    NUMPAD8 = 0x68
    NUMPAD9 = 0x69
    MULTIPLY = 0x6A
    ADD = 0x6B
    SEPARATOR = 0x6C
    SUBTRACT = 0x6D
    DECIMAL = 0x6E
    DIVIDE = 0x6F
    F1 = 0x70
    F2 = 0x71
    F3 = 0x72
    F4 = 0x73
    F5 = 0x74
    F6 = 0x75
    F7 = 0x76
    F8 = 0x77
    F9 = 0x78
    F10 = 0x79
    F11 = 0x7A
    F12 = 0x7B
    F13 = 0x7C
    F14 = 0x7D
    F15 = 0x7E
    F16 = 0x7F
    F17 = 0x80
    F18 = 0x81
    F19 = 0x82
    F20 = 0x83
    F21 = 0x84
    F22 = 0x85
    F23 = 0x86
    F24 = 0x87
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    NUMLOCK = 0x90
    SCROLL = 0x91
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # unassigned
    # unassigned
    # unassigned
    # unassigned
    # unassigned
    # unassigned
    # unassigned
    # unassigned
    # unassigned
    LSHIFT = 0xA0
    RSHIFT = 0xA1
    LCONTROL = 0xA2
    RCONTROL = 0xA3
    LMENU = 0xA4
    RMENU = 0xA5
    BROWSER_BACK = 0xA6
    BROWSER_FORWARD = 0xA7
    BROWSER_REFRESH = 0xA8
    BROWSER_STOP = 0xA9
    BROWSER_SEARCH = 0xAA
    BROWSER_FAVORITES = 0xAB
    BROWSER_HOME = 0xAC
    VOLUME_MUTE = 0xAD
    VOLUME_DOWN = 0xAE
    VOLUME_UP = 0xAF
    MEDIA_NEXT_TRACK = 0xB0
    MEDIA_PREV_TRACK = 0xB1
    MEDIA_STOP = 0xB2
    MEDIA_PLAY_PAUSE = 0xB3
    LAUNCH_MAIL = 0xB4
    LAUNCH_MEDIA_SELECT = 0xB5
    LAUNCH_APP1 = 0xB6
    LAUNCH_APP2 = 0xB7
    # reserved
    # reserved
    OEM_1 = 0xBA
    OEM_PLUS = 0xBB
    OEM_COMMA = 0xBC
    OEM_MINUS = 0xBD
    OEM_2 = 0xBF
    OEM_3 = 0xC0
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    # reserved
    OEM_4 = 0xDB
    OEM_5 = 0xDC
    OEM_6 = 0xDD
    OEM_7 = 0xDE
    OEM_8 = 0xDF
    # reserved
    # oem-specific
    OEM_102 = 0xE2
    # oem-specific
    # oem-specific
    PROCESSKEY = 0xE5
    # oem-specific
    PACKET = 0xE7
    # unassigned
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    # oem-specific
    ATTN = 0xF6
    CRSEL = 0xF7
    EXSEL = 0xF8
    EREOF = 0xF9
    PLAY = 0xFA
    ZOOM = 0xFB
    # reserved
    PA1 = 0xFD
    OEM_CLEAR = 0xFE
    # unknown


__all__ = [
    "get_console_mode",
    "read_console_input",
    "set_console_mode",
    "ConsoleMode",
    "ConsoleInputEvent",
    "ConsoleInputFocusEvent",
    "ConsoleInputKeyEvent",
    "ConsoleInputMenuEvent",
    "ConsoleInputMouseEvent",
    "ConsoleInputResizeEvent",
]
