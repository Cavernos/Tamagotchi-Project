<<<<<<< HEAD
import webbrowser
=======
import logging
>>>>>>> 440c2b5 (Test MVC Gui)

import pygame
import pytmx
import pyscroll
from pygame import Surface, SurfaceType

<<<<<<< HEAD
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
=======
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
>>>>>>> 440c2b5 (Test MVC Gui)
