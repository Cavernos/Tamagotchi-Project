import pygame.display

from tamagoatchi.app.gui.controllers.TamagotchiView import TamagotchiView
from tamagoatchi.app.gui.views.HouseView import HouseView
from tamagoatchi.lib.communication import Request, Response, ResponseType


class GameController:
    @staticmethod
    def start_game(request: Request) -> Response:
        view = HouseView(pygame.display.get_surface(), request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def view_tamagotchi(request: Request) -> Response:
        view = TamagotchiView(pygame.display.get_surface(), request.json['ext'], request.json)
        return Response(ResponseType.valid, view)
