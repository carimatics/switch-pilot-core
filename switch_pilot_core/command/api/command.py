from switch_pilot_core.camera import Camera
from switch_pilot_core.config import Config
from switch_pilot_core.controller import Controller
from switch_pilot_core.logger import Logger
from switch_pilot_core.path import Path
from switch_pilot_core.timer import Timer

from .config import CommandConfigAPI
from .extensions import CommandExtensionsAPI
from .image import CommandImageAPI
from .timer import CommandTimerAPI
from .video import CommandVideoAPI


class CommandAPI:
    def __init__(self,
                 name: str,
                 logger: Logger,
                 controller: Controller,
                 config: Config,
                 camera: Camera,
                 path: Path,
                 timer: Timer):
        self._name = name
        self._config = CommandConfigAPI(config=config, command=name)
        self._controller = controller
        self._video = CommandVideoAPI(camera=camera, path=path)
        self._image = CommandImageAPI(path=path, command=name)
        self._timer = CommandTimerAPI(timer=timer)
        self._logger = logger
        self._extensions = CommandExtensionsAPI(camera=camera, path=path, controller=controller)

    @property
    def name(self) -> str:
        return self._name

    @property
    def config(self) -> CommandConfigAPI:
        return self._config

    @property
    def controller(self) -> Controller:
        return self._controller

    @property
    def video(self) -> CommandVideoAPI:
        return self._video

    @property
    def image(self) -> CommandImageAPI:
        return self._image

    @property
    def logger(self) -> Logger:
        return self._logger

    @property
    def timer(self) -> CommandTimerAPI:
        return self._timer

    @property
    def extensions(self) -> CommandExtensionsAPI:
        return self._extensions
