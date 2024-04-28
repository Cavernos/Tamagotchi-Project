import threading
import tamagotchi
from config import DAY_DURATION
import time


class Clock(threading.Thread):
    def __init__(self, name) -> None:
        threading.Thread.__init__(self, name=name)
        self.day_duration = DAY_DURATION
        self.tamagotchis = tamagotchi.tamagotchis

    def run(self) -> None:
        for element in self.tamagotchis:
            tamagotchi.night_duration(element)
        while self.day_duration:
            for element in self.tamagotchis:
                if tamagotchi.battle(element):
                    tamagotchi.is_in_battle(self.tamagotchis)
                if tamagotchi.die(element):
                    return
                if self.day_duration <= element["night_duration"]:
                    tamagotchi.sleep_zzz(element)
                tamagotchi.awake(element) 
            time.sleep(1)       
            self.day_duration -= 1

    