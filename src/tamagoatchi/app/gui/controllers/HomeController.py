import pygame

from tamagoatchi.app.gui.views import MenuView
from tamagoatchi.lib.communication import Request, Response, ResponseType


class HomeController:
    """
    Class used to control the splash screen
    """
    @staticmethod
    def show_home(request: Request) -> Response:
        """
        Method used to display Main Menu
        """
        view = MenuView(pygame.display.get_surface(), request.json)
        return Response(ResponseType.valid, view)
