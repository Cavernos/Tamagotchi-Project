import pygame
import pyscroll
from pygame import Surface, SurfaceType
import pytmx

from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.app.models import tamagotchis
from tamagoatchi.lib.event import EventManager
from tamagoatchi.lib.handlers import ResourceHandler
from tamagoatchi.lib.view import GUIView
from tamagoatchi.lib.widgets import Button


class HouseView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(screen, ext_dict)
        for tamagotchi in tamagotchis:
            self.buttons.append(Button(self, self.view_tamagotchi,
                                       self.zoom*tamagotchi['position'][0],
                                       self.zoom*tamagotchi['position'][1], self.zoom*16, self.zoom*16))

    def on_key_pressed(self, event):
        super().on_key_pressed(event)
        if event.key == pygame.K_ESCAPE:
            self.redirect('')
        return

    def view_tamagotchi(self, event):
        self.redirect('game.tamagotchi', event.pos)
        return
