import pygame
import pyscroll
from pygame import Surface, SurfaceType

from tamagoatchi.app.definitions import RATIO
from tamagoatchi.lib.view import GUIView


class TamagotchiView(GUIView):
    """
    Class used to represent view for each tamagotchi
    """
    file_name = 'house'

    def __init__(self, screen: Surface | SurfaceType, click_pos: tuple, ext_dict: dict):
        """
        Method that define on what tamagotchi zoom in function of it position
        """
        super().__init__(screen, ext_dict)
        self.positions = {}
        for layer in self.map.objectgroups:
            for obj in layer:
                self.positions[obj.type] = obj.x, obj.y
        self.map_layer.zoom = self.zoom * 2
        tamagotchi = ''
        for key, value in self.positions.items():
            if (click_pos[0]//self.zoom in range(int(value[0]), int(value[0]+16))
                    and click_pos[1]//self.zoom in range(int(value[1]), int(value[1])+16)):
                tamagotchi = key
                break
        self.group.center(self.positions[tamagotchi])

    def on_key_pressed(self, event):
        """
        Method that define escape action
        """
        super().on_key_pressed(event)
        if event.key == pygame.K_ESCAPE:
            self.redirect('home')
        return
