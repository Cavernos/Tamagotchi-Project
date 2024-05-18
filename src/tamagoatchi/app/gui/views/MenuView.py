<<<<<<< HEAD
<<<<<<< HEAD
import webbrowser
=======
import logging
>>>>>>> 440c2b5 (Test MVC Gui)

=======
>>>>>>> 4b602c8 (prepare to get Nicolas's Code)
import pygame
import pytmx
import pyscroll
from pygame import Surface, SurfaceType

<<<<<<< HEAD
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
=======
from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.lib.event import EventHandler
>>>>>>> 4b602c8 (prepare to get Nicolas's Code)
from tamagoatchi.lib.view import GUIView


class MenuView(GUIView):
    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        super().__init__(ext_dict)
        self.screen = screen
        map = pytmx.util_pygame.load_pygame(self.view_location)
        map_data = pyscroll.TiledMapData(map)
<<<<<<< HEAD
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, pygame.display.get_window_size())
        map_layer.zoom = 4
        pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1).draw(self.screen)
>>>>>>> 440c2b5 (Test MVC Gui)
=======
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

>>>>>>> 4b602c8 (prepare to get Nicolas's Code)
