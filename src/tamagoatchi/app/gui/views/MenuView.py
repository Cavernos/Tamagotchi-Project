import webbrowser

import pygame
import pytmx
import pyscroll
from pygame import Surface, SurfaceType

from tamagoatchi.app.definitions import MAP_SIZE
from tamagoatchi.lib.view import GUIView
from tamagoatchi.lib.widgets import Button


class MenuView(GUIView):
    """
    Class used to represent splash screen view
    """

    def __init__(self, screen: Surface | SurfaceType, ext_dict: dict):
        """
        Define buttons for Menu view
        """
        super().__init__(screen, ext_dict)
        for layer in self.map.objectgroups:
            for obj in layer:
                self.buttons.append(
                    Button(screen,
                           getattr(self, obj.type),
                           self.zoom * obj.x,
                           self.zoom * obj.y,
                           self.zoom * obj.width,
                           self.zoom * obj.height)
                )

    def new_game(self, event):
        """
        New game button action
        """
        self.redirect('home')

    def load_game(self, event):
        # TODO
        ...

    def settings(self, event):
        # TODO
        ...

    def credits(self, event):
        """
        credits button action
        """
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        pygame.quit()
        exit(0)
