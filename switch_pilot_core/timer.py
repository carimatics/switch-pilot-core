import time
from dataclasses import dataclass
from typing import Optional


@dataclass
class ElapsedTime:
    hours: int
    minutes: int
    seconds: int


class Timer:
    def __init__(self):
        self._start_time: Optional[float] = None
        self._stop_time: Optional[float] = None

    def start(self):
        self._start_time = self._get_current_time()

    def stop(self):
        self._stop_time = self._get_current_time()

    @property
    def elapsed_time(self) -> Optional[ElapsedTime]:
        start_time = self._start_time
        stop_time = self._stop_time

        if start_time is None:
            return None

        if stop_time is None or stop_time < start_time:
            end_time = self._get_current_time()
        else:
            end_time = stop_time

        elapsed_time_in_seconds = end_time - start_time

        hours = int(elapsed_time_in_seconds / (60 * 60))
        minutes = int((elapsed_time_in_seconds / 60) % 60)
        seconds = int(elapsed_time_in_seconds % 60)

        return ElapsedTime(hours=hours,
                           minutes=minutes,
                           seconds=seconds)

    @staticmethod
    def _get_current_time():
        return time.time()
