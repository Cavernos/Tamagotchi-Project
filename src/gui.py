# dev Nicolas

# import
import pygame
import pytmx
import pyscroll

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
        
        self.ratio = 9 / 16
        self.width = 1024
        self.height = int(self.width * self.ratio)
        self.zoom = 4

        # screen
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption("TamaGOATchi")
        game_icon = pygame.image.load('./assets/tamagotchis/default.png')
        pygame.display.set_icon(game_icon)
        
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
                if event.type == pygame.VIDEORESIZE:
                    self.resize_window(event)
                for button in self.buttons:
                    if button.is_clicked(event):
                        if button.action == "quit":
                            pygame.quit()
                        if button.action == "settings":
                            self.menu()
                        if button.action == "new_game":
                            self.view_all_tamagotchis()


            pygame.display.flip()
        pygame.quit()

    def menu(self):
        self.display = "menu"
        self.map = pytmx.util_pygame.load_pygame('./assets/menu/menu.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.buttons = [Button(self, "new_game", self.zoom*92, self.zoom*87, self.zoom*74, self.zoom*7),
                        Button(self, "quit", self.zoom*95, self.zoom*124, self.zoom*66, self.zoom*7)]

    def setting(self):
        ...

    def resize_window(self, event):
        new_width = event.w
        new_height = int(new_width * self.ratio)
        self.zoom = event.w / 256
        self.map_layer.zoom = self.zoom
        pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)

        if self.display == "menu":
            self.menu()
        elif self.display == "view_all_tamagotchis":
            self.view_all_tamagotchis()
        
    
    def view_all_tamagotchis(self):
        self.display = "view_all_tamagotchis"
        self.map = pytmx.util_pygame.load_pygame('./assets/map_maison/map_maison.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = self.zoom

        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        self.group.draw(self.screen)

        self.buttons = [Button(self, "settings", 0, 0, self.zoom*16, self.zoom*16, (70, 70, 70, 128))]

    def view_tamagotchi(self, tamagotchi):
        ...



if __name__ == '__main__':
    pygame.init()
    game = Gui()
    game.run()