import math
from enum import IntEnum
from typing import Optional


class StickDisplacementRange(IntEnum):
    """Stick displacement range enum for the Nintendo Switch Controller."""

    MIN = 0
    """Minimum value"""

    CENTER = 128
    """Center value"""

    MAX = 255
    """Maximum value"""


class StickDisplacement:
    """Stick displacement class for the Nintendo Switch Controller."""

    def __init__(self, angle: float, magnification: float = 1.0):
        """Stick displacement class for the Nintendo Switch Controller."""

        magnification = self._clamp_magnification(magnification)
        if magnification == 0.0:
            center = StickDisplacementRange.CENTER
            self.x, self.y = center, center
        else:
            self.x, self.y = self._calculate_xy(self._clamp_angle(angle), magnification)

    @property
    def x(self):
        """Get x-axis value"""
        return self._x

    @x.setter
    def x(self, new_value: int):
        """Set x-axis value"""
        self._x = new_value

    @property
    def y(self):
        """Get y-axis value"""
        return self._y

    @y.setter
    def y(self, new_value: int):
        """Set y-axis value"""
        self._y = new_value

    @staticmethod
    def _clamp_angle(angle: float) -> float:
        return angle % 360

    @staticmethod
    def _clamp_magnification(magnification: float):
        if magnification < 0.0:
            return 0.0
        elif magnification > 1.0:
            return 1.0
        else:
            return magnification

    @staticmethod
    def _calculate_xy(angle: float, magnification: float) -> tuple[int, int]:
        max_range = StickDisplacementRange.MAX
        rad = math.radians(angle)
        x = math.ceil(127.5 * math.cos(rad) * magnification + 127.5)
        y = max_range - math.ceil(127.5 * math.sin(rad) * magnification + 127.5)
        return x, y


class Stick:
    """Stick class for the Nintendo Switch Controller."""

    def __init__(self,
                 displacement: Optional[StickDisplacement] = None,
                 x: Optional[int] = None,
                 y: Optional[int] = None):
        """Stick class for the Nintendo Switch Controller."""

        if x is not None and y is not None:
            self._x, self._y = x, y
        elif displacement is None:
            center = StickDisplacementRange.CENTER
            self._x, self._y = center, center
        else:
            self.set_displacement(displacement)
        self._changed = False

    @property
    def x(self):
        """Get x-axis value"""
        return self._x

    @x.setter
    def x(self, new_value: int):
        """Set x-axis value and set changed flag to True"""
        self._x = new_value
        self._changed = True

    @property
    def y(self):
        """Get y-axis value"""
        return self._y

    @y.setter
    def y(self, new_value: int):
        """Set y-axis value and set changed flag to True"""
        self._y = new_value
        self._changed = True

    @property
    def changed(self):
        """Get if changed"""
        return self._changed

    def consume(self):
        """Consume changed flag"""
        self._changed = False

    def set_displacement(self, displacement: StickDisplacement):
        """Set x and y value by displacement"""
        if self.x != displacement.x or self.y != displacement.y:
            self.x, self.y = displacement.x, displacement.y
            self._changed = True

    def reset(self):
        """Reset x and y value to center"""
        center = StickDisplacementRange.CENTER
        if self.x != center or self.y != center:
            self.x, self.y = center, center
            self._changed = True


class StickDisplacementPreset:
    """Stick displacement presets for the Nintendo Switch Controller."""

    CENTER = StickDisplacement(angle=0, magnification=0.0)
    """Center"""

    RIGHT = StickDisplacement(angle=0)
    """Right"""

    TOP_RIGHT = StickDisplacement(angle=45)
    """Top Right"""

    TOP = StickDisplacement(angle=90)
    """Top"""

    TOP_LEFT = StickDisplacement(angle=135)
    """Top Left"""

    LEFT = StickDisplacement(angle=180)
    """Left"""

    BOTTOM_LEFT = StickDisplacement(angle=215)
    """Bottom Left"""

    BOTTOM = StickDisplacement(angle=270)
    """Bottom"""

    BOTTOM_RIGHT = StickDisplacement(angle=315)
    """Bottom Right"""
