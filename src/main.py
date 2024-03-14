import keyboard
from Game import Game
from Player import Player
from Tamagotchi import Tamagotchi

class Main:
    def __init__(self) -> None:
        pass

game = Game()
game.start()
while True:
    if keyboard.is_pressed("Esc"):
        break
    if game.is_day:
        for tamagotchi in tamagotchis:
            tamagotchi.awake()
    if not game.is_day:
        for tamagotchi in tamagotchis:
            tamagotchi.sleep()
 


