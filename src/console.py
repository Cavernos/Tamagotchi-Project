from threading import Event
import logging

import tamagotchi_file

from Player import Player
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
            self.clock.start()
            logging.info("Lancement de la partie")
            self.get_game_info()
        else:
            self.quit()
            
    def get_game_info(self):
        print(f" Vous disposez de {self.player.biscuit} croquettes et nous venons de vous remettre vos tamagotchis.\n" 
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
                self.player.give_biscuit(tamagotchi_file.tamagotchis[int(input("Quelle tamagotchi ? "))])
                self.get_game_info()
            case "q":
                self.quit()
            case "st":
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

