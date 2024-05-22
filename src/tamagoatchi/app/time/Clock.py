import logging
import threading
import tamagoatchi.app.models.tamagotchi_file as tamagotchi_file
from threading import Event
from tamagoatchi.app.definitions import DAY_DURATION
import time

from tamagoatchi.lib.model import Model


class Clock(threading.Thread, Model):
    """
       A classed used to represent the Time
       ...

        Attributes
        ----------
        name : str
           the name of the thread
        day_duration : int
            the clock duration
        tamagotchis : list[dict]
            a list of tamagotchis
        game_time : list
            a list of minutes and hours
        statement : str
            reason why the thread was stopped
       """

    def __init__(self, name: str) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the thread
        """
        threading.Thread.__init__(self, name=name, daemon=True)
        self.day_duration = DAY_DURATION
        self.tamagotchis = tamagotchi_file.tamagotchis
        self.event = Event()
        self._days = 0
        self.game_time = [0, 0]

    def run(self) -> None:
        """
        Run method (principal thread function) verify condition and execute tamagotch's method
        """
        while self.day_duration:
            if self.event.is_set():
                return
            for element in self.tamagotchis:
                if tamagotchi_file.battle(element):
                    tamagotchi_file.is_in_battle(self.tamagotchis)
                if tamagotchi_file.die(element):
                    return
                if self.day_duration <= element["night_duration"]:
                    tamagotchi_file.sleep_zzz(element)
                else:
                    tamagotchi_file.awake(element)
            time.sleep(1)
            self.calc_game_time()
            self.day_duration -= 1

        for element in self.tamagotchis:
            tamagotchi_file.night_duration(element)
        self.day_duration = DAY_DURATION
        self._days += 1
        self.run()

    def calc_game_time(self):
        """
        Calculation of the game time in 24 hour bases
        """
        self.game_time[1] += (24 * 60) // DAY_DURATION
        if self.game_time[1] >= 60:
            self.game_time[0] += 1
            self.game_time[1] = self.game_time[1] % 60
        if self.game_time[0] >= 24:
            self.game_time[0] = 0

    def print_time(self):
        """
        Print Time is a time printer
        """
        print(
            f"{"0" if self.game_time[0] < 10 else ""}{self.game_time[0]}:{"0" if self.game_time[1] < 10 else ""}{self.game_time[1]}")

    def stop(self):
        self.event.set()
        return str(self.day_duration)

    @property
    def days(self) -> int:
        return self._days
