import pygame

from tamagoatchi.app.definitions import ROOT_SIZE
from tamagoatchi.app.gui.views import MenuView
from tamagoatchi.app.gui.views.HouseView import HouseView
from tamagoatchi.lib.communication import Request, Response, ResponseType


class HomeController:
    @staticmethod
    def show_home(request: Request) -> Response:
        view = MenuView(pygame.display.get_surface(), request.json)
        return Response(ResponseType.valid, view)
