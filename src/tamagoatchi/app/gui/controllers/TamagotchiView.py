import pygame
from pygame import Surface, SurfaceType

from tamagoatchi.app.models import tamagotchis
from tamagoatchi.lib.view import GUIView


class TamagotchiView(GUIView):
    file_name = 'house'

    def __init__(self, screen: Surface | SurfaceType, click_pos: tuple, ext_dict: dict):
        super().__init__(screen, ext_dict)
        for tamagotchi in tamagotchis:
            if tamagotchi['position'] in click_pos:
                self.rect = pygame.Rect(tamagotchi['position'][0], tamagotchi['position'][1], 120, 120)
                break
        self.map_layer.zoom = self.zoom + 2

    def on_key_pressed(self, event):
        super().on_key_pressed(event)
        if event.key == pygame.K_ESCAPE:
            self.redirect('home')
        return

