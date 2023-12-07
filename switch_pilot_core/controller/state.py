from typing import Optional

from .button import Button
from .hat import Hat
from .stick import StickDisplacementRange, Stick, StickDisplacement


class ControllerState:
    """ControllerState class for the Nintendo Switch Controller."""

    def __init__(self,
                 buttons=0,
                 hat=Hat.CENTER,
                 lx=StickDisplacementRange.CENTER,
                 ly=StickDisplacementRange.CENTER,
                 rx=StickDisplacementRange.CENTER,
                 ry=StickDisplacementRange.CENTER):
        """ControllerState class for the Nintendo Switch Controller."""

        self._buttons = buttons
        self._hat = hat

        # L stick
        self._l_stick = Stick()
        self._l_stick.x = lx
        self._l_stick.y = ly

        # R stick
        self._r_stick = Stick()
        self._r_stick.x = rx
        self._r_stick.y = ry

    @property
    def buttons(self):
        """Get buttons"""
        return self._buttons

    @property
    def hat(self):
        """Get hat"""
        return self._hat

    @property
    def l_stick(self):
        """Get left stick"""
        return self._l_stick

    @property
    def r_stick(self):
        """Get right stick"""
        return self._r_stick

    @property
    def lx(self):
        """Get left stick x-axis value"""
        return self._l_stick.x

    @lx.setter
    def lx(self, new_value: int):
        """Set left stick x-axis value"""
        self._l_stick.x = new_value

    @property
    def ly(self):
        """Get left stick y-axis value"""
        return self._l_stick.y

    @ly.setter
    def ly(self, new_value: int):
        """Set left stick y-axis value"""
        self._l_stick.y = new_value

    @property
    def rx(self):
        """Get right stick x-axis value"""
        return self._r_stick.x

    @rx.setter
    def rx(self, new_value: int):
        """Set right stick x-axis value"""
        self._r_stick.x = new_value

    @property
    def ry(self):
        """Get right stick y-axis value"""
        return self._r_stick.y

    @ry.setter
    def ry(self, new_value: int):
        """Set right stick y-axis value"""
        self._r_stick.y = new_value

    def set(self,
            buttons: Optional[list[Button]] = None,
            l_displacement: Optional[StickDisplacement] = None,
            r_displacement: Optional[StickDisplacement] = None,
            hat: Optional[Hat] = None):
        """Set buttons, sticks and hat state"""
        if buttons is not None:
            for button in buttons:
                self._buttons |= button

        if l_displacement is not None:
            self._l_stick.set_displacement(l_displacement)
        if r_displacement is not None:
            self._r_stick.set_displacement(r_displacement)

        if hat is not None:
            self._hat = hat

    def unset(self,
              buttons: Optional[list[Button]] = None,
              hat: bool = False):
        """Unset buttons and hat state"""
        if buttons is not None:
            for button in buttons:
                self._buttons &= ~button
        if hat:
            self._hat = Hat.CENTER

    def reset_buttons(self):
        """Reset buttons state."""
        self._buttons = 0

    def reset_stick_displacement(self):
        """Reset sticks state."""
        self._l_stick.reset()
        self._r_stick.reset()

    def consume_stick_displacement(self):
        """Consume sticks state."""
        self._l_stick.consume()
        self._r_stick.consume()

    def reset_hat(self):
        """Reset hat state."""
        self._hat = Hat.CENTER

    def reset(self):
        """Reset all state."""
        self.reset_buttons()
        self.reset_stick_displacement()
        self.reset_hat()

    def copy(self):
        """Copy state."""
        return ControllerState(buttons=self.buttons,
                               hat=self.hat,
                               lx=self.l_stick.x,
                               ly=self.l_stick.y,
                               rx=self.r_stick.x,
                               ry=self.r_stick.y)
