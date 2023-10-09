import _tkinter
import tkinter as tk
from tkinter.font import *
from typing import Any, Callable, Optional, Union, Mapping
from typing_extensions import Literal

_FontDescription = Union[
    # "Helvetica 12"
    str,
    # A font object constructed in Python
    Font,
    # ("Helvetica", 12, BOLD)
    list[Any],
    tuple[Any, ...],
    # A font object constructed in Tcl
    _tkinter.Tcl_Obj,
]


_Anchor = Literal["nw", "n", "ne", "w", "center", "e", "sw", "s", "se"]  # manual page: Tk_GetAnchor
_Bitmap = str  # manual page: Tk_GetBitmap
_ButtonCommand = Union[str, Callable[[], Any]]  # accepts string of tcl code, return value is returned from Button.invoke()
_CanvasItemId = int
_Color = str  # typically '#rrggbb', '#rgb' or color names.
_Compound = Literal["top", "left", "center", "right", "bottom", "none"]  # -compound in manual page named 'options'
_Cursor = Union[str, tuple[str], tuple[str, str], tuple[str, str, str], tuple[str, str, str, str]]  # manual page: Tk_GetCursor
_EntryValidateCommand = Union[
    Callable[[], bool], str, list[str], tuple[str, ...]
]  # example when it's sequence:  entry['invalidcommand'] = [entry.register(print), '%P']
_GridIndex = Union[int, str, Literal["all"]]
_Padding = Union[
    _ScreenUnits,
    tuple[_ScreenUnits],
    tuple[_ScreenUnits, _ScreenUnits],
    tuple[_ScreenUnits, _ScreenUnits, _ScreenUnits],
    tuple[_ScreenUnits, _ScreenUnits, _ScreenUnits, _ScreenUnits],
]
_Relief = Literal["raised", "sunken", "flat", "ridge", "solid", "groove"]  # manual page: Tk_GetRelief
_ScreenUnits = Union[str, float]  # Often the right type instead of int. Manual page: Tk_GetPixels
_XYScrollCommand = Union[str, Callable[[float, float], Any]]  # -xscrollcommand and -yscrollcommand in 'options' manual page
_TakeFocusValue = Union[int, Literal[""], Callable[[str], Optional[bool]]]  # -takefocus in manual page named 'options'





class Entry:
    def __init__(self,
                 master: tk.Misc | None = ...,
                 cnf: dict[str, Any] | None = ...,
                 *,
                 background: _Color = ...,
                 bd: _ScreenUnits = ...,
                 bg: _Color = ...,
                 border: _ScreenUnits = ...,
                 borderwidth: _ScreenUnits = ...,
                 cursor: _Cursor = ...,
                 disabledbackground: _Color = ...,
                 disabledforeground: _Color = ...,
                 exportselection: bool = ...,
                 fg: _Color = ...,
                 font: _FontDescription = ...,
                 foreground: _Color = ...,
                 highlightbackground: _Color = ...,
                 highlightcolor: _Color = ...,
                 highlightthickness: _ScreenUnits = ...,
                 insertbackground: _Color = ...,
                 insertborderwidth: _ScreenUnits = ...,
                 insertofftime: int = ...,
                 insertontime: int = ...,
                 insertwidth: _ScreenUnits = ...,
                 invalidcommand: _EntryValidateCommand = ...,
                 invcmd: _EntryValidateCommand = ...,  # same as invalidcommand
                 justify: Literal["left", "center", "right"] = ...,
                 name: str = ...,
                 readonlybackground: _Color = ...,
                 relief: _Relief = ...,
                 selectbackground: _Color = ...,
                 selectborderwidth: _ScreenUnits = ...,
                 selectforeground: _Color = ...,
                 show: str = ...,
                 state: Literal["normal", "disabled", "readonly"] = ...,
                 takefocus: _TakeFocusValue = ...,
                 textvariable: tk.Variable = ...,
                 validate: Literal["none", "focus", "focusin", "focusout", "key", "all"] = ...,
                 validatecommand: _EntryValidateCommand = ...,
                 vcmd: _EntryValidateCommand = ...,  # same as validatecommand
                 width: int = ...,
                 xscrollcommand: _XYScrollCommand = ...,
                 ) -> None:
        self.entry = None
        ...

    def pack(
        self,
        cnf: Mapping[str, Any] | None = ...,
        *,
        after: tk.Misc = ...,
        anchor: _Anchor = ...,
        before: tk.Misc = ...,
        expand: int = ...,
        fill: Literal["none", "x", "y", "both"] = ...,
        side: Literal["left", "right", "top", "bottom"] = ...,
        ipadx: _ScreenUnits = ...,
        ipady: _ScreenUnits = ...,
        padx: _ScreenUnits | tuple[_ScreenUnits, _ScreenUnits] = ...,
        pady: _ScreenUnits | tuple[_ScreenUnits, _ScreenUnits] = ...,
        in_: tk.Misc = ...,
        **kw: Any,  # allow keyword argument named 'in', see #4836
    ) -> None: ...