import json

from tamagoatchi.app.time import Clock
from tamagoatchi.lib.communication import Request, Response, ResponseType
from tamagoatchi.lib.controller import Controller
from tamagoatchi.lib.view import View
from tamagoatchi.app.models import tamagotchi_file
from tamagoatchi.app.models import Player


class GameController(Controller):

    @staticmethod
    def new_game(request: Request) -> Response:
        player: Player = Player()
        view = View('game', {'player': player}, request.json)
        return Response(ResponseType.valid, view)

    @staticmethod
    def load_game(request: Request) -> Response:
        if "ext" in request.inputs.keys():
            player: Player = Player.get_instance(request.inputs["ext"][0])
        else:
            player = Player()
        clock = Clock(name="")
        clock.start()
        if not clock.is_alive():
            return Response(ResponseType.error, View('', {"error": "Vous avez perdu !"}, request.json))
        return Response(ResponseType.valid, View('game',
                                                 {'tamagotchis': tamagotchi_file,
                                                  'player': player
                                                  },
                                                 request.json))

    @staticmethod
    def play(request: Request) -> Response:
        name_of_tamagotchi = request.inputs['name']
        player = Player.get_instance(request.inputs['ext'][0])
        for tamagotchi in tamagotchi_file.tamagotchis:
            if tamagotchi['name'] == name_of_tamagotchi:
                player.play_with(tamagotchi)
        request.json['form_redirect'] = 'game.load'
        return Response(ResponseType.valid, View("game",
                                                 {'player': player, 'tamagotchis': tamagotchi_file},
                                                 request.json))

    @staticmethod
    def eat(request: Request) -> Response:
        name_of_tamagotchi = request.inputs['name']
        player = Player.get_instance(request.inputs['ext'][0])
        for tamagotchi in tamagotchi_file.tamagotchis:
            if tamagotchi['name'] == name_of_tamagotchi:
                player.give_biscuit(tamagotchi)
        request.json['form_redirect'] = 'game.load'
        return Response(ResponseType.valid, View("game",
                                                 {'player': player, 'tamagotchis': tamagotchi_file},
                                                 request.json))
