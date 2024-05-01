import threading
import tamagotchi
from config import DAY_DURATION
import time


class Clock(threading.Thread):
    def __init__(self, name: str = "") -> None:
        threading.Thread.__init__(self, name=name)
        self.day_duration = DAY_DURATION
        self.tamagotchis = tamagotchi.tamagotchis
        self.game_time = [0, 0]

    def run(self) -> None:
        while self.day_duration:
            for element in self.tamagotchis:
                if tamagotchi.battle(element):
                    tamagotchi.is_in_battle(self.tamagotchis)
                if tamagotchi.die(element):
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

    def calc_game_time(self):
        self.game_time[1] += (24*60) // DAY_DURATION
        if self.game_time[1] >= 60:
            self.game_time[0] += 1
            self.game_time[1] = self.game_time[1] % 60
        if self.game_time[0] >= 24:
            self.game_time[0] = 0

    def print_time(self):
        print(f"{"0" if self.game_time[0] < 10 else ""}{self.game_time[0]}:{"0" if self.game_time[1] < 10 else ""}{self.game_time[1]}")