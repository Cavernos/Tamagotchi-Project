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
    """
    Class used to represent the game view
    """
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        """
        Method used to add all buttons of the view
        """
        super().__init__(screen, ext_dict)
        for layer in self.map.objectgroups:
            for obj in layer:
                self.buttons.append(Button(screen, self.view_tamagotchi, self.zoom * obj.x,
                                           self.zoom * obj.y, self.zoom * obj.width, self.zoom * obj.height))

    def on_key_pressed(self, event):
        """
        Method used to return to home when Esc Key is pressed
        """
        super().on_key_pressed(event)
        if event.key == pygame.K_ESCAPE:
            self.redirect('')
        return

    def view_tamagotchi(self, event):
        """
        Method that define action for all tamagotchi button
        """
        self.redirect('game.tamagotchi', click_pos=event.pos)
        return
