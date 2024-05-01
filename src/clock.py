import threading
import tamagotchi
from config import DAY_DURATION
import time


class Clock(threading.Thread):
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
    def __init__(self, name: str = "") -> None:
        """
        Parameters
        ----------
        name : str
            The name of the thread
        """
        threading.Thread.__init__(self, name=name)
        self.day_duration = DAY_DURATION
        self.tamagotchis = tamagotchi.tamagotchis
        self.statement = ""
        self.game_time = [0, 0]

    def run(self) -> None:
        """
        Run method (principal thread function) verify condition and execute tamagotch's method
        """
        while self.day_duration:
            for element in self.tamagotchis:
                if tamagotchi.battle(element):
                    tamagotchi.is_in_battle(self.tamagotchis)
                if tamagotchi.die(element):
                    self.statement = "Le tamagotchi est mort"
                    print("le tamagotchi est mort")  # TODO Replace with option
                    return
                if self.day_duration <= element["night_duration"]:
                    tamagotchi.sleep_zzz(element)
                else:
                    tamagotchi.awake(element)
            self.calc_game_time()
            time.sleep(1)
            self.day_duration -= 1
        for element in self.tamagotchis:
            tamagotchi.night_duration(element)
        self.statement = "Fin de la journée"

    def calc_game_time(self):
        """
        Calculation of the game time in 24 hour bases
        """
        self.game_time[1] += (24*60) // DAY_DURATION
        if self.game_time[1] >= 60:
            self.game_time[0] += 1
            self.game_time[1] = self.game_time[1] % 60
        if self.game_time[0] >= 24:
            self.game_time[0] = 0

    def print_time(self):
        """
        Print Time is a time printer
        """
        print(f"{"0" if self.game_time[0] < 10 else ""}{self.game_time[0]}:{"0" if self.game_time[1] < 10 else ""}{self.game_time[1]}")