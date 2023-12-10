from abc import ABCMeta, abstractmethod
from typing import Any, Optional

from switch_pilot_core.controller import Controller, Button, Hat, StickDisplacementPreset
from switch_pilot_core.image import ImageRegion
from switch_pilot_core.logger import Logger
from switch_pilot_core.timer import ElapsedTime
from .api import CommandAPI, CommandExtensionsAPI, CommandImageAPI, CommandTimerAPI, CommandVideoAPI


class CommandCancellationError(Exception):
    pass


def check_should_keep_running(f):
    def wrapper(*args):
        self = args[0]
        result = f(*args)
        if not self.should_keep_running:
            raise CommandCancellationError
        return result

    return wrapper


class BaseCommand(metaclass=ABCMeta):
    def __init__(self, api: CommandAPI):
        self._api = api
        self.text_reader = None
        self.should_keep_running = False
        self.is_alive = False

    @property
    def should_exit(self):
        return not self.should_keep_running

    @property
    def api(self) -> CommandAPI:
        return self._api

    @property
    def name(self) -> str:
        return self.api.name

    @property
    def config(self) -> Any:
        return self.api.config.read()

    @property
    def controller(self) -> Controller:
        return self.api.controller

    @property
    def video(self) -> CommandVideoAPI:
        return self.api.video

    @property
    def image(self) -> CommandImageAPI:
        return self.api.image

    @property
    def logger(self) -> Logger:
        return self.api.logger

    @property
    def timer(self) -> CommandTimerAPI:
        return self.api.timer

    @property
    def extensions(self) -> CommandExtensionsAPI:
        return self.api.extensions

    @property
    def attempt_count(self) -> int:
        return self.extensions.attempt_count

    @property
    def elapsed_time(self) -> ElapsedTime:
        return self.timer.elapsed_time

    @abstractmethod
    def process(self):
        raise NotImplementedError

    def preprocess(self):
        self.api.extensions.prepare(self)
        self.timer.start()
        self.text_reader = self.image.create_text_reader()
        self.should_keep_running = True
        self.is_alive = True

    def postprocess(self):
        self.should_keep_running = False
        self.is_alive = False

    def stop(self):
        self.should_keep_running = False

    def send_a(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.A],
                                      duration=duration)
        self.wait(duration=wait)

    def send_b(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.B],
                                      duration=duration)
        self.wait(duration=wait)

    def send_x(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.X],
                                      duration=duration)
        self.wait(duration=wait)

    def send_y(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.Y],
                                      duration=duration)
        self.wait(duration=wait)

    def send_l(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.L],
                                      duration=duration)
        self.wait(duration=wait)

    def send_r(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.R],
                                      duration=duration)
        self.wait(duration=wait)

    def send_zl(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.ZL],
                                      duration=duration)
        self.wait(duration=wait)

    def send_zr(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.ZR],
                                      duration=duration)
        self.wait(duration=wait)

    def send_plus(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.PLUS],
                                      duration=duration)
        self.wait(duration=wait)

    def send_minus(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.MINUS],
                                      duration=duration)
        self.wait(duration=wait)

    def send_home(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.HOME],
                                      duration=duration)
        self.wait(duration=wait)

    def send_capture(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(buttons=[Button.CAPTURE],
                                      duration=duration)
        self.wait(duration=wait)

    def send_hat_top(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(hat=Hat.TOP,
                                      duration=duration)
        self.wait(duration=wait)

    def send_hat_bottom(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(hat=Hat.BOTTOM,
                                      duration=duration)
        self.wait(duration=wait)

    def send_hat_left(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(hat=Hat.LEFT,
                                      duration=duration)
        self.wait(duration=wait)

    def send_hat_right(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(hat=Hat.RIGHT,
                                      duration=duration)
        self.wait(duration=wait)

    def send_right(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(l_displacement=StickDisplacementPreset.RIGHT,
                                      duration=duration)
        self.wait(duration=wait)

    def send_left(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(l_displacement=StickDisplacementPreset.LEFT,
                                      duration=duration)
        self.wait(duration=wait)

    def send_up(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(l_displacement=StickDisplacementPreset.TOP,
                                      duration=duration)
        self.wait(duration=wait)

    def send_down(self, duration: float = 0.1, wait: float = 0.1):
        self.controller.send_one_shot(l_displacement=StickDisplacementPreset.BOTTOM,
                                      duration=duration)
        self.wait(duration=wait)

    def screenshot(self, region: Optional[ImageRegion] = None, wait: float = 0.1):
        self.video.capture(region=region)
        self.wait(duration=wait)

    def time_leap(self,
                  years: int = 0,
                  months: int = 0,
                  days: int = 0,
                  hours: int = 0,
                  minutes: int = 0,
                  toggle_auto: bool = False,
                  with_reset: bool = False):
        self.extensions.time_leap(years=years,
                                  months=months,
                                  days=days,
                                  hours=hours,
                                  minutes=minutes,
                                  toggle_auto=toggle_auto,
                                  with_reset=with_reset)

    @check_should_keep_running
    def attempt(self):
        self.extensions.attempt()

    def wait(self, duration: float, check_interval: float = 1.0):
        self.extensions.wait(duration=duration,
                             check_interval=check_interval)

    @check_should_keep_running
    def goto_home(self):
        self.extensions.goto_home()

    def guide_contains_text(self, text: str, threshold: float = 0.9) -> bool:
        region = self.image.create_region(x=(0.25, 0.651), y=(0.022, 0.063))
        return self.contains_text(text=text, region=region, threshold=threshold)

    def textbox_contains_text(self, text: str, threshold: float = 0.9) -> bool:
        region = self.image.create_region(x=(0.27, 0.72), y=(0.76, 0.87))
        return self.contains_text(text=text, region=region, threshold=threshold)

    def contains_text(self, text: str, region: ImageRegion = None, threshold: float = 0.9) -> bool:
        return self.video.get_current_frame(region=region).contains_text(text,
                                                                         reader=self.text_reader,
                                                                         threshold=threshold)

    def detect_guide_text(self, threshold: float = 0.9):
        region = self.image.create_region(x=(0.25, 0.651), y=(0.022, 0.063))
        return self.detect_text(region=region, threshold=threshold)

    def detect_textbox_text(self, threshold: float = 0.9):
        region = self.image.create_region(x=(0.27, 0.72), y=(0.76, 0.87))
        return self.detect_text(region=region, threshold=threshold)

    def detect_text(self, region: ImageRegion = None, threshold: float = 0.9):
        return self.video.get_current_frame(region=region).detect_text(reader=self.text_reader,
                                                                       threshold=threshold)

    def get_recognition(self, buttons: Optional[list[Button]] = None):
        if buttons is None:
            self.extensions.get_recognition(buttons=[Button.ZL])
        else:
            self.extensions.get_recognition(buttons=buttons)

    @check_should_keep_running
    def restart_sv(self):
        self.extensions.restart_sv()
