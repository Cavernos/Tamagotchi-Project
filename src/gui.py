# dev Nicolas

# import
import pygame
import pytmx
import pyscroll

from threading import Event

import pytmx.util_pygame
from clock import Clock
from models.player import Player
import tamagotchi


class Gui:
    def __init__(self,
                 width: int=1024,
                 height: int=576):
        self.event = Event()
        self.clock = Clock("console_game", self.event)
        self.player = Player("John") 

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("TamaGOATchi")
        self.pygame_clock = pygame.time.Clock()
        self.pygame_clock.tick(30)  # limits FPS
        
        # map
        self.map = pytmx.util_pygame.load_pygame('./assets/menu/menu.tmx')
        self.map_data = pyscroll.data.TiledMapData(self.map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(self.map_data, self.screen.get_size())
        self.map_layer.zoom = 4

        # layer
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1)
        

    def run(self):
        # main loop
        in_game = True
        while in_game:
            self.screen.fill("white")
            self.group.draw(self.screen)
            pygame.display.flip()

            # pygame.QUIT
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
    
        
        pygame.quit()

    def menu(self):
        ...
    
    def setting(self):
        ...
    
    def view_all_tamagotchis(self):
        ...
    
    def view_tamagotchi(self, tamagotchi):
        ...



if __name__ == '__main__':
    pygame.init()
    game = Gui()
    game.run()