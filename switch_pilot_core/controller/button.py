from enum import IntFlag, auto


class Button(IntFlag):
    """Button enum for the Nintendo Switch Controller."""

    Y = auto()
    """Y Button"""

    B = auto()
    """B Button"""

    A = auto()
    """A Button"""

    X = auto()
    """X Button"""

    L = auto()
    """L Shoulder Button"""

    R = auto()
    """R Shoulder Button"""

    ZL = auto()
    """ZL Shoulder Button"""

    ZR = auto()
    """ZR Shoulder Button"""

    MINUS = auto()
    """Minus Button"""

    PLUS = auto()
    """Plus Button"""

    L_CLICK = auto()
    """Left Stick Click"""

    R_CLICK = auto()
    """Right Stick Click"""

    HOME = auto()
    """Home Button"""

    CAPTURE = auto()
    """Capture Button"""
