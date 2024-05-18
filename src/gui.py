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
    def __init__(self,
                 width: int=1024,
                 height: int=576,
                 zoom:int = 4):
        self.event = Event()
        self.clock = Clock("console_game", self.event)
        self.player = Player("John") 
        self.zoom = zoom

        # screen
        self.screen = pygame.display.set_mode((width, height))
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
                if event.type == pygame.QUIT:
                    in_game = False
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
    
    def view_all_tamagotchis(self):
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