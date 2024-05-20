import pygame
import pyscroll
from pygame import Surface, SurfaceType
import pytmx

from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.lib.event import EventManager
from tamagoatchi.lib.handlers import ResourceHandler
from tamagoatchi.lib.view import GUIView
from tamagoatchi.lib.widgets import Button


class HouseView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(screen, ext_dict)
        self.buttons.append(Button(self, self.view_tamagotchi_red, self.zoom*48, self.zoom*48, self.zoom*16, self.zoom*16))

    def on_key_pressed(self, event):
        super().on_key_pressed(event)
        if event.key == pygame.K_ESCAPE:
            self.redirect('')
        return

    def view_tamagotchi_red(self, event):
        self.redirect('game.red_tamagotchi')
        return
