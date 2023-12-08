from typing import Optional

from easyocr import easyocr

from switch_pilot_core.image import Image, ImageRegion
from switch_pilot_core.path import Path


class CommandImageAPI:
    def __init__(self, command: str, path: Path):
        self._command = command
        self._path = path

    def read_template(self, name: str, use_gray_scale: bool = True) -> Image:
        path = self._path.template(command=self._command, name=name)
        return Image.from_file(file_path=path, use_gray_scale=use_gray_scale)

    @staticmethod
    def create_text_reader(langs: Optional[list[str]] = None) -> easyocr.Reader:
        return Image.get_text_reader(langs=langs)

    @staticmethod
    def create_region(x: tuple[float, float], y: tuple[float, float]) -> ImageRegion:
        return ImageRegion(x=x, y=y)
