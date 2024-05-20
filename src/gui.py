# dev Nicolas

# import
import pygame
import pytmx
import pyscroll
import re

from threading import Event

import pytmx.util_pygame
from clock import Clock
from models.player import Player
from button import Button
import tamagotchi


class Gui:
    def __init__(self):
        self.event = Event()
        self.clock = Clock("console_game", self.event)
        self.player = Player("John") 
        self.buttons = []
        self.name_map = "map_maison"
        self.ratio = 16 / 9
        self.height = 576
        self.width = int(self.height * self.ratio)
        self.zoom = 4

        # screen
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("TamaGOATchi")
        game_icon = pygame.image.load('./assets/tamagotchis/default.png')
        pygame.display.set_icon(game_icon)

        # Jouer la musique de fond
        pygame.mixer.music.load("./assets/sound/main_theme.mp3")
        pygame.mixer.music.play(-1)  # -1 signifie boucle infinie
        
        self.pygame_clock = pygame.time.Clock()
        self.pygame_clock.tick(30)
       
    def run(self):
        self.menu()
        in_game = True
        while in_game:

            # pygame.event
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT:
                    in_game = False
                elif event.type == pygame.VIDEORESIZE:
                    self.resize_window(event)
                
                # check keys
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and re.search("view_all_tamagotchis.*", self.display) or (self.display in ["red", "yellow", "green", "blue", "pink"]):
                        self.esc()
                
                # check buttons
                for button in self.buttons:
                    if button.is_clicked(event):
                        # main_menu
                        if button.action == "new_game":
                            self.view_all_tamagotchis()
                        elif button.action == "quit":
                            pygame.quit()
                        # view_all_tamagotchis
                        elif button.action == "red":
                            self.view_tamagotchi("red")
                        elif button.action == "yellow":
                            self.view_tamagotchi("yellow")
                        elif button.action == "green":
                            self.view_tamagotchi("green")
                        elif button.action == "blue":
                            self.view_tamagotchi("blue")
                        elif button.action == "pink":
                            self.view_tamagotchi("pink")
                        # esc
                        elif button.action == "view_all_tamagotchis":
                            self.view_all_tamagotchis()
                        elif button.action == "main_menu":
                            self.menu()

            pygame.display.flip()
        pygame.quit()

    #-------------------- views --------------------#
    def menu(self):
        self.display = "menu"
        self.map = pytmx.util_pygame.load_pygame(f'./assets/menu/menu.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.calcul_zoom()
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.create_buttons()

    def esc(self):
        self.display = "esc"
        self.map = pytmx.util_pygame.load_pygame(f'./assets/esc/esc.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.calcul_zoom()
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.create_buttons()

    def view_all_tamagotchis(self):
        self.display = f"view_all_tamagotchis_{self.name_map}"
        self.map = pytmx.util_pygame.load_pygame(f'./assets/{self.name_map}/{self.name_map}.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.calcul_zoom()
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)
        
        self.tamagotchis_positions = {}
        for layer in self.map.objectgroups:
            for obj in layer:
                self.tamagotchis_positions[obj.type] = (obj.x+16), obj.y
        print(self.tamagotchis_positions)

        self.create_buttons()

    def view_tamagotchi(self, tamagotchi):
        self.display = f"{tamagotchi}"
        self.map_layer.zoom = self.zoom * 2

        self.group.center(self.tamagotchis_positions[tamagotchi])
        self.group.draw(self.screen)
        self.map_layer.zoom = self.zoom

    #-------------------- others --------------------#
    def create_buttons(self):
        self.buttons.clear
        for layer in self.map.objectgroups:
            for obj in layer:
                self.buttons.append(Button(game, obj, obj.type))

    def calcul_zoom(self):
        self.height = self.screen.get_height()
        self.width = int(self.height * self.ratio)
        self.zoom = self.height / (self.map.height * self.map.tilewidth)


    def resize_window(self, event):
        self.calcul_zoom()
        pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

        if self.display == "menu":
            self.menu()
        elif re.search("view_all_tamagotchis.*", self.display):
            self.view_all_tamagotchis()
        elif self.display in ["red", "yellow", "green", "blue", "pink"]:
            self.view_tamagotchi(self.display)
        elif self.display == "esc":
            self.esc()



if __name__ == '__main__':
    pygame.init()
    game = Gui()
    game.run()
