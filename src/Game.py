import threading
import time
import random

# dev Cavernos
class Game(threading.Thread):
    def __init__(self) -> None:
        threading.Thread.__init__(self)
        self._total_day_duration = 180
        self._night_duration = 0
        self._day_duration = 0
        self._is_day = False
        self._running = False

    def day(self) -> None:
        self._night_duration = random.randint(30, 60)
        self._day_duration = self._total_day_duration - self._night_duration
        while self._day_duration:
            self._is_day = True
            time.sleep(1)
            self._day_duration -= 1
        while self._night_duration:
            self._is_day = False
            time.sleep(1)
            self._night_duration -= 1
        

    def run(self) -> None:
        self._running = True
        while True:
            self.day()
            if not self._running:
                break


    @property
    def is_day(self) -> bool:
        return self._is_day
    
    @property
    def running(self) -> bool:
        return self._running

    @running.setter
    def running(self, value) -> None:
        self._running = value

