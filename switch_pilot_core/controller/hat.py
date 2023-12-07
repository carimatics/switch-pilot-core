from enum import IntEnum, auto


class Hat(IntEnum):
    """Hat enum for the Nintendo Switch Controller."""

    TOP = 0
    """Top"""

    TOP_RIGHT = auto()
    """Top Right"""

    RIGHT = auto()
    """Right"""

    BOTTOM_RIGHT = auto()
    """Bottom Right"""

    BOTTOM = auto()
    """Bottom"""

    BOTTOM_LEFT = auto()
    """Bottom Left"""

    LEFT = auto()
    """Left"""

    TOP_LEFT = auto()
    """Top Left"""

    CENTER = auto()
    """Center"""
