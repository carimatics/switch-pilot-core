import math
import os
from typing import Optional

import cv2
from easyocr import easyocr
import numpy as np

from switch_pilot_core.image.region import ImageRegion


class Image:
    def __init__(self, mat: Optional[cv2.typing.MatLike] = None):
        self._mat: Optional[cv2.typing.MatLike] = mat

    @property
    def width(self) -> int:
        return self._mat.shape[1]

    @property
    def height(self) -> int:
        return self._mat.shape[0]

    @staticmethod
    def from_file(file_path: str, use_gray_scale: bool = True) -> 'Image':
        if use_gray_scale:
            flags = cv2.IMREAD_GRAYSCALE
        else:
            flags = cv2.IMREAD_COLOR
        return Image(cv2.imread(filename=file_path, flags=flags))

    def save(self, file_path: str) -> bool:
        ext = os.path.splitext(file_path)[1]
        result, n = cv2.imencode(ext, self._mat)

        if result:
            with open(file_path, mode="w+b") as f:
                n.tofile(f)
        return result

    def roi(self, region: ImageRegion) -> 'Image':
        height, width, _ = self._mat.shape
        x0, x1 = math.ceil(width * region.x[0]), math.ceil(width * region.x[1])
        y0, y1 = math.ceil(height * region.y[0]), math.ceil(height * region.y[1])
        return Image(self._mat[y0:y1, x0:x1])

    def to_gray_scale(self) -> 'Image':
        return Image(cv2.cvtColor(self._mat, cv2.COLOR_BGR2GRAY))

    def contains(self, other: 'Image', threshold: float) -> bool:
        result = cv2.matchTemplate(self._mat, other._mat, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        return max_val >= threshold

    def is_contained_in(self, other: 'Image', threshold: float) -> bool:
        return other.contains(self, threshold)

    def contains_text(self, target_text: str, threshold: float = 0.8, langs: Optional[list[str]] = None) -> bool:
        results = self.detect_text(threshold=threshold, langs=langs)
        for result in results:
            if target_text in result[0]:
                return True
        return False

    def detect_text(self, threshold: float = 0.8, langs: Optional[list[str]] = None) -> list[tuple[str, float]]:
        if langs is None or len(langs) == 0:
            langs = ['ja', 'en']
        reader = easyocr.Reader(langs)
        image_array = np.asarray(self._mat[:, :])
        results = reader.readtext(image=image_array)
        return [(result[1], result[2]) for result in results if result[2] >= threshold]
