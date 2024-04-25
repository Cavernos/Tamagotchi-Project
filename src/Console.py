import threading
import time
import argparse
from clock import Clock
class Console:
    def __init__(self):
        self.player = Player("")
        self.clock = Clock(name="day_clock", player=player)

    def interaction(self):
        while True:
            action = input("Bonjour et bienvenue dans le jeu Tamagotchi, souhaitez-vous commencer? (oui/non) ")

            if action == "non":
                print("Vous quittez le jeu, en espérant vous revoir bientôt")
                break

            elif action == "oui":
                input("Vous disposez de 50 croquettes et nous venons de vous remettre vos Tamagotchis.\n"
                      "Vous pouvez réaliser les actions suivantes:\n"
                      "S – Afficher le statut des Tamagotchis\n"
                      "N – Nourrir un Tamagotchi (Cela coûte une croquette)\n"
                      "J – Jouer avec l’un des Tamagotchis\n"
                      "Q – Quitter le jeu ")
                break

            else:
                print("Je n'ai pas compris votre réponse. Veuillez répondre par 'oui' ou 'non'.")

    def start(self):
        pass