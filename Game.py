import random
import time


class Game:
    def __init__(self, day_duration: float = 180, night_duration: float = random.randint(30, 60)):
        self._day_duration = day_duration
        self._night_duration = night_duration

    def is_day(self):
        while self._day_duration:
            time.sleep(1)
            self._day_duration -= 1

