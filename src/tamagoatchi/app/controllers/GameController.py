from tamagoatchi.lib.communication import Request, Response, ResponseType
from tamagoatchi.lib.controller import Controller
from tamagoatchi.lib.view import View
from tamagoatchi.app.models import Player


class GameController(Controller):

    @staticmethod
    def new_game(request: Request) -> Response:
        player: Player = Player()
        view = View('game', {'player': player}, request.json)
        return Response(ResponseType.valid, view)
