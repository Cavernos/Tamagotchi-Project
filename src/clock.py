import threading
from tamagotchi import tamagotchi
from Player import Player
class Clock(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(name=name)
        self.day_duration = 180
        self.tamagotchis = tamagotchi
        self.player = Player("Michel")

    def run(self):
        while self.day_duration:
            
            self.day_duration -= 1

