import webbrowser

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
        zoom = screen.get_size()[0] / MAP_SIZE[0]
        for layer in self.map.objectgroups:
            for obj in layer:
                self.buttons.append(Button(screen, getattr(self, obj.type), zoom * obj.x, zoom * obj.y, zoom * obj.width, zoom * obj.height))
        self.map_layer.zoom = zoom

    def new_game(self, event):
        self.redirect('home')

    def load_game(self, event):
        ...

    def settings(self, event):
        ...

    def credits(self, event):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        pygame.quit()
        exit(0)
