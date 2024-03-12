import random
import threading
import time


class Game(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self._total_day_duration = 180
        self._night_duration = random.randint(30, 60)
        self._day_duration = self._total_day_duration - self._night_duration
        self._is_day = False

    def day(self) -> None:
        while self._day_duration:
            self._is_day = True
            time.sleep(1)
            self._day_duration -= 1
        self._is_day = False

    def run(self):
        self.day()

    @property
    def is_day(self):
        return self._is_day
