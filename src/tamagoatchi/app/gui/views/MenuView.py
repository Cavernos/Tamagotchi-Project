import pygame
import pytmx
import pyscroll
from pygame import Surface, SurfaceType

from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.lib.view import GUIView
from tamagoatchi.lib.widgets import Button


class MenuView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(screen, ext_dict)
        map = pytmx.util_pygame.load_pygame(self.view_location)
        zoom = screen.get_size()[0] / MAP_SIZE[0]
        self.buttons.append(Button(screen, self.new_game, zoom * 92, zoom * 87, zoom * 74, zoom * 7))
        self.buttons.append(Button(screen, self.quit, zoom * 95, zoom * 124, zoom * 66, zoom * 7))
        for button in self.buttons:
            button.draw()
        map_data = pyscroll.TiledMapData(map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, pygame.display.get_window_size())
        self.map_layer.zoom = zoom

    def new_game(self, event):
        self.redirect('home')
