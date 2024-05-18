import pygame
import pytmx
import pyscroll
from pygame import Surface, SurfaceType

from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.lib.event import EventHandler
from tamagoatchi.lib.view import GUIView


class MenuView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(ext_dict)
        self.screen = screen
        map = pytmx.util_pygame.load_pygame(self.view_location)
        map_data = pyscroll.TiledMapData(map)
        self.map_layer = pyscroll.orthographic.BufferedRenderer(map_data, pygame.display.get_window_size())
        self.map_layer.zoom = screen.get_size()[0] / MAP_SIZE[0]

    def render(self):
        pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=1).draw(self.screen)

    @staticmethod
    @EventHandler.register(pygame.VIDEORESIZE)
    def on_resize(event):
        pygame.display.set_mode(event.dict['size'], pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.update()

    @staticmethod
    @EventHandler.register(pygame.MOUSEBUTTONDOWN)

