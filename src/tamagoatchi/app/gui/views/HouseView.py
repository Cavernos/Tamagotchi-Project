import pygame
import pyscroll
from pygame import Surface, SurfaceType
import pytmx

from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.lib.view import GUIView
from tamagoatchi.lib.widgets import Button


class HouseView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(screen, ext_dict)
        map = pytmx.util_pygame.load_pygame(self.view_location)
        zoom = screen.get_size()[0] / MAP_SIZE[0]
        map_data = pyscroll.TiledMapData(map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, pygame.display.get_window_size())
        self.map_layer.zoom = zoom
