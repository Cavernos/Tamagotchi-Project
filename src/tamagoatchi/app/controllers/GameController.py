import json

from tamagoatchi.app.time import Clock
from tamagoatchi.lib.communication import Request, Response, ResponseType
from tamagoatchi.lib.controller import Controller
from tamagoatchi.lib.view import View
from tamagoatchi.app.models import tamagotchi_file
from tamagoatchi.app.models import Player


class GameController(Controller):
    def __init__(self) -> None:
        self.clock = Clock(name='game_clock')
        self.clock.start()

    @staticmethod
    def new_game(request: Request) -> Response:
        player: Player = Player()
        view = View('game', {'player': player}, request.json)
        return Response(ResponseType.valid, view)

    def game(self, request: Request) -> Response:
        if "ext" in request.inputs.keys():
            player: Player = Player.get_instance(request.inputs["ext"][0])
        else:
            player = Player()
        if not self.clock.is_alive():
            self.clock.join()
            return Response(ResponseType.error, View('',
                                                     {"error": "Vous avez perdu ! Un des tamagotchis est mort"},
                                                     request.json))
        return Response(ResponseType.valid, View('game',
                                                 {'tamagotchis': tamagotchi_file,
                                                  'player': player
                                                  },
                                                 request.json))

    def play(self, request: Request) -> Response:
        name_of_tamagotchi = request.inputs['name']
        player = Player.get_instance(request.inputs['ext'][0])
        for tamagotchi in tamagotchi_file.tamagotchis:
            if tamagotchi['name'] == name_of_tamagotchi and self.clock.day_duration > tamagotchi['night_duration']:
                player.play_with(tamagotchi)
        request.json['form_redirect'] = 'game.load'
        return Response(ResponseType.valid, View("game",
                                                 {'player': player, 'tamagotchis': tamagotchi_file},
                                                 request.json))

    def eat(self, request: Request) -> Response:
        name_of_tamagotchi = request.inputs['name']
        player = Player.get_instance(request.inputs['ext'][0])
        for tamagotchi in tamagotchi_file.tamagotchis:
            if tamagotchi['name'] == name_of_tamagotchi and self.clock.day_duration > tamagotchi['night_duration']:
                player.give_biscuit(tamagotchi)
        request.json['form_redirect'] = 'game.load'
        return Response(ResponseType.valid, View("game",
                                                 {'player': player, 'tamagotchis': tamagotchi_file},
                                                 request.json))
