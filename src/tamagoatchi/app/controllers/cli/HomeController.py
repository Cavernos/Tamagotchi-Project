import json

from tamagoatchi.lib.communication import Response, Request, ResponseType
from tamagoatchi.lib.controller import Controller
<<<<<<<< HEAD:src/tamagoatchi/app/cli/controllers/HomeController.py
========
from tamagoatchi.lib.event import Event, EventType
>>>>>>>> d947d55 (Refactor to welcome the new gui version):src/tamagoatchi/app/controllers/cli/HomeController.py
from tamagoatchi.lib.view import ConsoleView


class HomeController(Controller):
    """
    Class used to show home page and exit the game
    """
    @staticmethod
    def show_home(request: Request) -> Response:
        view = ConsoleView('', {}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def exit(request: Request) -> None:
        exit(0)
