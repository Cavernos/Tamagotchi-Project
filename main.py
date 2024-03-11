import inspect

from Player import Player
from Tamagotchi import Tamagotchi

player = Player("Ten")
tamagotchi = Tamagotchi("Michel")


def show_info() -> str:
       return f" Name : {tamagotchi.name} \n Health : {tamagotchi.health} \n Hunger : {tamagotchi.hunger} \n Boredom : {tamagotchi.boredom} \n Tiredness : {tamagotchi.tiredness} \n"


action = int(input("Que voulez vous faire ? Donner à manger 1 ou Jouer 2 \n"))
print(show_info())
match action:
      case 1:
            tamagotchi.feed(player)
      case 2:
            tamagotchi.play()
print(show_info())
