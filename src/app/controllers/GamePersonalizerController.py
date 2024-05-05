from app.models import Player
from lib.communication import Response, Request, ResponseType
from lib.view import View


class GamePersonalizerController:
    @staticmethod
    def show_personalization(request: Request) -> Response:
        view = View('personalization', {}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def new_player(request: Request) -> Response:
        playername = request.json['inputs']['name']
        player = Player(playername)
        view = View('personalization', {'player': player}, request.json)
        return Response(ResponseType.valid, view)
