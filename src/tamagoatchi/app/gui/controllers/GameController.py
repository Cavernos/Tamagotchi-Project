import pygame.display

from tamagoatchi.app.gui.views import TamagotchiView
from tamagoatchi.app.gui.views import HouseView
from tamagoatchi.lib.communication import Request, Response, ResponseType


class GameController:
    """
    Class used to control the game
    """
    @staticmethod
    def start_game(request: Request) -> Response:
        """
        Method used to display the house view
        """
        view = HouseView(pygame.display.get_surface(), request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def view_tamagotchi(request: Request) -> Response:
        """
        Method used to zoom on a tamagotchi in function of what tamagotchi is clicked
        """
        view = TamagotchiView(pygame.display.get_surface(), request.json['ext']['click_pos'], request.json)
        return Response(ResponseType.valid, view)
