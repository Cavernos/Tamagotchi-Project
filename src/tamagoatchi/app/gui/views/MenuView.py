import logging

import pygame
import pytmx
import pyscroll
from pygame import Surface, SurfaceType

from tamagoatchi import logger
from tamagoatchi.lib.view import GUIView


class MenuView(GUIView):
    def __init__(self, screen: Surface | SurfaceType):
        self.screen = screen
        super().__init__()

    def render(self):
        map = pytmx.util_pygame.load_pygame(self.view_location)
        map_data = pyscroll.TiledMapData(map)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, pygame.display.get_window_size())
        map_layer.zoom = 4
        pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1).draw(self.screen)
