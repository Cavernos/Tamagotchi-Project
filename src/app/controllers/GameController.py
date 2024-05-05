from lib.communication import Request, Response, ResponseType
from lib.controller import Controller
from lib.view import View
from models.player import Player


class GameController(Controller):

    @staticmethod
    def new_game(request: Request) -> Response:
        player: Player = Player()
        view = View('game', {'player': player}, request.json)
        return Response(ResponseType.valid, view)
