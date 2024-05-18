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
                print(event)
                if event.type == pygame.QUIT:
                    in_game = False
                elif event.type == pygame.VIDEORESIZE:
                    self.resize_window(event)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and re.search("view_all_tamagotchis.*", self.display) or re.search("view_tamagotchi.*", self.display):
                        self.esc()
                for button in self.buttons:
                    if button.is_clicked(event):
                        if button.action == "view_tamagotchi_red":
                            self.view_tamagotchi("red")
                        elif button.action == "view_tamagotchi_yellow":
                            self.view_tamagotchi("yellow")
                        elif button.action == "view_tamagotchi_green":
                            self.view_tamagotchi("green")
                        elif button.action == "view_tamagotchi_blue":
                            self.view_tamagotchi("blue")
                        elif button.action == "view_tamagotchi_pink":
                            self.view_tamagotchi("pink")
                        elif button.action == "menu":
                            self.menu()
                        elif button.action == "new_game":
                            self.view_all_tamagotchis("map_maison")
                        elif button.action == "quit":
                            pygame.quit()

            pygame.display.flip()
        pygame.quit()

    def menu(self):
        self.display = "menu"
        self.map = pytmx.util_pygame.load_pygame(f'./assets/menu/menu.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.buttons = [Button(self, "new_game", self.zoom*92, self.zoom*87, self.zoom*74, self.zoom*7),
                        Button(self, "quit", self.zoom*95, self.zoom*124, self.zoom*66, self.zoom*7)]

    def esc(self):
        self.display = "esc"
        self.map = pytmx.util_pygame.load_pygame(f'./assets/esc/esc.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.buttons = [Button(self, "new_game", self.zoom*105, self.zoom*32, self.zoom*46, self.zoom*7),
                        Button(self, "esc", self.zoom*102, self.zoom*47, self.zoom*53, self.zoom*7),
                        Button(self, "save", self.zoom*100, self.zoom*64, self.zoom*57, self.zoom*7),
                        Button(self, "menu", self.zoom*96, self.zoom*81, self.zoom*67, self.zoom*7),
                        Button(self, "quit", self.zoom*96, self.zoom*98, self.zoom*66, self.zoom*7)]

    def resize_window(self, event):
        new_height = event.h
        new_width = int(new_height * self.ratio)
        self.zoom = new_height / 144
        pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

        if self.display == "menu":
            self.menu()
        elif re.search("view_all_tamagotchis.*", self.display):
            self.view_all_tamagotchis("map_maison")
        elif re.search("view_tamagotchi.*", self.display):
            self.view_all_tamagotchis("red")
        elif self.display == "esc":
            self.esc()

    def view_all_tamagotchis(self, map):
        self.tamagotchis_positions = {"red": (48, 48),
                                      "yellow": (48, 112),
                                      "green": (144, 112),
                                      "blue": (192, 96),
                                      "pink": (208, 48)}
        self.display = f"view_all_tamagotchis_{map}"
        self.map = pytmx.util_pygame.load_pygame(f'./assets/{map}/{map}.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.buttons = [Button(self, "view_tamagotchi_red", self.zoom*self.tamagotchis_positions["red"][0], self.zoom*self.tamagotchis_positions["red"][1], self.zoom*16, self.zoom*16),
                        Button(self, "view_tamagotchi_yellow", self.zoom*self.tamagotchis_positions["yellow"][0], self.zoom*self.tamagotchis_positions["yellow"][1], self.zoom*16, self.zoom*16),
                        Button(self, "view_tamagotchi_green", self.zoom*self.tamagotchis_positions["green"][0], self.zoom*self.tamagotchis_positions["green"][1], self.zoom*16, self.zoom*16),
                        Button(self, "view_tamagotchi_blue", self.zoom*self.tamagotchis_positions["blue"][0], self.zoom*self.tamagotchis_positions["blue"][1], self.zoom*16, self.zoom*16),
                        Button(self, "view_tamagotchi_pink", self.zoom*self.tamagotchis_positions["pink"][0], self.zoom*self.tamagotchis_positions["pink"][1], self.zoom*16, self.zoom*16)]

    def view_tamagotchi(self, tamagotchi):
        self.display = f"view_tamagotchi_{tamagotchi}"
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = self.zoom + 2

        self.view = pygame.Rect(self.tamagotchis_positions[tamagotchi][0], self.tamagotchis_positions[tamagotchi][1], 120, 120)

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.buttons = []



if __name__ == '__main__':
    pygame.init()
    game = Gui()
    game.run()
