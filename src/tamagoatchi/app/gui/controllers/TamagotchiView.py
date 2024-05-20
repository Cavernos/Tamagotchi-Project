import pygame
from pygame import Surface, SurfaceType

from tamagoatchi.lib.view import GUIView


class TamagotchiView(GUIView):
    file_name = 'house'

    def __init__(self, screen: Surface | SurfaceType, tamagotchi, ext_dict: dict):
        super().__init__(screen, ext_dict)
        self.rect = pygame.Rect(48, 48, 120, 120)
        self.map_layer.zoom = self.zoom + 2

    def on_key_pressed(self, event):
        super().on_key_pressed(event)
        if event.key == pygame.K_ESCAPE:
            self.redirect('home')
        return

