import json

from tamagoatchi.lib.communication import Response, Request, ResponseType
from tamagoatchi.lib.controller import Controller
from tamagoatchi.lib.event import Event, EventType
from tamagoatchi.lib.view import View


class HomeController(Controller):
    @staticmethod
    def show_home(request: Request) -> Response:
        view = View('', {}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def exit(request: Request) -> None:
        exit(0)
