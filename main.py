import inspect

from Game import Game
from Player import Player
from Tamagotchi import Tamagotchi
import threading


class Thread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        game.day()


player = Player("Ten", 2)
tamagotchi = Tamagotchi("Michel")


def show_info() -> str:
    return f" Name : {tamagotchi.name} \n Health : {tamagotchi.health} \n Hunger : {tamagotchi.hunger} \n Boredom : {tamagotchi.boredom} \n Tiredness : {tamagotchi.tiredness} \n"


def main():
    print(show_info())
    action = int(input("Que voulez vous faire ? Donner à manger 1 ou Jouer 2 \n"
                       f"Vos croquettes : {player.biscuit} \n"))
    match action:
        case 1:
            if player.biscuit > 0:
                tamagotchi.feed(player)
            else:
                print("Vous n'avez plus de croquette")
        case 2:
            tamagotchi.play()
    return main()


game = Game()
m = Thread()
m.start()
