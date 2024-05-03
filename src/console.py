from threading import Event
import logging
import os
import keyboard

from config import CARACTERISTICS_INITIAL_VALUE, NUMBER_OF_TAMAGOTCHI
import models.tamagotchi_file as tamagotchi_file

from models.player import Player
from clock import Clock
from game_saver import GameSaver

class Console:
    def __init__(self):
        self.event = Event()
        self.clock = Clock("console_game", self.event)
        self.player = Player("Michel")
    
    def start(self):
        action = input("Bonjour et bienvenue dans le jeu tamagotchi, voulez vous commencer ? (Oui/Non) ")
        if action == "Oui":
            self.create_game_info()
            self.clock.start()
            logging.info("Lancement de la partie")
            self.get_game_info()
        else:
            self.quit()

    def create_game_info(self):
        self.player = Player(name=input("Choisissez un nom ? "))
        tamagotchi_names = []
        i = 0
        while len(tamagotchi_names) < NUMBER_OF_TAMAGOTCHI:
            name = input(f"Choisissez un nom pour le {i+1}{"er" if i == 0 else "e"} tamagotchi ")
            if name in tamagotchi_names:
                logging.info("Deux tamagotchis ne peuvent avoir le même nom")
                print("Attention, Deux tamagotchis ne peuvent avoir le même nom")
            else:
                tamagotchi_names.append(name)
                i +=1

                
        for element in tamagotchi_file.tamagotchis:
            element["name"] = tamagotchi_names[tamagotchi_file.tamagotchis.index(element)]
        

        
    def get_game_info(self):
        print(f" Vous disposez de {self.player.biscuits} croquettes et nous venons de vous remettre vos tamagotchis.\n" 
                " Vous pouvez réalisez les actions suivante:\n" 
                " S - Afficher le statut des tamagotchis\n" 
                " N - Nourrir un tamagotchi (Cela coûte une croquette)\n" 
                " J - Jouer avec l'un des tamagotchis\n" 
                " Q - Quitter le jeu"
                )
        action = input("Quelle est votre action ? ")
        match action.lower():
            case "s":
                self.save()
            case "n":
                name_of_tamagotchi = input("Quelle tamagotchi ? (name)")
                for tamagotchi in tamagotchi_file.tamagotchis:
                    if tamagotchi["name"] == name_of_tamagotchi:
                        id_of_tamagotchi = tamagotchi_file.tamagotchis.index(tamagotchi)
                        break
                self.player.give_biscuit(tamagotchi_file.tamagotchis[id_of_tamagotchi])
                self.get_game_info()
            case "q":
                self.quit()
            case "st":
                while not keyboard.is_pressed('q'):
                    os.system('cls')
                    tamagotchi_file.print_status(tamagotchi_file.get_status(tamagotchi_file.tamagotchis))
                self.get_game_info()


    
    def save(self):
        logging.info("Sauvegarde du Jeu")
        self.event.set()
        self.clock.join()
        game_saver = GameSaver("")
        game_saver.save(tamagotchis=self.clock.tamagotchis, player=self.player.__dict__, game_time=self.clock.game_time)
        logging.debug(f"saved data : {game_saver.save_data}")
    
    def quit(self, quit_message= "Fin de la partie"):
        if self.clock.is_alive():
            self.event.set()
            self.clock.join()
        logging.info(quit_message)
        exit(0)

